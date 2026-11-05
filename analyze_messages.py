import pandas as pd
import re

pb = pd.read_csv('data/production_board.csv')
with open('data/messages.txt', 'r', encoding='utf-8') as f:
    messages = f.readlines()

print(f"Total messages: {len(messages)}")

# Let's see all videos on the production board
# video_id, client, title, editor, stage, notes_on_board, revisions, editor_hours, client_approved_on, shoot_booking
print("--- PRODUCTION BOARD COLUMNS & STAGES ---")
print(pb['stage'].value_counts())

# Parse messages
parsed_msgs = []
pattern = r'\[(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})\] (WHATSAPP|VOICE NOTE|EMAIL|INSTAGRAM DM|WEBSITE FORM)(?: from ([^:]+))?: (.+)'

for line in messages:
    line = line.strip()
    if not line:
        continue
    m = re.match(pattern, line)
    if m:
        dt, tm, channel, sender, content = m.groups()
        parsed_msgs.append({
            'date': dt,
            'time': tm,
            'channel': channel,
            'sender': sender,
            'content': content
        })

df_msgs = pd.DataFrame(parsed_msgs)
print(f"Parsed {len(df_msgs)} messages.")
print("Channels breakdown:")
print(df_msgs['channel'].value_counts())

# Find messages that talk about specific videos / revisions / edits
print("\nSample revision / edit requests in messages:")
keywords = ['video', 'edit', 'cut', 'caption', 'color', 'change', 'fix', 'remove', 'add', 'part', 'music', 'sound', 'phone', 'logo', 'transcript', 'revision']
edit_msgs = df_msgs[df_msgs['content'].apply(lambda c: any(k in c.lower() for k in keywords))].copy()
print(f"Messages mentioning video edits: {len(edit_msgs)}")

