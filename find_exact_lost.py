import pandas as pd
import re

pb = pd.read_csv('data/production_board.csv')
with open('data/messages.txt', 'r', encoding='utf-8') as f:
    messages = [l.strip() for l in f if l.strip()]

complaint_regex = re.compile(r'(still not fixed|second time i ask|did anyone see my message|todav[ií]a no est[aá]|already told you)', re.I)

# Parse all messages into structured records
parsed = []
for i, line in enumerate(messages):
    m = re.match(r'\[(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})\] (WHATSAPP|VOICE NOTE|EMAIL|INSTAGRAM DM|WEBSITE FORM)(?: from ([^:]+))?: (.+)', line)
    if m:
        dt, tm, ch, sender, content = m.groups()
        parsed.append({
            'idx': i,
            'date': dt,
            'time': tm,
            'channel': ch.lower(),
            'sender': sender or '',
            'content': content,
            'raw': line
        })

# Find all complaints
complaints = [p for p in parsed if complaint_regex.search(p['content'])]

print(f"Total complaint messages: {len(complaints)}")

lost_list = []
for c in complaints:
    # Find which video title is mentioned in c['content']
    # If not mentioned, check recent messages from same sender
    c_text = c['content'].lower()
    
    # Check matching video on PB
    matched_pb = []
    for _, row in pb.iterrows():
        title = row['title'].lower()
        if title in c_text:
            matched_pb.append(row)
    
    # If no title in complaint, check previous message from same sender
    orig_msg = None
    if matched_pb:
        target_title = matched_pb[0]['title'].lower()
        # look backward for original message containing target_title
        for prev in reversed(parsed[:c['idx']]):
            if target_title in prev['content'].lower() and not complaint_regex.search(prev['content']):
                orig_msg = prev
                break
    else:
        # Check previous messages from same sender
        for prev in reversed(parsed[:c['idx']]):
            if prev['sender'] == c['sender'] and not complaint_regex.search(prev['content']):
                orig_msg = prev
                # find title in prev
                for _, row in pb.iterrows():
                    if row['title'].lower() in prev['content'].lower():
                        matched_pb.append(row)
                break
    
    # Find why it was lost
    if orig_msg:
        # Determine why it was lost
        # Reasons:
        # 1. Voice note (audio not transcribed / listened by editor)
        # 2. Instagram DM (checked infrequently or missed)
        # 3. Spanish message (language barrier)
        # 4. Weekend / off-hours
        # 5. Phrased as "the one we shot last week" (ambiguous title)
        # 6. Notes not on board / revisions 0
        print(f"\nComplaint on {c['date']} by {c['sender']}: '{c['content']}'")
        print(f"  Orig request on {orig_msg['date']} via {orig_msg['channel']}: '{orig_msg['content']}'")
        if matched_pb:
            v = matched_pb[0]
            print(f"  Video: {v['video_id']} | {v['client']} | {v['title']} | Notes on board: {v['notes_on_board']} | Revs: {v['revisions']}")

