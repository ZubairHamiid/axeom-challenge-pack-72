# Axeom Challenge — Daily Work Log (`daily_log.md`)
**Candidate:** Zubair Hamid 
**Pack ID:** 72  

---

## Day 1 (2026-11-03)
- **10:00 to 13:30. What I did:**
  - Unpacked the dataset and read all instructions in `Axeom Challenge.pdf` and `Axeom Challenge - What to send.pdf`.
  - Audited the file structures of `bookings.csv`, `invoices.csv`, `leads.csv`, `payments.csv`, `production_board.csv`, `team.csv`, `costs.csv`, and `messages.txt`.
  - Built an entity-resolution script in Python to cluster client names, detect legal suffix variations, and map emails/phones.
- **What I changed my mind about, and why:**
  - Initially, I assumed Brightline Marketing was a standard agency client that booked video shoots for itself. Looking closely at the bookings and invoices, I realized that Greenway Pediatrics and Summit Chiropractic were the clinical clients being filmed, and Brightline was strictly an agency paying on their behalf. I moved Brightline to `payers_who_are_not_clients`.
- **What went wrong, and how I fixed it:**
  - The script initially counted 34 unique email addresses as 34 clients. I caught that `tasha.green.mail@gmail.com` belonged to Tasha Green (Hustle & Heart), `sarah@khandental.con` was a typo in `.com`, and `frisco@bloommedspa.com` belonged to Priya Shah (Bloom Med Spa). I built an alias dictionary to merge them into the canonical 29 clients.
- **Where the AI was wrong, and how I caught it:**
  - The AI initially flagged `INV-1132` (Mike's Roofing, $900) as 13 days overdue because the status column in `invoices.csv` said `unpaid`. I checked `payments.csv` and found payment `P5137` made on 2026-10-06 specifically referencing `INV-1132`. The AI failed to check same-day bank deposits; I corrected the script to cross-reference payment references before classifying an invoice as overdue.

---

## Day 2 (2026-11-04)
- **10:00 to 14:00. What I did:**
  - Conducted forensic financial reconciliation: checked for never-billed completed bookings, unapplied credits, and tool discrepancy errors.
  - Parsed all 204 lines in `messages.txt` and correlated client complaints ("still not fixed", "second time I ask") with production board video records.
  - Researched Jev (docs.typesafe.ai) and designed a low-latency System One classification architecture for intake message routing.
- **What I changed my mind about, and why:**
  - I initially thought lost requests were evenly distributed across the entire timeline. When I plotted complaints by month, I realized that from April to July complaints averaged only 1–3 per month, but exploded to 10 in August and 12 in September. I changed the escalation start date from Q2 to `2026-08`.
- **What went wrong, and how I fixed it:**
  - When calculating `never_billed`, I initially missed that Apex Physical Therapy's monthly retainers cover their retainer shoots. The booking for B138 on 2026-09-08 had a price of $0. By checking the invoice sequence, I realized September retainer was completely missing from `invoices.csv`. I added Apex PT September retainer ($2,500) to `never_billed`.
- **Where the AI was wrong, and how I caught it:**
  - The AI assumed that Tony Russo had not paid anything for invoice `INV-1128` ($900) because `invoices.csv` listed it as `partial` without showing the paid amount. I filtered `payments.csv` by Tony Russo's name and found payment `P5121` on 2026-09-14 for $450 with reference "half now half later". The AI had ignored payments with missing email addresses; I fixed the script to match by payer name.

---

## Day 3 (2026-11-05)
- **09:30 to 13:45. What I did:**
  - Built the interactive, mobile-responsive web application (`index.html`) featuring the 10-second Monday Action Center, Connected Client 360° views, Financial Audit dashboard, and Jev AI simulator.
  - Implemented the client-side "Add New Files" drag-and-drop feature powered by PapaParse to re-index arbitrary CSV/TXT uploads dynamically.
  - Completed all final verification checks across `answers.json`, `writeup.md`, `assumptions.md`, `ai_log.md`, and prepared the video presentation script.
- **What I changed my mind about, and why:**
  - In designing the web app, I initially drafted a complex dashboard with multiple charts and graphs. Realizing that this violated the "10-second test" rule for an owner opening their phone on Monday morning, I stripped away non-essential analytics and created a prominent 3-card priority action center right at the top.
- **What went wrong, and how I fixed it:**
  - The browser's drag-and-drop handler initially crashed when reading non-CSV text files like `messages.txt`. I added a custom text reader branch in JavaScript so that dropping both CSV files and `messages.txt` simultaneously updates the in-memory state smoothly.
- **Where the AI was wrong, and how I caught it:**
  - The AI suggested sending automated SMS and email reminders to overdue clients on a cron schedule. I caught that this directly violated the core challenge prompt: *"Suggest, never act alone... Nothing gets sent automatically."* I rewrote the interaction flow to require explicit modal confirmation for every suggested action.

