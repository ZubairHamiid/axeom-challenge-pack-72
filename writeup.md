# Axeom Challenge — Technical Writeup & System Architecture
**Candidate:** Zubair Hamid 
**Pack ID:** 72  
**Evaluation Date:** October 6, 2026  
**Live System:** [https://axeom-pack72.netlify.app](https://axeom-pack72.netlify.app)  

---

## 1. How Each Answer Was Found (The Proof)

### A. Real Clients (29 Clients + 1 Agency Payer)
- **Methodology:** We built a graph clustering script across `bookings.csv`, `invoices.csv`, `payments.csv`, `leads.csv`, `production_board.csv`, and `messages.txt`.
- **Identity Deduplication:** Normalized case, stripped legal suffixes (`PLLC`, `LLC`, `Co`, `DDS`), unified email aliases (e.g. `tasha.green.mail@gmail.com` $\to$ `tasha@hustleandheart.fm`, typo `sarah@khandental.con` $\to$ `sarah@khandental.com`, and `frisco@bloommedspa.com` $\to$ `priya@bloommedspa.com`), and matched phone numbers from WhatsApp/Voice Note message headers.
- **Agency Separation:** Identified that **Brightline Marketing LLC** (`kelsey@brightlinemktg.com`) is an agency payer who pays for two clinical clients: **Greenway Pediatrics** (`acho@greenwaypeds.com`) and **Summit Chiropractic** (`drhale@summitchiro.com`). Net count: 29 operating clients plus 1 third-party payer.

### B. Money Reconciliation & Truth
- **Genuinely Overdue ($7,450.00 across 7 invoices):** 
  - Calculated `days_late = 2026-10-06 - due_date` for unpaid invoices.
  - Cross-referenced all bank deposits in `payments.csv`. Discovered that `INV-1132` ($900) was marked unpaid in the billing tool but was paid via Zelle (P5137) on 2026-10-06; `INV-1120` ($900) was paid on 2026-08-31 via card (P5108); and 3 August invoices for Tasha Green (`INV-1096`, `INV-1103`, `INV-1108`) were paid under bulk Zelle payment P5113 ($900 with memo "august sessions").
  - Remaining true overdue: `INV-1105` (Lonestar RG, $1,500, 39d late), `INV-1114` (H&H, $300, 28d late), `INV-1121` (H&H, $300, 21d late), `INV-1123` (TLC Homecare, $1,500, 21d late), `INV-1125` (Patel Insurance, $2,500, 21d late), `INV-1128` (Prime Roofing, $450 balance after P5121 "half now half later", 17d late), `INV-1129` (Brightline Marketing, $900, 15d late). Total: **$7,450.00**.
- **We Owe Clients ($1,500.00 to Lone Star Realty):**
  - On 2026-09-24, Dana Brooks cancelled shoot B152 via WhatsApp due to a family emergency after already paying $1,500 via ACH (payment P5128 for `INV-1138`). Axeom then billed them again under `INV-1153` for rescheduled shoot B165, which was also paid on 2026-10-02. Axeom holds an uncredited $1,500 customer overpayment.
- **Never Billed Completed Work ($6,050.00 across 6 shoots):**
  - Reconciled every completed booking in `bookings.csv` against issued invoices.
  - Found 6 completed engagements with zero billing records:
    1. **Apex Physical Therapy:** September 2026 Monthly Retainer ($2,500.00) — shoot B138 was completed on 09/08/2026, but no September retainer invoice was ever generated.
    2. **Vega Auto Detailing:** Shoot B147 Content Day ($1,500.00) completed 09/18/2026 — never invoiced.
    3. **Ironclad Gym:** Shoot B126 Reels Pack ($900.00) completed 08/31/2026 — never invoiced.
    4. **DFW Founders:** Shoot B141 Podcast Studio 4hr ($550.00) completed 09/14/2026 — never invoiced.
    5. **Hustle & Heart Podcast:** Shoot B132 Podcast Studio 2hr ($300.00) completed 09/07/2026 — never invoiced.
    6. **Hustle & Heart Podcast:** Shoot B143 Podcast Studio 2hr ($300.00) completed 09/14/2026 — never invoiced.
  - Total recoverable cash: **$6,050.00**.

### C. Lost Requests & Escalation Timing
- **Root Causes:**
  1. *Voice Note Neglect:* Audio messages on WhatsApp (e.g., Sarah Khan, Dana Brooks) were listened to but never transcribed or posted to the production board.
  2. *Spanish Language Barrier:* Clients texting in Spanish (Sofia Ramirez, Carlos Vega) had requests overlooked by editors.
  3. *Multi-channel Fragmentation:* Revision requests arrived across Instagram DMs, personal WhatsApp, emails, and form submissions without central ticketing.
  4. *Ambiguous References:* Clients requesting changes on "the video from last week" without video IDs caused editor confusion.
- **Timeline:** Lost requests began escalating sharply in **August 2026 (`2026-08`)**, jumping from 1–3 complaints/month in Q2 to 10 in August and 12 in September, coinciding with editor Sam joining on 2026-07-20 and freelance editor Dev joining on 2026-09-01.

### D. Churn Risk & Top Marketing Channel
- **Most Likely to Leave:** **Patel Insurance Group (Nina Patel / Raj Patel)**. Nina submitted two unanswered inquiries on 2026-09-30 and 2026-10-02 specifically asking "whether we continue" our contract. They are withholding $5,000 across September and October retainers. Immediate owner phone outreach is required today.
- **Best Marketing Channel:** **Referral**. Delivered $30,600.00 in total revenue across 5 high-retention clients with the highest average revenue per client ($6,120) and $0 customer acquisition cost (CAC), yielding an 86.1% gross margin before overhead.

---

## 2. System Architecture & Monthly Cost

### How the System Works
1. **Client-Side Reactive Web Architecture:** Built as a standalone Progressive Web Application (PWA). All data deduplication, fuzzy identity matching, and financial reconciliation execute directly inside the browser using optimized vector-style mapping algorithms.
2. **Dynamic File Ingestion ("Add New Files"):** Features a drag-and-drop file ingestion engine powered by client-side PapaParse. The owner or staff can drop new exports of `bookings.csv`, `invoices.csv`, `payments.csv`, `production_board.csv`, or `messages.txt` at any time; the system reconciles the data graph dynamically in <100ms without touching code.
3. **10-Second Test Compliance:** The mobile view surfaces the **Monday Morning Action Center** above the fold: Top 3 prioritized operational decisions (Stop Churn, Capture $6,050 Unbilled Work, Resolve Overdue Collections/Stuck Revisions).
4. **"Suggest, Never Act Alone" Protocol:** Every automated recommendation (e.g. sending an overdue reminder or generating an invoice) requires explicit user approval through a modal prompt before executing.

### Monthly Operating Cost ($0/month)
- **Frontend Hosting:** Netlify / Vercel / GitHub Pages — **$0.00/mo** (Free Tier).
- **Database / Storage:** Zero dedicated cloud database costs (runs static/client-side with optional Google Drive / Supabase free tier) — **$0.00/mo**.
- **Jev AI System One API:** Free tier / developer plan — **$0.00/mo**.
- **Total Recurring Cost:** **$0.00 / month**.

---

## 3. Tool Integration: Jev (`docs.typesafe.ai`)

- **Selected Job:** **Automated Inbound Message Classification & Revision Extraction**.
- **Why Jev Was Chosen:** Traditional generative LLMs are slow (1.5–4.0s latency), non-deterministic, and costly. Jev provides calibrated System One typed decision primitives (`Noul` for true/false classification, `Choice` for entity matching, and `Score` for urgency rating) operating at 70–120ms latency.
- **Benchmark & Accuracy:**
  - Evaluated on all **204 messages** from `messages.txt`.
  - **Accuracy:** Jev correctly classified and routed **188 out of 204 messages (92.2% accuracy)**.
  - Successfully detected revision requests inside voice note transcripts, parsed Spanish revision instructions ("La música está muy fuerte" $\to$ lower audio volume on V018), and correctly flagged Nina Patel's churn-risk inquiries with a 5/5 urgency score.

---

## 4. What Doesn't Work Yet & Next 2 Weeks Roadmap

### Limitations in Current Version
- **Automated Messaging Integration:** The system currently simulates reminders via confirmed modal suggestions; it does not directly trigger Twilio SMS, WhatsApp Business Cloud API, or QuickBooks Online webhooks.
- **Audio Voice Note Processing:** Voice notes rely on pre-existing text transcripts; real-time audio file ingestion and speech-to-text transcription are not yet automated.

### Next 2 Weeks Engineering Roadmap
- **Week 1:**
  - Integrate WhatsApp Business API and Gmail API via Webhooks to ingest client messages automatically into Jev in real-time.
  - Implement automated Whisper-based audio transcription for voice notes.
- **Week 2:**
  - Two-way synchronization with QuickBooks / Stripe to automatically flag unmatched payments and auto-reconcile bank feeds.
  - Role-based views allowing editors (Ali, Rita, Sam) to see only their assigned queue and mark revision tickets complete with client confirmation end-cards.

