#!/usr/bin/env python3
"""Fetch public YouTube uploads into static JSON. Preserve last good data on failure."""
import json
import os
import pathlib
import re
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEST = ROOT / 'data' / 'videos.json'
CHANNEL = os.getenv('YOUTUBE_CHANNEL_ID', '').strip()
if not re.fullmatch(r'UC[A-Za-z0-9_-]{22}', CHANNEL):
    raise SystemExit('Set YOUTUBE_CHANNEL_ID to a valid UC... channel ID in repository variables.')
url = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + CHANNEL
request = urllib.request.Request(url, headers={'User-Agent': 'TkohV7SiteFeed/1.0'})
with urllib.request.urlopen(request, timeout=20) as response:
    content = response.read(1_000_001)
if len(content) > 1_000_000:
    raise SystemExit('Feed exceeds size limit')
root = ET.fromstring(content)
ns = {'atom': 'http://www.w3.org/2005/Atom', 'yt': 'http://www.youtube.com/xml/schemas/2015'}
items = []
for entry in root.findall('atom:entry', ns):
    video_id = entry.findtext('yt:videoId', default='', namespaces=ns)
    title = entry.findtext('atom:title', default='', namespaces=ns).strip()
    published = entry.findtext('atom:published', default='', namespaces=ns)
    if re.fullmatch(r'[A-Za-z0-9_-]{11}', video_id) and title:
        items.append({'id': video_id, 'title': title[:200], 'description': published[:10], 'url': 'https://www.youtube.com/watch?v=' + video_id})
if not items:
    raise SystemExit('No valid videos found; preserving existing JSON')
DEST.write_text(json.dumps(items[:15], indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(f'Updated {len(items)} video records')
