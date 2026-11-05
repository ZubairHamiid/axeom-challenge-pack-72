import pandas as pd
import re

pb = pd.read_csv('data/production_board.csv')
with open('data/messages.txt', 'r', encoding='utf-8') as f:
    messages = f.readlines()

# Map all video titles to video_id and client
print("Sample video titles on production board:")
print(pb[['video_id', 'client', 'title', 'revisions', 'notes_on_board', 'stage', 'editor']].head(10))

# For each video title, find all messages mentioning it
titles = pb['title'].dropna().unique()
print(f"Total unique video titles: {len(titles)}")

# Let's match messages to video titles
matches = []
for idx, line in enumerate(messages):
    line_clean = line.strip()
    if not line_clean:
        continue
    # find matching title
    found_vids = []
    for _, row in pb.iterrows():
        t = row['title'].lower()
        # check if title is in line
        if t in line_clean.lower():
            found_vids.append(row['video_id'])
    
    # Also check phrases like "the one we shot last week"
    if found_vids:
        matches.append((line_clean, found_vids))

print(f"Messages directly matching video title: {len(matches)}")
for m, vids in matches[:20]:
    print(f"VID {vids}: {m}")

