import pandas as pd
import re

bookings = pd.read_csv('data/bookings.csv')
invoices = pd.read_csv('data/invoices.csv')
payments = pd.read_csv('data/payments.csv')
pb = pd.read_csv('data/production_board.csv')

# Clean prices in bookings
def clean_price(val):
    if pd.isna(val):
        return 0.0
    s = str(val).replace('$', '').replace(',', '').strip()
    try:
        return float(s)
    except:
        return 0.0

bookings['price_clean'] = bookings['price'].apply(clean_price)

# Check all completed bookings
completed_b = bookings[bookings['status'] == 'completed'].copy()
print(f"Total completed bookings: {len(completed_b)}")

# Invoices memos often have booking id: B001, B002, etc.
# Also match by client email and date/service
inv_memos = invoices['memo'].dropna().tolist()

matched_bookings = set()
for memo in inv_memos:
    b_ids = re.findall(r'B\d{3}', memo)
    for b in b_ids:
        matched_bookings.add(b)

print(f"Bookings explicitly referenced by ID in invoice memos: {len(matched_bookings)}")

unmatched_b = completed_b[~completed_b['booking_id'].isin(matched_bookings)].copy()
print(f"Completed bookings NOT referenced by ID in memo: {len(unmatched_b)}")
print(unmatched_b[['booking_id', 'date', 'client_name', 'email', 'service', 'price_clean']])

