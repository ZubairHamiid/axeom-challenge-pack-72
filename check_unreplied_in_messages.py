import pandas as pd

leads = pd.read_csv('data/leads.csv')
with open('data/messages.txt', 'r', encoding='utf-8') as f:
    msg_text = f.read()

no_reply_leads = leads[leads['first_reply'].isna() | (leads['first_reply'] == '')].copy()

print("--- CHECKING NO-REPLY LEADS IN MESSAGES.TXT ---")
for idx, r in no_reply_leads.iterrows():
    lid = r['lead_id']
    name = r['name']
    email = str(r['email'])
    phone = str(r['phone']) if pd.notna(r['phone']) else "NOPHONE"
    
    in_msg = (email in msg_text) or (phone in msg_text) or (name in msg_text)
    print(f"{lid} | {name} | {email} | {phone} | in_messages: {in_msg} | status: {r['status']}")

