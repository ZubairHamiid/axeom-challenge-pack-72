import pandas as pd
import re

pb = pd.read_csv('data/production_board.csv')
with open('data/messages.txt', 'r', encoding='utf-8') as f:
    messages = [l.strip() for l in f if l.strip()]

# Pattern for complaints / followups
complaint_patterns = [
    r'still not fixed',
    r'second time i ask',
    r'did anyone see my message',
    r'todav[ií]a no est[aá]',
    r'frustrated',
    r'already told you'
]

print("--- COMPLAINT / FOLLOW-UP MESSAGES ---")
complaints = []
for idx, m in enumerate(messages):
    for cp in complaint_patterns:
        if re.search(cp, m, re.IGNORECASE):
            complaints.append((idx, m))
            break

print(f"Total follow-ups / complaints found: {len(complaints)}")
for idx, c in complaints:
    print(f"\nMessage #{idx}: {c}")
    # find previous messages from same sender or mentioning same title
    # let's look at preceding messages
    print("  Preceding related messages:")
    for prev_idx in range(max(0, idx-15), idx):
        prev_m = messages[prev_idx]
        # check if same sender or shares words
        print(f"    [{prev_idx}] {prev_m}")

