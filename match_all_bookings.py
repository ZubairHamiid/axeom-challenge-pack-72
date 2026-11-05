import pandas as pd
import re
from datetime import datetime

bookings = pd.read_csv('data/bookings.csv')
invoices = pd.read_csv('data/invoices.csv')

def clean_price(val):
    if pd.isna(val):
        return 0.0
    s = str(val).replace('$', '').replace(',', '').strip()
    try:
        return float(s)
    except:
        return 0.0

bookings['price_clean'] = bookings['price'].apply(clean_price)
bookings['b_dt'] = pd.to_datetime(bookings['date'], dayfirst=False, errors='coerce')
invoices['inv_dt'] = pd.to_datetime(invoices['issued'], errors='coerce')

# Map emails
email_aliases = {
    'tasha.green.mail@gmail.com': 'tasha@hustleandheart.fm',
    'sarah@khandental.con': 'sarah@khandental.com',
    'frisco@bloommedspa.com': 'priya@bloommedspa.com',
    'acho@greenwaypeds.com': 'kelsey@brightlinemktg.com',
    'drhale@summitchiro.com': 'kelsey@brightlinemktg.com'
}

bookings['clean_email'] = bookings['email'].str.lower().str.strip().replace(email_aliases)
invoices['clean_email'] = invoices['email'].str.lower().str.strip().replace(email_aliases)

# Filter out void invoices
valid_invoices = invoices[invoices['status'] != 'void'].copy()
completed_bookings = bookings[bookings['status'] == 'completed'].copy()

# Step 1: Match by explicit Bxxx ID in memo
valid_invoices['matched_bid'] = valid_invoices['memo'].str.extract(r'(B\d{3})')

# Mark which bookings are matched
completed_bookings['matched_inv'] = None
for idx, inv in valid_invoices.dropna(subset=['matched_bid']).iterrows():
    bid = inv['matched_bid']
    b_matches = completed_bookings[completed_bookings['booking_id'] == bid]
    if len(b_matches) > 0:
        completed_bookings.loc[b_matches.index, 'matched_inv'] = inv['invoice_no']

unmatched_b = completed_bookings[completed_bookings['matched_inv'].isna()].copy()
unmatched_inv = valid_invoices[~valid_invoices['invoice_no'].isin(completed_bookings['matched_inv'].dropna())].copy()

print(f"Remaining unmatched completed bookings: {len(unmatched_b)}")
print(f"Remaining unmatched valid invoices: {len(unmatched_inv)}")

# Retainer invoices cover retainer shoots by month!
# Let's match retainer shoots to retainer invoices by client and month
for idx, b in unmatched_b[unmatched_b['service'].str.contains('Retainer', na=False)].iterrows():
    b_month = b['b_dt'].strftime('%Y-%m')
    inv_match = unmatched_inv[
        (unmatched_inv['clean_email'] == b['clean_email']) & 
        (unmatched_inv['inv_dt'].dt.strftime('%Y-%m') == b_month) &
        (unmatched_inv['memo'].str.contains('retainer', na=False, case=False))
    ]
    if len(inv_match) > 0:
        completed_bookings.loc[idx, 'matched_inv'] = inv_match.iloc[0]['invoice_no']

# Refresh unmatched
unmatched_b = completed_bookings[completed_bookings['matched_inv'].isna()].copy()
unmatched_inv = valid_invoices[~valid_invoices['invoice_no'].isin(completed_bookings['matched_inv'].dropna())].copy()

print(f"After retainer matching: unmatched bookings: {len(unmatched_b)}, unmatched invoices: {len(unmatched_inv)}")

# For remaining, match by email, service/amount, and closest date
for email, grp in unmatched_b.groupby('clean_email'):
    inv_grp = unmatched_inv[unmatched_inv['clean_email'] == email]
    print(f"\n--- CLIENT {email} ---")
    print("Unmatched Bookings:")
    print(grp[['booking_id', 'date', 'service', 'price_clean']])
    print("Unmatched Invoices:")
    print(inv_grp[['invoice_no', 'issued', 'amount', 'memo']])

