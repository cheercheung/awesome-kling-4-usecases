#!/usr/bin/env python3
"""Check complete case/data/CSV/localization/media parity from a clean checkout."""
import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LOCALES = {'es':('Caso','por'),'pt':('Caso','por'),'ja':('ケース','投稿者'),'ko':('사례','작성자'),'de':('Fall','von'),'fr':('Cas','par'),'tr':('Örnek','yazan'),'zh-TW':('案例','作者'),'zh-CN':('案例','作者'),'ru':('Пример','автор')}
CASE = re.compile(r'^<a id="case-(\d+)"></a>\n### ([^\n:]+) \1: \[([^\]]+)\]\((https://[^)]+)\) \(([^\n]+) \[@([^\]]+)\]\((https://[^)]+)\)\)',re.M)
CODES = re.compile(r'^```[^\n]*\n(.*?)\n```$',re.M|re.S)
IMAGES = re.compile(r'!\[[^\]]*\]\((https://[^)]+)\)')
errors=[]
def expect(condition,message):
    if not condition:errors.append(message)
def blocks(text):
    found=list(CASE.finditer(text))
    result=[]
    for i,m in enumerate(found):
        end=found[i+1].start() if i+1<len(found) else len(text)
        section=re.search(r'^## ',text[m.end():end],re.M)
        if section:end=m.end()+section.start()
        result.append((m,text[m.end():end]))
    return result
def sha(text):return hashlib.sha256(text.encode()).hexdigest()
def anchors(text):
    ids=set(re.findall(r'<a\s+id="([^"]+)"',text))
    for heading in re.findall(r'^#{1,6} (.+)$',text,re.M):
        heading=re.sub(r'<[^>]+>','',heading).lower()
        heading=re.sub(r'[^\w\- ]','',heading,flags=re.U).replace(' ','-')
        ids.add(heading)
    return ids

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--english-only',action='store_true');args=parser.parse_args()
    data=json.loads((ROOT/'data/use-cases.json').read_text())
    items=data['items']; english=(ROOT/'README.md').read_text(); enblocks=blocks(english)
    expect(len(items)>0,'empty curated dataset')
    expect([c['public_number'] for c in items]==list(range(1,len(items)+1)),'dataset public numbering is not contiguous')
    expect(len({c['source_url'] for c in items})==len(items),'duplicate dataset source URL')
    expect(sum(c['expected_public_visual_count'] for c in items)==data['expected_public_visual_count'],'dataset visual denominator differs from manifest')
    expect(len(enblocks)==len(items),'English case count differs from curated dataset')
    expected_codes=[]
    for (match,body),c in zip(enblocks,items):
        n,label,title,source,by,handle,author=match.groups();prefix=f'case {c["public_number"]}'
        expect((int(n),label,title,source,by,handle,author)==(c['public_number'],'Case',c['title'],c['source_url'],'by',c['author_handle'],c['author_url']),prefix+': English identity differs from dataset')
        takeaway=re.search(r'^\*\*(.+)\*\*$',body,re.M)
        expect(takeaway is not None and takeaway.group(1)==c['takeaway'],prefix+': takeaway differs from dataset')
        for note in c['body_notes']:expect(note in body,prefix+': source note missing')
        expect(f'Type: {c["type"]} | Date: {c["date"]}' in body,prefix+': metadata differs from dataset')
        expect(f'[![{c["title"]}]({c["poster_url"]})]({c["playable_video_url"]})' in body,prefix+': poster/playback pair missing')
        expected=[c['poster_url'],*c['r2_media_urls']]
        observed=IMAGES.findall(body)
        expect(observed==expected,prefix+': media set/order differs from source-derived denominator')
        expect(c['source_media_count']==len(c['source_media_urls'])==len(expected)==c['expected_public_visual_count'],prefix+': source/public media counts differ')
        for url in expected+[c['playable_video_url']]:expect('.r2.dev/' in url,prefix+': non-R2 display/playback URL')
        actual_codes=CODES.findall(body)
        expect(actual_codes==[p['text'] for p in c['prompts']],prefix+': Prompt text differs from source dataset')
        for p in c['prompts']:expect(sha(p['text'])==p['sha256'],prefix+': Prompt source hash mismatch')
        expected_codes += actual_codes
    expect(CODES.findall(english)==expected_codes,'English has unaccounted code/Prompt blocks')
    with (ROOT/'data/use-cases.csv').open(newline='') as handle:rows=list(csv.DictReader(handle))
    expect(len(rows)==len(items),'CSV count differs from dataset')
    for row,c in zip(rows,items):
        for k in ['public_number','group_id','category','type','title','date','author_handle','source_url','duration_seconds','playable_video_url']:
            expect(row.get(k)==str(c[k]),f'CSV {c["group_id"]}: {k} differs')
        for k,v in c['metrics'].items():expect(row.get(k)==('' if v is None else str(v)),f'CSV {c["group_id"]}: {k} differs')
        expect(row.get('prompt_count')==str(len(c['prompts'])),f'CSV {c["group_id"]}: Prompt count differs')
    expected_files={'README.md'}|{'README_'+x+'.md' for x in LOCALES}
    if not args.english_only:
        expect({p.name for p in ROOT.glob('README*.md')}==expected_files,'README language file set differs from 11-language policy')
        en_headings=re.findall(r'^## ',english,re.M)
        for locale,(label,by) in LOCALES.items():
            path=ROOT/('README_'+locale+'.md')
            if not path.exists():continue
            text=path.read_text();localized=blocks(text)
            expect(len(localized)==len(items),f'{path.name}: case count differs')
            expect(len(re.findall(r'^## ',text,re.M))==len(en_headings),f'{path.name}: section count differs')
            expect(CODES.findall(text)==expected_codes,f'{path.name}: immutable code/Prompt text differs')
            for (match,body),c in zip(localized,items):
                n,actual_label,title,source,actual_by,handle,author=match.groups();prefix=f'{path.name} case {c["public_number"]}'
                expect((int(n),actual_label,source,actual_by,handle,author)==(c['public_number'],label,c['source_url'],by,c['author_handle'],c['author_url']),prefix+': immutable identity/localized labels differ')
                expect(title!=c['title'],prefix+': untranslated title')
                takeaway=re.search(r'^\*\*(.+)\*\*$',body,re.M)
                expect(takeaway is not None and takeaway.group(1)!=c['takeaway'],prefix+': untranslated/missing takeaway')
                expect(IMAGES.findall(body)==[c['poster_url'],*c['r2_media_urls']],prefix+': source-derived media set differs')
                expect(f'](#case-{n})' in text and f'[{title}](#case-{n})' in text,prefix+': translated Menu title differs')
                expect(f'Type: {c["type"]} | Date: {c["date"]}' in body,prefix+': metadata differs')
    paths=[p for p in ROOT.rglob('*.md') if not {'.git','.codex'} & set(p.relative_to(ROOT).parts)]
    for path in paths:
        text=path.read_text();relative=path.relative_to(ROOT)
        for link in re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)',text):
            parsed=urlsplit(link)
            if parsed.scheme:
                if parsed.hostname=='evolink.ai':
                    expect('utm_source=github' in parsed.query and 'utm_campaign=awesome-kling-4-usecases' in parsed.query and 'utm_medium=' in parsed.query and 'utm_content=' in parsed.query,f'{relative}: unattributed EvoLink URL')
                continue
            target=path.parent/unquote(parsed.path) if parsed.path else path
            if args.english_only and target.name in expected_files and not target.exists():continue
            expect(target.is_file(),f'{relative}: missing relative target {link}')
            if target.is_file() and parsed.fragment and target.suffix=='.md':expect(unquote(parsed.fragment) in anchors(target.read_text()),f'{relative}: missing fragment {link}')
        expect(not re.search(r'^\s*<video\b',text,re.M|re.I),f'{relative}: raw video embed')
    if errors:
        print('FAIL');print('\n'.join('- '+e for e in errors));return 1
    print(f'PASS: {len(items)} complete cases; {data["expected_public_visual_count"]} source-derived visuals; {len(expected_codes)} exact Prompts; '+('English only' if args.english_only else '11 READMEs')+'; CSV and relative links')
    return 0
if __name__=='__main__':sys.exit(main())
