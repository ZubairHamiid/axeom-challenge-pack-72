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
bookings['b_date'] = pd.to_datetime(bookings['date'], format='%d/%m/%Y', errors='coerce')
if bookings['b_date'].isna().sum() > 0:
    # try mm/dd/yyyy
    bookings['b_date'] = pd.to_datetime(bookings['date'], errors='coerce')

invoices['inv_issued'] = pd.to_datetime(invoices['issued'])

print("--- RECONCILING EACH CLIENT'S BOOKINGS vs INVOICES ---")
# Group by normalized email
bookings['norm_email'] = bookings['email'].str.lower().str.strip()
invoices['norm_email'] = invoices['email'].str.lower().str.strip()

for email, b_group in bookings[bookings['status'] == 'completed'].groupby('norm_email'):
    i_group = invoices[invoices['norm_email'] == email]
    b_count = len(b_group)
    i_count = len(i_group[i_group['status'] != 'void'])
    b_sum = b_group['price_clean'].sum()
    i_sum = i_group[i_group['status'] != 'void']['amount'].sum()
    
    if b_count != i_count or b_sum != i_sum:
        print(f"\nDiscrepancy for {email}:")
        print(f"  Completed Bookings: {b_count} shoots, total ${b_sum}")
        print(f"  Valid Invoices:     {i_count} bills,  total ${i_sum}")
        print(f"  Difference: ${b_sum - i_sum}")
        print("  Bookings:")
        for _, b in b_group.iterrows():
            print(f"    {b['booking_id']} | {b['date']} | {b['service']} | ${b['price_clean']}")
        print("  Invoices:")
        for _, inv in i_group.iterrows():
            print(f"    {inv['invoice_no']} | {inv['issued']} | ${inv['amount']} | {inv['status']} | {inv['memo']}")

