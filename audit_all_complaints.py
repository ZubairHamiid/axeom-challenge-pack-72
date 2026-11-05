import pandas as pd
import re

pb = pd.read_csv('data/production_board.csv')
with open('data/messages.txt', 'r', encoding='utf-8') as f:
    messages = [l.strip() for l in f if l.strip()]

complaint_patterns = [
    r'still not fixed',
    r'second time i ask',
    r'did anyone see my message',
    r'todav[ií]a no est[aá]',
    r'already told you'
]

print("=== AUDITING LOST REQUESTS ===")
# For each complaint, find the original request
for idx, m in enumerate(messages):
    is_complaint = any(re.search(cp, m, re.IGNORECASE) for cp in complaint_patterns)
    if is_complaint:
        # extract date, time, channel, sender, text
        print("\n" + "="*50)
        print(f"COMPLAINT [{idx}]: {m}")
        
        # Look back for original message
        # Extract title or topic mentioned in complaint
        # Find all preceding messages
        # Let's search preceding messages
        found_orig = []
        for p_idx in range(idx-1, -1, -1):
            pm = messages[p_idx]
            # check if video title in complaint matches video title in pm
            # or sender matches
            # Let's print candidate
            # match words of 4+ letters
            words = [w for w in re.findall(r'[a-zA-Z]{4,}', m) if w.lower() not in ['still', 'fixed', 'little', 'frustrated', 'honestly', 'second', 'time', 'wrong', 'anyone', 'message', 'already', 'told', 'about', 'from', 'whatsapp', 'email', 'voice', 'note', 'transcript']]
            if any(w.lower() in pm.lower() for w in words):
                found_orig.append((p_idx, pm))
        
        if found_orig:
            print("  ORIGINAL REQUEST CANDIDATES:")
            for p_idx, pm in found_orig:
                print(f"    [{p_idx}]: {pm}")
                # check corresponding video on PB
                # find PB video
                for _, row in pb.iterrows():
                    if row['title'].lower() in pm.lower() or any(w.lower() in row['title'].lower() for w in words):
                        print(f"      PB: {row['video_id']} | {row['client']} | {row['title']} | {row['editor']} | Stage: {row['stage']} | Notes: {row['notes_on_board']} | Revs: {row['revisions']}")
                        break

