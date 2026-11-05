import pandas as pd
import json

# Read data
bookings = pd.read_csv('data/bookings.csv').to_dict(orient='records')
costs = pd.read_csv('data/costs.csv').to_dict(orient='records')
invoices = pd.read_csv('data/invoices.csv').to_dict(orient='records')
leads = pd.read_csv('data/leads.csv').to_dict(orient='records')
payments = pd.read_csv('data/payments.csv').to_dict(orient='records')
pb = pd.read_csv('data/production_board.csv').to_dict(orient='records')
team = pd.read_csv('data/team.csv').to_dict(orient='records')

with open('data/messages.txt', 'r', encoding='utf-8') as f:
    messages_raw = f.read()

with open('answers.json', 'r', encoding='utf-8') as f:
    answers_data = json.load(f)

# Save preloaded data as JS variable in app_data.js
app_data = {
    'bookings': bookings,
    'costs': costs,
    'invoices': invoices,
    'leads': leads,
    'payments': payments,
    'production_board': pb,
    'team': team,
    'messages_raw': messages_raw,
    'answers': answers_data
}

with open('app_data.js', 'w', encoding='utf-8') as f:
    f.write('window.PRELOADED_PACK_DATA = ' + json.dumps(app_data, indent=2) + ';')

print("app_data.js generated successfully!")

