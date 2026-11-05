import pandas as pd
import re

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

# Find all booking IDs mentioned in invoice memos
all_memos = invoices['memo'].dropna().tolist()
memos_str = " ".join(all_memos)
mentioned_b_ids = set(re.findall(r'B\d{3}', memos_str))

# For invoices without explicit booking ID, look at date, email, amount, service
# Let's see which invoices don't have a booking ID in memo:
non_id_inv = invoices[~invoices['memo'].str.contains(r'B\d{3}', na=False)].copy()
print(f"Invoices without explicit Bxxx in memo: {len(non_id_inv)}")
print(non_id_inv[['invoice_no', 'bill_to', 'email', 'issued', 'amount', 'memo']].to_string())

# For each completed booking, let's see if it was billed:
# A booking is billed if:
# 1. Its ID is in an invoice memo
# 2. Or it's a retainer shoot covered by a monthly retainer invoice for that month
# 3. Or its date/service/client matches an invoice memo like "Podcast Studio 2hr 4/3"

