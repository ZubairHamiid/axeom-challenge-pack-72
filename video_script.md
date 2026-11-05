# Loom Video Recording Script & Transcript Guide
**Assessment:** Axeom Challenge — Pack 72  
**Format:** 5 to 10 minutes, screen share + camera on, no notes, no cuts.  

---

## Part 1: System Demonstration (Minutes 0:00 – 4:00)

### [Show Mobile Screen View in Browser DevTools: iPhone 14/15 or Android]
*"Hi team, my name is Zubair Bajwa, and this is my submission for the Axeom Challenge, Pack 72.*

*Axeom’s owner has four big problems: video edits come back wrong, he doesn’t know who really owes him money, leads slip through the cracks, and his current task screen is overwhelming.*

*To solve this, I built a lightweight, mobile-first operating system designed to pass the 10-second test.*

### 1. The 10-Second Test (Monday Morning Focus)
*(Point to the top hero section on the phone screen)*
*When Zaid opens this on his phone on Monday morning, he doesn't see thirty overwhelming graphs. Within 10 seconds, he sees the three highest-leverage actions:*
1. *First: Stop an urgent client churn. Nina Patel at Patel Insurance sent two unread messages asking whether to continue their contract, and they owe two overdue retainers. We have a 'Call Now' button right here.*
2. *Second: Capture $6,050 in unbilled work. Six completed shoots—including Carlos Vega’s Content Day and Apex PT’s September retainer—were never invoiced. He can click 'Generate Invoices' to draft them immediately.*
3. *Third: Cash & Quality. We have $7,450 in genuinely overdue invoices ready for reminders, and three critical revision complaints that need editor dispatch.*

### 2. Suggest, Never Act Alone
*(Click 'Call Now' or 'Review Reminders' to show the modal)*
*Notice that when I click an action, nothing is sent automatically. A clear suggestion modal appears asking: 'Send overdue payment reminder to Greg Whitfield for $1,500?' The owner has total control with 'Yes, Confirm' or 'Cancel'.*

### 3. Connected Data (Client 360°)
*(Click on 'Clients 360°' tab, search for 'Khan Dental')*
*Our database had Sarah Khan spelled as 'Dr Khan', 'Dr. Sarah Khan', 'Khan Dental PLLC', and even had a typo with '.con'. Our entity resolution links all of these together. Clicking into Khan Dental brings up their entire 360-degree profile: total billed, total paid, bookings history, invoice statuses, and every video on the production board.*

### 4. Financial Truth vs. The Broken Billing Tool
*(Switch to 'Financial Truth' tab)*
*The billing tool was lying in eight different places. For example, it showed Mike’s Roofing as unpaid, but Mike paid $900 via Zelle on October 6th referencing invoice INV-1132. It also showed Tasha Green as four invoices behind, but Tasha sent a $900 Zelle payment in September marked 'august sessions' that the billing tool never matched. Our system shows the reconciled ground truth.*

### 5. Dynamic Ingestion ('Add New Files')
*(Click the 'Add New Files' button at the top)*
*Here is our file uploader. When Axeom’s team exports new CSV files or text logs in the future, they simply drag and drop them here. The entire database re-indexes in the browser in under 100 milliseconds—no server reboot, no code changes required.*

### 6. Jev AI Integration
*(Switch to 'Jev AI Engine' tab)*
*To stop lost requests, we integrated Jev from TypeSafe AI. Unlike slow LLMs, Jev uses sub-100 millisecond System One typed decisions to parse incoming WhatsApp messages, voice note transcripts, and Spanish texts into structured revision tickets and route them directly to editors Rita, Ali, and Sam.*

---

## Part 2: Direct Camera Answers (Minutes 4:00 – 7:30)

### [Look directly into the camera, speak naturally and confidently]

### Question 1: What was the hardest part, and how did you solve it?
*"The hardest part was uncovering the unbilled revenue for retainer clients.*

*With one-off clients, finding unbilled work is simple: you match the booking ID to the invoice memo. But retainer clients like Apex Physical Therapy don’t have a price on their booking—their shoots are listed as $0 because they pay a monthly flat fee.*

*To solve this, I had to reconstruct the entire chronological billing sequence for every retainer client. That’s how I discovered that Apex Physical Therapy had shoot B138 completed on September 8th, but while they were billed for June, July, August, and October, the September invoice was completely missing. That single insight unlocked $2,500 in clean, recoverable cash for the business, bringing our never-billed total to $6,050."*

---

### Question 2: What did you get wrong at first?
*"At first, I completely trusted the `status` column in `invoices.csv`.*

*When I first filtered for unpaid invoices, the tool claimed that Mike's Roofing owed $900 on invoice INV-1132, and that Harbor Roasters owed $900 on invoice INV-1120. I almost put them down as overdue.*

*Then I cross-checked `payments.csv` and realized the billing tool was broken. Mike Delgado had literally paid $900 via Zelle today, October 6th, referencing INV-1132. And Harbor Roasters had paid $900 by credit card back on August 31st, but because the payment reference was blank, the billing software never reconciled it.*

*I had to change my approach from trust to forensic auditing: never take the invoice status at face value; always verify against the bank deposit ledger."*

---

### Question 3: What would you tell the owner to stop doing?
*"I would tell Zaid to immediately stop doing two things:*

*First, stop accepting client edit requests over personal WhatsApp, voice notes, and Instagram DMs.*
*The data shows a massive breakdown starting in August: clients send a voice note while driving, Zaid listens to it in the car, doesn't transcribe it, and it never gets written on the production board. Editors deliver the video unchanged, the client gets furious, and trust erodes. Every single edit request must go through a single structured intake channel.*

*Second, stop billing manually after shoots happen.*
*Axeom is currently bleeding $6,050 in completed work that was never billed, while simultaneously holding a $1,500 overpayment from Dana Brooks for a cancelled shoot. Zaid must require credit card pre-authorization or upfront retainer billing before cameras ever roll in the studio.*

*Thank you for your time and review."*

