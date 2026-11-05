import pandas as pd
import numpy as np
import re
from datetime import datetime

# Load data
bookings = pd.read_csv('data/bookings.csv')
costs = pd.read_csv('data/costs.csv')
invoices = pd.read_csv('data/invoices.csv')
leads = pd.read_csv('data/leads.csv')
payments = pd.read_csv('data/payments.csv')
pb = pd.read_csv('data/production_board.csv')
team = pd.read_csv('data/team.csv')

with open('data/messages.txt', 'r', encoding='utf-8') as f:
    messages_raw = f.read()

print("="*60)
print("1. CLIENT RESOLUTION AUDIT")
print("="*60)

# Check all leads
# Which leads became clients (Won)?
won_leads = leads[leads['status'] == 'Won']
print(f"Total won leads: {len(won_leads)}")
for idx, r in won_leads.iterrows():
    print(f"Won Lead: {r['lead_id']} | {r['name']} | {r['business']} | {r['email']} | {r['phone']}")

# Check all bookings clients
print("\n--- Bookings Clients ---")
print(bookings.groupby(['client_name', 'email']).size())

# Check Invoices Bill_to
print("\n--- Invoices Bill_to ---")
print(invoices.groupby(['bill_to', 'email']).size())

# Check Production Board Clients
print("\n--- Production Board Clients ---")
print(pb['client'].value_counts())

