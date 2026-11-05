import pandas as pd
import numpy as np
import re
from datetime import datetime

bookings = pd.read_csv('data/bookings.csv')
costs = pd.read_csv('data/costs.csv')
invoices = pd.read_csv('data/invoices.csv')
leads = pd.read_csv('data/leads.csv')
payments = pd.read_csv('data/payments.csv')
pb = pd.read_csv('data/production_board.csv')
team = pd.read_csv('data/team.csv')

with open('data/messages.txt', 'r', encoding='utf-8') as f:
    messages_raw = f.read()

print("="*60)
print("--- ALL UNIQUE EMAILS IN BOOKINGS & INVOICES ---")
b_emails = set(bookings['email'].dropna().str.lower().str.strip())
i_emails = set(invoices['email'].dropna().str.lower().str.strip())
p_emails = set(payments['payer_email'].dropna().str.lower().str.strip())
l_won_emails = set(leads[leads['status'] == 'Won']['email'].dropna().str.lower().str.strip())

all_client_emails = b_emails.union(i_emails)
print(f"Total unique client emails across bookings & invoices: {len(all_client_emails)}")
for e in sorted(all_client_emails):
    b_names = set(bookings[bookings['email'].str.lower().str.strip() == e]['client_name'])
    i_names = set(invoices[invoices['email'].str.lower().str.strip() == e]['bill_to'])
    print(f"Email: {e} | Bookings names: {b_names} | Invoices names: {i_names}")

print("\n--- EMAILS IN PAYMENTS BUT NOT IN BOOKINGS/INVOICES ---")
print(p_emails - all_client_emails)

print("\n--- PAYMENTS WITHOUT MATCHING INVOICE REFERENCE ---")
unmatched_p = payments[payments['reference'].isna() | ~payments['reference'].isin(invoices['invoice_no'])]
print(f"Total payments without valid invoice ref: {len(unmatched_p)}")
print(unmatched_p[['payment_id', 'date', 'payer', 'payer_email', 'amount', 'reference']])


