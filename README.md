# Axeom Challenge — Pack 72
**Candidate:** Zubair Bajwa  
**Repository:** [https://github.com/ZubairHamiid/axeom-challenge-pack-72](https://github.com/ZubairHamiid/axeom-challenge-pack-72)  
**Simulation Date:** October 6, 2026  

---

## 📌 Executive Summary

This repository contains the complete forensic business audit, analytical answers, and interactive operational software system for the **Axeom Challenge (Pack 72)**.

Axeom is a content production and podcast studio based in Dallas, Texas serving ~30 clients. Its operations were severely hindered by disconnected data across eight separate files (`leads.csv`, `bookings.csv`, `invoices.csv`, `payments.csv`, `production_board.csv`, `messages.txt`, `costs.csv`, and `team.csv`).

This project solves all core business breakdowns:
1. **Financial Forensic Audit:** Uncovered **\$6,050.00** in unbilled completed work, verified **\$7,450.00** in true overdue accounts, caught **8 billing software discrepancies**, and identified **\$1,500.00** in client overpayments.
2. **Quality & Revision Recovery:** Identified the root cause of client revision breakdowns (dropped voice notes and language barriers escalating since **August 2026**).
3. **10-Second Test Operating Dashboard (`index.html`):** Built a mobile-first, zero-dependency client application that surfaces the **Monday Morning Top 3 Priorities** in under 10 seconds.
4. **Jev AI Integration:** Integrated TypeSafe AI's **Jev** System One decision engine for sub-100ms structured inbound message routing.

---

## 📁 Repository Structure & Deliverables

| File / Folder | Description |
| :--- | :--- |
| **`answers.json`** | Filled-in submission template with 100% verified analytical answers. |
| **`index.html`** | Standalone reactive web app passing the 10-second test with "Add New Files" ingestion. |
| **`app_data.js`** | Preloaded Pack 72 dataset enabling instant client-side execution. |
| **`writeup.md`** | 2-page technical writeup detailing proof methods, system architecture, \$0/mo cost, Jev job, and 2-week roadmap. |
| **`assumptions.md`** | Complete log of business assumptions made in place of asking questions. |
| **`daily_log.md`** | Daily journal tracking decisions, pivots, and fixes over the 3-day assessment. |
| **`ai_log.md`** | Comprehensive log of AI prompts, verification methods, and errors caught. |
| **`video_script.md`** | Word-for-word transcript and guide for the 5–10 min Loom walkthrough and direct camera questions. |
| **`data/`** | Raw Pack 72 CSV and text dataset files. |

---

## 🚀 How to Run the Web Application

The application is completely self-contained with zero build steps or server setup needed:
1. Clone the repository:
   ```bash
   git clone https://github.com/ZubairHamiid/axeom-challenge-pack-72.git
   cd axeom-challenge-pack-72
   ```
2. Double-click **`index.html`** to open directly in any modern browser (Chrome, Edge, Safari, Firefox).
3. Press `F12` and toggle the **Device Toolbar (Ctrl+Shift+M)** to test on mobile screens (iPhone / Android).
4. Use the **"Add New Files"** button to upload new CSV/TXT files; the app dynamically recalculates metrics in <100ms.

---

## 🔑 Key Verified Findings

* **Real Clients:** 29 active operating clients + 1 third-party agency payer (**Brightline Marketing LLC** paying for Greenway Pediatrics & Summit Chiropractic).
* **Genuinely Overdue:** **\$7,450.00** across 7 invoices (`INV-1105`, `INV-1114`, `INV-1121`, `INV-1123`, `INV-1125`, `INV-1128`, `INV-1129`).
* **Never Billed Work:** **\$6,050.00** across 6 completed shoots:
  - Apex Physical Therapy (Sept 2026 Monthly Retainer): **\$2,500.00**
  - Vega Auto Detailing (B147 Content Day): **\$1,500.00**
  - Ironclad Gym (B126 Reels Pack): **\$900.00**
  - DFW Founders (B141 Podcast 4hr): **\$550.00**
  - Hustle & Heart Podcast (B132 & B143 Podcast 2hr): **\$600.00**
* **We Owe:** **\$1,500.00** to **Lone Star Realty** (overpayment on cancelled shoot B152 re-billed under INV-1153).
* **Most Likely to Churn:** **Patel Insurance Group (Nina Patel)** with two unread contract inquiries and \$5,000 in withheld retainer payments.
* **Top Marketing Channel:** **Referral** (\$30,600 revenue, \$6,120 avg revenue/client, \$0 CAC, 86.1% gross margin).
