import pandas as pd

bookings = pd.read_csv('data/bookings.csv')
invoices = pd.read_csv('data/invoices.csv')

# Retainer clients have "Retainer Shoot" in bookings or "Monthly retainer" in invoices
retainer_inv = invoices[invoices['memo'].str.contains('retainer', na=False, case=False)]
print("--- RETAINER INVOICES ---")
print(retainer_inv[['invoice_no', 'bill_to', 'email', 'issued', 'amount', 'status', 'memo']])

print("\n--- RETAINER BOOKINGS ---")
retainer_b = bookings[bookings['service'].str.contains('retainer', na=False, case=False)]
print(retainer_b[['booking_id', 'date', 'client_name', 'email', 'service']])

print("\n--- CHECK MONTHLY RETAINERS PER CLIENT ---")
for email, grp in retainer_inv.groupby('email'):
    print(f"\nClient {email}:")
    for _, r in grp.iterrows():
        print(f"  {r['issued']} | {r['amount']} | {r['status']} | {r['memo']}")

