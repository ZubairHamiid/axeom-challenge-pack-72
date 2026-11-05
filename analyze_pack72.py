import pandas as pd
import json
import re
from datetime import datetime

# Load all files
bookings = pd.read_csv('data/bookings.csv')
costs = pd.read_csv('data/costs.csv')
invoices = pd.read_csv('data/invoices.csv')
leads = pd.read_csv('data/leads.csv')
payments = pd.read_csv('data/payments.csv')
pb = pd.read_csv('data/production_board.csv')
team = pd.read_csv('data/team.csv')

with open('data/messages.txt', 'r', encoding='utf-8') as f:
    messages_raw = f.read()

print("Files loaded successfully.")

