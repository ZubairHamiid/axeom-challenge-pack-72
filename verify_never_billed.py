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
completed_b = bookings[bookings['status'] == 'completed'].copy()

# List of all unbilled candidates:
candidates = ['B147', 'B141', 'B132', 'B143', 'B126', 'B138']

print("Details of unbilled bookings:")
for b in candidates:
    row = bookings[bookings['booking_id'] == b].iloc[0]
    print(f"{b}: Client={row['client_name']}, Email={row['email']}, Date={row['date']}, Service={row['service']}, Price={row['price_clean']}")

