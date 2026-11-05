import pandas as pd

bookings = pd.read_csv('data/bookings.csv')
invoices = pd.read_csv('data/invoices.csv')
leads = pd.read_csv('data/leads.csv')
pb = pd.read_csv('data/production_board.csv')
team = pd.read_csv('data/team.csv')

# Studio hours note:
# Content Day uses 6 hours, Reels Pack 3, Retainer Shoot 4, podcast sessions their booked hours
def get_studio_hours(service):
    if pd.isna(service):
        return 0
    s = str(service).lower()
    if 'content day' in s:
        return 6
    elif 'reels pack' in s:
        return 3
    elif 'retainer shoot' in s:
        return 4
    elif 'podcast studio 2hr' in s or '2hr' in s:
        return 2
    elif 'podcast studio 4hr' in s or '4hr' in s:
        return 4
    return 0

bookings['studio_hours'] = bookings['service'].apply(get_studio_hours)
bookings['studio_cost'] = bookings['studio_hours'] * 40.0

# Editor pay rates
editor_pay = {'Ali': 35.0, 'Rita': 30.0, 'Sam': 22.0, 'Dev': 40.0}
pb['editor_rate'] = pb['editor'].map(editor_pay).fillna(30.0)
pb['editor_cost'] = pb['editor_hours'] * pb['editor_rate']

print("--- TOTAL STUDIO COST ACROSS ALL COMPLETED BOOKINGS ---")
completed_b = bookings[bookings['status'] == 'completed']
print(f"Total studio cost: ${completed_b['studio_cost'].sum():,.2f}")

print("--- TOTAL EDITOR COST ON PRODUCTION BOARD ---")
print(f"Total editor cost: ${pb['editor_cost'].sum():,.2f}")

# Now aggregate per client
# Normalize emails
email_to_source = {}
for _, l in leads[leads['status'] == 'Won'].iterrows():
    email_to_source[l['email'].lower().strip()] = l['source']

# Also add aliases
email_to_source['tasha.green.mail@gmail.com'] = 'Instagram'
email_to_source['sarah@khandental.con'] = 'Referral'
email_to_source['frisco@bloommedspa.com'] = 'Instagram'
email_to_source['acho@greenwaypeds.com'] = 'Referral'
email_to_source['drhale@summitchiro.com'] = 'Referral'

# Map client on PB to email/source
# Let's see profit by channel
channel_finances = {}
for src in leads['source'].unique():
    channel_finances[src] = {'revenue': 0.0, 'studio_cost': 0.0, 'editor_cost': 0.0, 'gross_profit': 0.0}

# Revenue
for _, inv in invoices[invoices['status'] != 'void'].iterrows():
    e = str(inv['email']).lower().strip()
    src = email_to_source.get(e, 'Unknown')
    if src in channel_finances:
        channel_finances[src]['revenue'] += inv['amount']

# Studio cost
for _, b in completed_b.iterrows():
    e = str(b['email']).lower().strip()
    src = email_to_source.get(e, 'Unknown')
    if src in channel_finances:
        channel_finances[src]['studio_cost'] += b['studio_cost']

for src, data in channel_finances.items():
    data['gross_profit'] = data['revenue'] - data['studio_cost']
    print(f"\nChannel: {src}")
    print(f"  Revenue:     ${data['revenue']:,.2f}")
    print(f"  Studio Cost: ${data['studio_cost']:,.2f}")
    print(f"  Est Margin:  ${data['gross_profit']:,.2f} ({data['gross_profit']/data['revenue']*100:.1f}%)" if data['revenue'] > 0 else "  N/A")

