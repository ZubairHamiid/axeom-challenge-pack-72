import pandas as pd
import json
import re

# Check client count and all details
bookings = pd.read_csv('data/bookings.csv')
invoices = pd.read_csv('data/invoices.csv')
leads = pd.read_csv('data/leads.csv')
payments = pd.read_csv('data/payments.csv')
pb = pd.read_csv('data/production_board.csv')

with open('data/messages.txt', 'r', encoding='utf-8') as f:
    messages = [l.strip() for l in f if l.strip()]

# Let's map every phone number and email in messages
phone_to_name = {}
email_to_name = {}

for l in messages:
    p_match = re.search(r'\+1 (\d{3}-\d{3}-\d{4}) \(([^)]+)\)', l)
    if p_match:
        phone, name = p_match.groups()
        phone_to_name[phone] = name
    e_match = re.search(r'from ([\w\.-]+@[\w\.-]+\.\w+)', l)
    if e_match:
        email = e_match.group(1).lower()
        # see if name in parentheses
        n_match = re.search(r'from [\w\.-]+@[\w\.-]+\.\w+ \(([^)]+)\)', l)
        if n_match:
            email_to_name[email] = n_match.group(1)

print("Phone to sender mapping from messages:")
for p, n in sorted(phone_to_name.items()):
    print(f"  {p}: {n}")

print("\nEmail to sender mapping from messages:")
for e, n in sorted(email_to_name.items()):
    print(f"  {e}: {n}")
