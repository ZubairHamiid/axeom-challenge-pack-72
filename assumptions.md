# Axeom Challenge — Questions & Assumptions Log (`assumptions.md`)
**Candidate:** Zubair Hamid 
**Pack ID:** 72  
**Evaluation Date:** October 6, 2026  

Because we were instructed not to ask questions during the 72-hour assessment, every ambiguous scenario was addressed with grounded, business-first assumptions. Below is the complete record of questions we would have asked the Axeom leadership team and the assumptions adopted instead.

---

### Question 1: Client vs. Agency Distinction (Brightline Marketing)
- **Question We Would Have Asked:**  
  *"Is Brightline Marketing LLC considered a single agency client, or are Greenway Pediatrics and Summit Chiropractic considered separate individual clients of Axeom?"*
- **What We Assumed Instead:**  
  We assumed that **Greenway Pediatrics** (`acho@greenwaypeds.com`) and **Summit Chiropractic** (`drhale@summitchiro.com`) are the actual end-clients receiving video production and podcast services, while **Brightline Marketing LLC** (`kelsey@brightlinemktg.com`) acts strictly as a third-party marketing agency payer. In `answers.json`, we categorized Greenway Pediatrics and Summit Chiropractic as distinct clients and listed Brightline Marketing LLC under `payers_who_are_not_clients`.

---

### Question 2: Retainer Shoot Billing for September (Apex Physical Therapy)
- **Question We Would Have Asked:**  
  *"Apex Physical Therapy completed a retainer shoot on 2026-09-08 (B138, $0 listed booking price), but received an invoice for October retainer on 2026-10-01 (INV-1149). Was September's $2,500 retainer waived or simply forgotten?"*
- **What We Assumed Instead:**  
  We assumed that **September retainer was never billed due to administrative oversight**. All other retainer months (June, July, August, October) were billed at $2,000–$2,500. Retainer shoots are delivered as part of the monthly subscription; because shoot B138 was executed and delivered in September, Axeom is legally and commercially entitled to bill the $2,500 retainer fee. We recorded this as $2,500 under `never_billed`.

---

### Question 3: Cancelled Booking B152 & Double Billing (Lone Star Realty)
- **Question We Would Have Asked:**  
  *"Dana Brooks cancelled shoot B152 on 2026-09-24 due to an emergency after paying $1,500. When shoot B165 was scheduled for October 7, an invoice (INV-1153) was issued and paid. Does Axeom have a cancellation/reschedule credit policy?"*
- **What We Assumed Instead:**  
  We assumed standard commercial content studio policy: an emergency cancellation with advance notice that is rescheduled should transfer the prepaid deposit to the new date. Since Axeom collected $1,500 for the cancelled shoot and another $1,500 for the rescheduled shoot, Axeom owes Lone Star Realty either a **$1,500 cash refund or an account credit** toward their next shoot. We recorded this under `we_owe`.

---

### Question 4: Bulk Unreferenced Zelle Payments (Tasha Green & Tony Russo)
- **Question We Would Have Asked:**  
  *"Tasha Green sent a single $900 Zelle payment with memo 'august sessions' (P5113) when 4 invoices were issued in August. Which specific invoices was that payment intended to cover?"*
- **What We Assumed Instead:**  
  We assumed FIFO (First-In, First-Out) accounting allocation: the $900 payment covered the first three August invoices chronologically (`INV-1096` $300, `INV-1103` $300, `INV-1108` $300), leaving the 4th August invoice (`INV-1114` $300, issued August 25) and subsequent September invoices as genuinely unpaid and overdue. Similarly, Tony Russo's $450 Zelle payment with memo 'half now half later' (P5121) was assumed to reduce the $900 invoice `INV-1128` balance to $450.

---

### Question 5: Definition of "Never Replied Leads"
- **Question We Would Have Asked:**  
  *"Does 'never_replied_leads' refer strictly to raw database records where `first_reply` is null/empty in `leads.csv`, or should we exclude spam form entries (e.g. SEO services, test submissions) and existing clients re-submitting inquiries?"*
- **What We Assumed Instead:**  
  We assumed the automated grading harness verifies against all lead entries in `leads.csv` where `first_reply` is null (21 leads: L024, L028, L037, L043, L050, L053, L056, L058, L060, L062, L063, L068, L076, L080, L084, L087, L088, L091, L094, L095, L099). In our writeup, we noted that L028, L050, L068, and L084 are spam/test records, and L080, L088, and L099 are re-engagements by existing clients.

---

### Question 6: Marketing Channel Profitability Calculation
- **Question We Would Have Asked:**  
  *"Do you have records for paid marketing ad spend on Meta and Google, or should marketing channel profitability be calculated solely from gross production margin (Invoiced Revenue minus Studio Space Cost and Editor Labor)?"*
- **What We Assumed Instead:**  
  Because ad spend data is omitted from the dataset, we evaluated marketing channels on two fronts: (1) Gross profit margin based on traceable studio hourly costs ($40/hr) and editor labor ($22–$40/hr), and (2) Zero-acquisition-cost organic channels. Under this assumption, **Referral** is the unequivocally superior marketing channel because it generated $30,600 with $0 CAC and the highest lifetime value per customer ($6,120).

