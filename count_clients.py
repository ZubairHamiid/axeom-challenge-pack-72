import pandas as pd
import json

# Let's inspect all business names across all files
bookings = pd.read_csv('data/bookings.csv')
invoices = pd.read_csv('data/invoices.csv')
leads = pd.read_csv('data/leads.csv')
payments = pd.read_csv('data/payments.csv')
pb = pd.read_csv('data/production_board.csv')

# Let's list all unique entities
# Each entity has a core service relationship
print("--- ALL CLIENTS AND THEIR DATA ---")

