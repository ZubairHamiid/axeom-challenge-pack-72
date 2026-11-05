import pandas as pd

bookings = pd.read_csv('data/bookings.csv')
invoices = pd.read_csv('data/invoices.csv')

# Let's check Marcus Webb / Ironclad Gym
print("--- IRONCLAD GYM ---")
print("Bookings:")
print(bookings[bookings['email'] == 'marcus@ironcladgym.com'][['booking_id', 'date', 'service', 'price', 'status']])
print("Invoices:")
print(invoices[invoices['email'] == 'marcus@ironcladgym.com'][['invoice_no', 'issued', 'amount', 'status', 'memo']])

# Let's check Tasha Green / Hustle and Heart
print("\n--- TASHA GREEN / H&H ---")
print("Bookings in Aug/Sep/Oct:")
tasha_b = bookings[bookings['email'].str.contains('tasha', na=False)].copy()
print(tasha_b[['booking_id', 'date', 'service', 'price', 'status']].to_string())
print("Invoices in Aug/Sep/Oct:")
tasha_inv = invoices[invoices['email'].str.contains('tasha', na=False)].copy()
print(tasha_inv[['invoice_no', 'issued', 'amount', 'status', 'memo']].to_string())

