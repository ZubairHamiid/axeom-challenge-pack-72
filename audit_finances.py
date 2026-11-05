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

TODAY = pd.to_datetime('2026-10-06')

print("="*60)
print("SECTION 2: INVOICES & PAYMENTS RECONCILIATION")
print("="*60)

# Check invoice dates, due dates, statuses
invoices['issued_dt'] = pd.to_datetime(invoices['issued'])
invoices['due_dt'] = pd.to_datetime(invoices['due'])
invoices['amount'] = invoices['amount'].astype(float)

# Compare total invoice amount vs total payments amount
print(f"Total invoices count: {len(invoices)}, Sum: ${invoices['amount'].sum():.2f}")
print(f"Invoices status breakdown:\n{invoices['status'].value_counts()}")
print(f"Sum by status:\n{invoices.groupby('status')['amount'].sum()}")

print(f"\nTotal payments count: {len(payments)}, Sum: ${payments['amount'].sum():.2f}")

# Check which invoices are marked unpaid
unpaid_inv = invoices[invoices['status'] == 'unpaid'].copy()
unpaid_inv['days_late'] = (TODAY - unpaid_inv['due_dt']).dt.days
print(f"\nInvoices marked 'unpaid' in invoices.csv: {len(unpaid_inv)}")
print(unpaid_inv[['invoice_no', 'bill_to', 'email', 'amount', 'due', 'days_late', 'memo']])

# BUT WAIT: Are some of these 'unpaid' invoices actually paid in payments.csv?
# Let's check payments with reference matching unpaid invoices!
print("\n--- Payments matching 'unpaid' invoices directly by reference ---")
print(payments[payments['reference'].isin(unpaid_inv['invoice_no'])])

# And what about payments matching by email / payer / amount?
print("\n--- Payments around same date / amount for unpaid invoices ---")
for idx, r in unpaid_inv.iterrows():
    p_match = payments[(payments['payer_email'] == r['email']) | (payments['amount'] == r['amount'])]
    # filter around invoice issued / due
    print(f"Unpaid {r['invoice_no']} ({r['bill_to']}, {r['email']}, ${r['amount']}, due {r['due']}):")
    refs = payments[payments['reference'] == r['invoice_no']]
    if len(refs) > 0:
        print("  DIRECT REF MATCH:", refs[['payment_id', 'date', 'payer', 'amount', 'reference']].to_dict('records'))
    else:
        # check by email
        by_email = payments[payments['payer_email'] == r['email']]
        print(f"  Total payments by this email: {len(by_email)}, sum: ${by_email['amount'].sum()}")
        # total invoiced for this email
        by_inv = invoices[invoices['email'] == r['email']]
        print(f"  Total invoiced for this email: {len(by_inv)}, sum: ${by_inv['amount'].sum()} (paid status: ${by_inv[by_inv['status']=='paid']['amount'].sum()})")

