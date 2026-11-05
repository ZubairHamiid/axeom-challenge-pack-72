import pandas as pd
import numpy as np

leads = pd.read_csv('data/leads.csv')
bookings = pd.read_csv('data/bookings.csv')
invoices = pd.read_csv('data/invoices.csv')
payments = pd.read_csv('data/payments.csv')
pb = pd.read_csv('data/production_board.csv')
team = pd.read_csv('data/team.csv')

# Sources in leads:
print("--- LEADS SOURCES & CONVERSION ---")
print(leads.groupby('source')['status'].value_counts().unstack().fillna(0))

# Let's map won leads to client emails
won_leads = leads[leads['status'] == 'Won'].copy()

# Let's see how much revenue and profit each client generated
# Studio time cost: $40/hr
# Content Day: 6 hrs studio ($240)
# Reels Pack: 3 hrs studio ($120)
# Retainer Shoot: 4 hrs studio ($160)
# Podcast Studio 2hr: 2 hrs studio ($80)
# Podcast Studio 4hr: 4 hrs studio ($160)

# Editor hourly pay:
# Ali: $35/hr, Rita: $30/hr, Sam: $22/hr, Dev: $40/hr
editor_rates = {'Ali': 35.0, 'Rita': 30.0, 'Sam': 22.0, 'Dev': 40.0}

# Let's calculate revenue per client
client_rev = {}
for email, grp in invoices[invoices['status'] != 'void'].groupby('email'):
    client_rev[email] = grp['amount'].sum()

print("\n--- CLIENT REVENUE BY LEAD SOURCE ---")
source_stats = {}
for _, l in won_leads.iterrows():
    src = l['source']
    email = l['email']
    rev = client_rev.get(email, 0.0)
    if src not in source_stats:
        source_stats[src] = {'won_count': 0, 'total_revenue': 0.0, 'clients': []}
    source_stats[src]['won_count'] += 1
    source_stats[src]['total_revenue'] += rev
    source_stats[src]['clients'].append((l['name'], rev))

for src, stat in sorted(source_stats.items(), key=lambda x: x[1]['total_revenue'], reverse=True):
    print(f"\nSource: {src}")
    print(f"  Won Leads: {stat['won_count']}")
    print(f"  Total Invoiced Revenue: ${stat['total_revenue']:,.2f}")
    print(f"  Avg Rev per Won Lead: ${stat['total_revenue']/stat['won_count']:,.2f}")
    for c, r in stat['clients']:
        print(f"    - {c}: ${r:,.2f}")

