import pandas as pd
import numpy as np

bookings = pd.read_csv('data/bookings.csv')
invoices = pd.read_csv('data/invoices.csv')
payments = pd.read_csv('data/payments.csv')

# Normalize emails
payments['email'] = payments['payer_email'].str.lower().str.strip()
invoices['email'] = invoices['email'].str.lower().str.strip()
bookings['email'] = bookings['email'].str.lower().str.strip()

# Aggregate by email
inv_summary = invoices.groupby('email').agg(
    total_invoiced=('amount', 'sum'),
    invoices_count=('invoice_no', 'count'),
    invoiced_paid_status=('amount', lambda s: s[invoices.loc[s.index, 'status'] == 'paid'].sum()),
    invoiced_unpaid_status=('amount', lambda s: s[invoices.loc[s.index, 'status'] == 'unpaid'].sum()),
    invoiced_partial_status=('amount', lambda s: s[invoices.loc[s.index, 'status'] == 'partial'].sum()),
    invoiced_void_status=('amount', lambda s: s[invoices.loc[s.index, 'status'] == 'void'].sum()),
).reset_index()

pay_summary = payments.groupby('email').agg(
    total_paid=('amount', 'sum'),
    payments_count=('payment_id', 'count')
).reset_index()

ledger = pd.merge(inv_summary, pay_summary, on='email', how='outer').fillna(0)
ledger['diff_paid_minus_invoiced'] = ledger['total_paid'] - ledger['total_invoiced']
ledger['diff_paid_minus_valid_invoiced'] = ledger['total_paid'] - (ledger['total_invoiced'] - ledger['invoiced_void_status'])

print("--- CLIENT LEDGER (ALL CLIENTS) ---")
print(ledger.sort_values(by='diff_paid_minus_invoiced', ascending=False).to_string())

