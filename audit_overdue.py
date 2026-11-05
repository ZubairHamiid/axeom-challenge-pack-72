import pandas as pd

invoices = pd.read_csv('data/invoices.csv')
payments = pd.read_csv('data/payments.csv')

TODAY = pd.to_datetime('2026-10-06')
invoices['due_dt'] = pd.to_datetime(invoices['due'])
invoices['issued_dt'] = pd.to_datetime(invoices['issued'])

# Find all invoices with due_dt < TODAY and status != 'paid' and status != 'void'
candidates = invoices[(invoices['due_dt'] < TODAY) & (invoices['status'].isin(['unpaid', 'partial']))].copy()
candidates['days_late'] = (TODAY - candidates['due_dt']).dt.days

print("--- OVERDUE CANDIDATES FROM INVOICES.CSV ---")
print(candidates[['invoice_no', 'bill_to', 'email', 'issued', 'due', 'amount', 'status', 'days_late', 'memo']].to_string())

# For each candidate, check actual payments
print("\n--- ACTUAL PAYMENT AUDIT FOR EACH CANDIDATE ---")
for idx, r in candidates.iterrows():
    inv_no = r['invoice_no']
    # Check direct ref
    p_ref = payments[payments['reference'] == inv_no]
    # Check unreferenced payments by same payer/email
    p_email = payments[(payments['payer_email'] == r['email']) & (payments['reference'].isna())]
    print(f"\n{inv_no} | {r['bill_to']} | Due: {r['due']} | Amount: ${r['amount']} | Tool status: {r['status']} | Days late: {r['days_late']}")
    if len(p_ref) > 0:
        print("  Direct Ref Payments:", p_ref[['payment_id', 'date', 'amount', 'method', 'reference']].to_dict('records'))
    if len(p_email) > 0:
        print("  Unreferenced Payments by email:", p_email[['payment_id', 'date', 'amount', 'method', 'reference']].to_dict('records'))

