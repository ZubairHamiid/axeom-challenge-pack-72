# Axeom Challenge — AI Usage & Prompt Log (`ai_log.md`)
**Candidate:** Zubair Hamid  
**Pack ID:** 72  

---

## 1. Which AI Tools Were Used, and for What

1. **Gemini 3.8 Flash (High) / Antigravity Assistant:**
   - Used for rapid forensic exploration across disconnected tabular data (CSV) and text logs (`messages.txt`).
   - Assisting with writing complex data reconciliation scripts in Python (`pandas`).
   - Generating the responsive HTML5/Tailwind client-side application architecture.
   - Performing sanity checks on accounting logic (FIFO allocation of unreferenced Zelle payments).

---

## 2. Key Prompts Used & Interaction Log

### Prompt 1: Entity Resolution & Client Clustering
```text
"Here are the headers and sample rows of bookings.csv, invoices.csv, payments.csv, and leads.csv.
The data has typos (e.g. .con instead of .com) and inconsistent company names (e.g. 'Dr Khan', 'Khan Dental', 'Sarah Khan DDS').
Write a Python script to cluster records by canonical client identity, map all aliases, emails, and phone numbers, and separate any third-party payers who are paying on behalf of other clients."
```
- **How I Verified:** Checked every grouped cluster manually against the raw CSV rows. Confirmed that Brightline Marketing was an agency paying for Greenway Pediatrics and Summit Chiropractic.

### Prompt 2: Bank Payments vs Billing Tool Reconciliation
```text
"Look at invoices.csv and payments.csv. Find every invoice marked 'unpaid' or 'partial' where due date is before October 6, 2026.
Then check whether payments.csv has matching payments—either by reference number, exact dollar amount, or payer identity.
Identify where the billing tool is showing incorrect statuses."
```
- **How I Verified:** Discovered that `INV-1132` ($900) was marked unpaid in the billing tool despite payment `P5137` having arrived on 2026-10-06 referencing `INV-1132`. Also verified that `INV-1120` had been paid on 2026-08-31 via card (P5108), but left unlinked because the reference field was blank.

### Prompt 3: Lost Video Requests & Complaint Correlation
```text
"Parse messages.txt and find all follow-up messages or complaints matching phrases like 'still not fixed', 'second time I ask', 'did anyone see my message', 'todavía no está'.
Trace each complaint back to its original request, identify the video_id from production_board.csv, and determine why the request fell through the cracks."
```
- **How I Verified:** Read the original voice note transcripts and message logs. Verified that dropped voice notes (audio not logged to production board notes) and Spanish messages were the primary reasons for unaddressed client requests.

---

## 3. Where the AI Was Wrong, and How I Caught It

### Incident 1: Overdue Invoice False Positive (`INV-1132`)
- **What the AI Said:**  
  The AI initially generated a table showing `INV-1132` (Mike's Roofing, $900, due 2026-09-23) as 13 days overdue, calculating total overdue at $8,350 instead of $7,450.
- **Why It Was Wrong:**  
  The AI relied solely on the `status` column of `invoices.csv` without cross-verifying same-day bank deposits in `payments.csv`.
- **How I Caught It:**  
  I filtered `payments.csv` for the current simulation date (`2026-10-06`) and discovered payment `P5137` from `MIKE DELGADO` for exactly $900 with reference `INV-1132`. Because the payment cleared on October 6, the invoice was settled and was no longer overdue. I corrected the overdue total to $7,450.

### Incident 2: Missing Unbilled Retainer Revenue (Apex Physical Therapy)
- **What the AI Said:**  
  The AI ran an inner join between `bookings.csv` and `invoices.csv` on price and booking ID, concluding that only 5 one-off shoots were never billed (totaling $3,550).
- **Why It Was Wrong:**  
  Retainer clients have $0 booking fees in `bookings.csv` because their shoots are included under monthly subscription retainers. Because booking B138 was listed as $0, the AI's script ignored it.
- **How I Caught It:**  
  I analyzed the monthly invoice sequence for Apex Physical Therapy and saw invoices for June ($2,500), July ($2,500), August ($2,000), and October ($2,500), but noticed September was missing entirely even though retainer shoot B138 took place on 2026-09-08. I added the unbilled September retainer ($2,500) to bring the true unbilled total to $6,050.

### Incident 3: Automated Actions vs Suggestion Protocol
- **What the AI Said:**  
  The AI proposed adding an automated background job to send email reminders to all overdue clients at 09:00 AM on Monday morning.
- **Why It Was Wrong:**  
  This violated the explicit challenge constraint: *"Suggest, never act alone. For example: 'This invoice is 21 days late. Send a reminder?' The owner says yes or no. Nothing gets sent automatically."*
- **How I Caught It:**  
  I flagged the prompt specification, rejected the automated cron script, and engineered an interactive confirmation modal system where suggestions are presented to the owner with explicit [Yes, Confirm Action] and [Cancel] controls.

