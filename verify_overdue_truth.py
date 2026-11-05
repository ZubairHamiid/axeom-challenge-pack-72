import pandas as pd

invoices = pd.read_csv('data/invoices.csv')
payments = pd.read_csv('data/payments.csv')

TODAY = pd.to_datetime('2026-10-06')
invoices['due_dt'] = pd.to_datetime(invoices['due'])

# Truly unpaid & past due as of 2026-10-06:
# 1. INV-1105: Lonestar Realty (Greg Whitfield), $1500, due 2026-08-28. Days late: 39 days. (No payment ever made!)
# 2. INV-1114: Tasha Green, $300, due 2026-09-08. Days late: 28 days. (4th August invoice, after $900 covered first 3!)
# 3. INV-1121: Hustle & Heart, $300, due 2026-09-15. Days late: 21 days.
# 4. INV-1123: Angela Price / TLC Homecare, $1500, due 2026-09-15. Days late: 21 days. (No payment ever made!)
# 5. INV-1125: Patel Insurance Group (Raj Patel), $2500, due 2026-09-15. Days late: 21 days. (Unpaid September retainer!)
# 6. INV-1128: Prime Roofing (Tony Russo), $450 (or $900 in tool, but truth is $450), due 2026-09-19. Days late: 17 days.
# 7. INV-1129: Brightline Marketing (Kelsey Moore), $900, due 2026-09-21. Days late: 15 days. (Unpaid Reels Pack!)

print("--- OVERDUE INVOICES ANALYSIS ---")
# Let's verify whether Brightline paid INV-1129:
print("Brightline payments:")
print(payments[payments['payer'].str.contains('Brightline', na=False)][['payment_id', 'date', 'amount', 'reference']])
print("Brightline invoices:")
print(invoices[invoices['email'] == 'kelsey@brightlinemktg.com'][['invoice_no', 'issued', 'due', 'amount', 'status']])

