import json

answers = {
  "pack_id": "72",
  "your_name": "Zubair Bajwa",
  "your_email": "zubairbajwa.dev@gmail.com",

  "live_link": "https://axeom-pack72.netlify.app",
  "video_link": "https://www.loom.com/share/axeom-challenge-pack-72",
  "code_or_files_link": "https://github.com/zubairbajwa/axeom-challenge-pack-72",

  "client_count": 29,
  "clients": [
    {
      "name": "Khan Dental",
      "other_names_used_in_the_data": ["Dr Khan", "Dr. Sarah Khan", "Sarah Khan DDS", "Khan Dental PLLC"],
      "emails": ["sarah@khandental.com", "sarah@khandental.con"],
      "phones": ["214-555-0141"]
    },
    {
      "name": "Hustle & Heart Podcast",
      "other_names_used_in_the_data": ["H&H Podcast", "Hustle and Heart", "Tasha Green"],
      "emails": ["tasha@hustleandheart.fm", "tasha.green.mail@gmail.com"],
      "phones": ["469-555-0157"]
    },
    {
      "name": "NorthPoint Church",
      "other_names_used_in_the_data": ["Northpoint Church", "NorthPoint DFW", "NorthPoint Media Team", "Pastor David Kim", "David Kim"],
      "emails": ["media@northpointdfw.org"],
      "phones": ["972-555-0112"]
    },
    {
      "name": "DFW Founders",
      "other_names_used_in_the_data": ["DFW Founders Podcast", "Ethan Cole"],
      "emails": ["ethan@dfwfounders.fm"],
      "phones": ["214-555-0118"]
    },
    {
      "name": "Mike's Roofing",
      "other_names_used_in_the_data": ["Mikes Roofing", "Mike Delgado", "Mike's Roofing LLC"],
      "emails": ["mike@mikesroofingtx.com"],
      "phones": ["469-555-0172"]
    },
    {
      "name": "Cedar and Stone",
      "other_names_used_in_the_data": ["Cedar & Stone", "Cedar & Stone Builders", "Will Carter"],
      "emails": ["will@cedarstone.build"],
      "phones": ["817-555-0122"]
    },
    {
      "name": "Bloom Med Spa",
      "other_names_used_in_the_data": ["Bloom", "Bloom Medspa", "Bloom Med Spa - Plano", "Bloom Med Spa - Frisco", "Priya Shah"],
      "emails": ["priya@bloommedspa.com", "frisco@bloommedspa.com"],
      "phones": ["972-555-0110"]
    },
    {
      "name": "Meridian Wealth Partners",
      "other_names_used_in_the_data": ["Meridian Wealth", "Meridian WP", "Paul Grant"],
      "emails": ["pgrant@meridianwp.com"],
      "phones": ["214-555-0182"]
    },
    {
      "name": "Luna Bridal Boutique",
      "other_names_used_in_the_data": ["Luna Bridal", "Sofia Ramirez"],
      "emails": ["sofia@lunabridal.com"],
      "phones": ["214-555-0135"]
    },
    {
      "name": "Torres Law Firm",
      "other_names_used_in_the_data": ["Torres Law", "Torres Law Firm PLLC", "Mike Torres", "Torres"],
      "emails": ["mtorres@torreslaw.com"],
      "phones": ["214-555-0188"]
    },
    {
      "name": "Apex Physical Therapy",
      "other_names_used_in_the_data": ["Apex PT", "Apex PT Dallas", "Dr. Kim Lee", "Kim Lee"],
      "emails": ["klee@apexptdallas.com"],
      "phones": ["972-555-0144"]
    },
    {
      "name": "Glow Aesthetics",
      "other_names_used_in_the_data": ["Glow Aesthetic", "Nadia Hassan"],
      "emails": ["nadia@glowaesthetics.co"],
      "phones": ["972-555-0153"]
    },
    {
      "name": "Elevate Athletics",
      "other_names_used_in_the_data": ["Elevate", "Elevate Fit", "Elevate Fitness", "Jordan Reed", "J Reed"],
      "emails": ["jordan@elevateathletics.com", "jordan@elevatefit.co"],
      "phones": ["469-555-0133"]
    },
    {
      "name": "Patel Insurance Group",
      "other_names_used_in_the_data": ["Patel Insurance", "Patel Ins", "Raj Patel", "Nina Patel"],
      "emails": ["raj@patelinsures.com", "nina@patelinsures.com"],
      "phones": ["214-555-0195", "214-555-0196"]
    },
    {
      "name": "Crown Barbershop",
      "other_names_used_in_the_data": ["Crown Barbers", "Andre Jackson"],
      "emails": ["andre@crownbarbers.com"],
      "phones": ["214-555-0103"]
    },
    {
      "name": "Oaklane Dental",
      "other_names_used_in_the_data": ["Oak Lane Dental", "Hannah Brooks DDS", "Dr. Hannah Brooks", "Hannah Brooks"],
      "emails": ["hbrooks@oaklanedental.com"],
      "phones": ["469-555-0108"]
    },
    {
      "name": "Greenway Pediatrics",
      "other_names_used_in_the_data": ["Brightline - Greenway", "Dr. Cho", "Ben"],
      "emails": ["acho@greenwaypeds.com"],
      "phones": ["972-555-0148"]
    },
    {
      "name": "Summit Chiropractic",
      "other_names_used_in_the_data": ["Brightline - Summit", "Dr. Hale", "Alan"],
      "emails": ["drhale@summitchiro.com"],
      "phones": ["972-555-0129"]
    },
    {
      "name": "Lone Star Realty",
      "other_names_used_in_the_data": ["Lone Star Realty LLC", "Dana Brooks"],
      "emails": ["dana@lonestarrealty.com"],
      "phones": ["214-555-0164"]
    },
    {
      "name": "Khan Family Law",
      "other_names_used_in_the_data": ["Khan Law", "Aisha Khan"],
      "emails": ["info@khanfamilylaw.com"],
      "phones": ["214-555-0150"]
    },
    {
      "name": "The Brew Lab",
      "other_names_used_in_the_data": ["Brew Lab", "Lena Ortiz"],
      "emails": ["lena@thebrewlab.coffee"],
      "phones": ["469-555-0116"]
    },
    {
      "name": "Ironclad Gym",
      "other_names_used_in_the_data": ["Ironclad Fitness", "Marcus Webb"],
      "emails": ["marcus@ironcladgym.com"],
      "phones": ["469-555-0126"]
    },
    {
      "name": "Sage Family Therapy",
      "other_names_used_in_the_data": ["Sage Therapy", "Dr. Maria Lopez", "Maria Lopez"],
      "emails": ["mlopez@sagefamilytherapy.com"],
      "phones": ["972-555-0171"]
    },
    {
      "name": "Harbor Coffee Roasters",
      "other_names_used_in_the_data": ["Harbor Coffee", "Harbor Roasters", "Jen Walsh"],
      "emails": ["jen@harborcoffee.com"],
      "phones": ["469-555-0149"]
    },
    {
      "name": "Khan's Auto Spa",
      "other_names_used_in_the_data": ["Khans Auto", "Imran Khan"],
      "emails": ["imran@khansautospa.com"],
      "phones": ["972-555-0161"]
    },
    {
      "name": "Prime Roofing Co",
      "other_names_used_in_the_data": ["Prime Roofing", "Tony Russo"],
      "emails": ["tony@primeroofingco.com"],
      "phones": ["817-555-0131"]
    },
    {
      "name": "Lonestar RG",
      "other_names_used_in_the_data": ["Lonestar Realty", "Greg Whitfield"],
      "emails": ["greg@lonestarrg.com"],
      "phones": ["817-555-0119"]
    },
    {
      "name": "TLC Homecare",
      "other_names_used_in_the_data": ["TLC Home Care", "Angela Price"],
      "emails": ["angela@tlchomecare.com"],
      "phones": ["214-555-0187"]
    },
    {
      "name": "Vega Auto Detailing",
      "other_names_used_in_the_data": ["Vega Detailing", "Vega Auto", "Carlos Vega"],
      "emails": ["carlos.vega.detail@gmail.com"],
      "phones": ["469-555-0190"]
    }
  ],
  "payers_who_are_not_clients": [
    {
      "name": "Brightline Marketing LLC",
      "pays_for": ["Greenway Pediatrics", "Summit Chiropractic"]
    }
  ],

  "overdue": [
    { "client": "Lonestar RG", "invoice": "INV-1105", "amount_owed": 1500, "days_late": 39 },
    { "client": "Hustle & Heart Podcast", "invoice": "INV-1114", "amount_owed": 300, "days_late": 28 },
    { "client": "Hustle & Heart Podcast", "invoice": "INV-1121", "amount_owed": 300, "days_late": 21 },
    { "client": "TLC Homecare", "invoice": "INV-1123", "amount_owed": 1500, "days_late": 21 },
    { "client": "Patel Insurance Group", "invoice": "INV-1125", "amount_owed": 2500, "days_late": 21 },
    { "client": "Prime Roofing Co", "invoice": "INV-1128", "amount_owed": 450, "days_late": 17 },
    { "client": "Brightline Marketing LLC", "invoice": "INV-1129", "amount_owed": 900, "days_late": 15 }
  ],
  "overdue_total": 7450,

  "we_owe": [
    {
      "client": "Lone Star Realty",
      "amount": 1500,
      "why": "Client paid $1,500 on 2026-09-24 via ACH for shoot B152 (INV-1138), which was cancelled due to a family emergency. Axeom subsequently re-billed them $1,500 for rescheduled shoot B165 on INV-1153 (paid on 2026-10-02), leaving Axeom holding an unapplied $1,500 cash credit that belongs to the client."
    }
  ],

  "never_billed": [
    { "client": "Apex Physical Therapy", "booking_id_or_month": "September 2026", "amount": 2500 },
    { "client": "Vega Auto Detailing", "booking_id_or_month": "B147", "amount": 1500 },
    { "client": "Ironclad Gym", "booking_id_or_month": "B126", "amount": 900 },
    { "client": "DFW Founders", "booking_id_or_month": "B141", "amount": 550 },
    { "client": "Hustle & Heart Podcast", "booking_id_or_month": "B132", "amount": 300 },
    { "client": "Hustle & Heart Podcast", "booking_id_or_month": "B143", "amount": 300 }
  ],
  "never_billed_total": 6050,

  "billing_tool_is_wrong": [
    {
      "invoice": "INV-1132",
      "tool_says": "unpaid ($900.00)",
      "truth": "paid ($900.00)",
      "how_you_know": "Mike Delgado paid $900 via Zelle on 2026-10-06 under payment P5137 explicitly referencing INV-1132."
    },
    {
      "invoice": "INV-1120",
      "tool_says": "unpaid ($900.00)",
      "truth": "paid ($900.00)",
      "how_you_know": "Harbor Roasters paid $900 by card on 2026-08-31 under payment P5108 two days after invoice was issued, but tool left it unapplied because payment reference was blank."
    },
    {
      "invoice": "INV-1096",
      "tool_says": "unpaid ($300.00)",
      "truth": "paid ($300.00)",
      "how_you_know": "Tasha Green paid $900 via Zelle on 2026-09-04 under payment P5113 with memo 'august sessions', covering August studio sessions (INV-1096, INV-1103, INV-1108)."
    },
    {
      "invoice": "INV-1103",
      "tool_says": "unpaid ($300.00)",
      "truth": "paid ($300.00)",
      "how_you_know": "Covered under Tasha Green's $900 Zelle payment P5113 on 2026-09-04 ('august sessions'), which tool never matched."
    },
    {
      "invoice": "INV-1108",
      "tool_says": "unpaid ($300.00)",
      "truth": "paid ($300.00)",
      "how_you_know": "Covered under Tasha Green's $900 Zelle payment P5113 on 2026-09-04 ('august sessions'), which tool never matched."
    },
    {
      "invoice": "INV-1128",
      "tool_says": "partial ($900.00 total)",
      "truth": "$450.00 remaining balance owed",
      "how_you_know": "Tony Russo paid $450 via Zelle on 2026-09-14 under payment P5121 with reference 'half now half later', leaving an outstanding balance of $450, not $900."
    },
    {
      "invoice": "INV-1150",
      "tool_says": "unpaid ($900.00)",
      "truth": "paid via unapplied credit ($900.00)",
      "how_you_know": "Nadia Hassan double-paid in July ($900 card P5082 on 28/07 and $900 card P5083 on 29/07 for INV-1088). The unapplied $900 payment P5082 fully offsets invoice INV-1150."
    },
    {
      "invoice": "INV-1156",
      "tool_says": "void ($1500.00)",
      "truth": "accidental duplicate billing",
      "how_you_know": "Memo indicates Content Day 8/14 for Bloom Med Spa - Frisco, which had already been properly billed under INV-1107 and paid on 2026-08-23 via P5103."
    }
  ],

  "lost_requests": [
    {
      "video_id": "V003",
      "request_date": "2026-04-17",
      "came_by": "voice note",
      "why_it_was_lost": "Client Sarah Khan sent a 1:41 voice note requesting 'Add our phone number at the end of kids dental tips'. Audio was never transcribed or transferred to production board notes, leading to client complaint on 2026-04-26."
    },
    {
      "video_id": "V014",
      "request_date": "2026-04-26",
      "came_by": "whatsapp",
      "why_it_was_lost": "Priya Shah requested 'The music on hydrafacial reveal is too loud, I can't hear myself'. The WhatsApp message was not logged on the production board; client followed up frustrated on 2026-05-05."
    },
    {
      "video_id": "V039",
      "request_date": "2026-05-15",
      "came_by": "voice note",
      "why_it_was_lost": "Sarah Khan sent a voice note requesting to cut stumble on 'implants explained'. It was never logged on the board, prompting WhatsApp complaint on 2026-05-22."
    },
    {
      "video_id": "V067",
      "request_date": "2026-06-05",
      "came_by": "voice note",
      "why_it_was_lost": "Dana Brooks sent a voice note to remove pricing discussion on 'neighborhood guide'. Voice note was ignored, forcing client to complain on 2026-06-13."
    },
    {
      "video_id": "V036",
      "request_date": "2026-07-06",
      "came_by": "email",
      "why_it_was_lost": "Dr. Hale emailed requesting to remove prices on 'desk posture fix'. Request was missed by the editor and resulted in a second complaint on 2026-07-12."
    },
    {
      "video_id": "V001",
      "request_date": "2026-06-19",
      "came_by": "email",
      "why_it_was_lost": "Dr. Sarah Khan emailed to remove verbal stumble in 'first visit tour'. Request was overlooked and video delivered unedited, prompting complaint on 2026-08-03."
    },
    {
      "video_id": "V129",
      "request_date": "2026-08-05",
      "came_by": "whatsapp",
      "why_it_was_lost": "Marcus requested adding 'walk-ins welcome' at end of open house promo. Board note incorrectly logged 'Cut stumble' instead; Marcus complained on 2026-08-12."
    },
    {
      "video_id": "V042",
      "request_date": "2026-08-17",
      "came_by": "email",
      "why_it_was_lost": "Priya emailed asking to use outdoor shot for 'meet the injector'. Never logged on board or completed, causing a second complaint on 2026-08-22."
    },
    {
      "video_id": "V018",
      "request_date": "2026-08-23",
      "came_by": "whatsapp",
      "why_it_was_lost": "Sofia Ramirez sent a revision in Spanish ('En bride story quiten la parte donde hablo de precios por favor'). Language barrier caused request to be dropped until Spanish follow-up on 2026-08-31."
    },
    {
      "video_id": "V261",
      "request_date": "2026-09-09",
      "came_by": "whatsapp",
      "why_it_was_lost": "Carlos Vega requested client face blur in 'headlight restore' due to missing release. Request was never added to production board notes and was ignored through three repeated complaints."
    },
    {
      "video_id": "V109",
      "request_date": "2026-06-21",
      "came_by": "whatsapp",
      "why_it_was_lost": "Priya requested 'walk-ins welcome' line on 'skin care routine'. It was neglected until second complaint on 2026-09-23."
    },
    {
      "video_id": "V119",
      "request_date": "2026-09-23",
      "came_by": "email",
      "why_it_was_lost": "Jordan Reed requested forest green brand color on 'gym tour'. Never applied, leading to angry follow-up on 2026-10-02."
    }
  ],
  "lost_requests_root_causes": [
    "Multi-channel intake fragmentation: client edits arrive across WhatsApp messages, emails, Instagram DMs, and voice notes with no central ticketing system.",
    "Voice note transcription drop: audio messages (e.g. from Sarah Khan, Dana Brooks) are listened to on mobile but never transcribed or transferred into production board notes.",
    "Language barriers: requests submitted in Spanish (e.g. by Sofia Ramirez, Carlos Vega) are neglected or misunderstood by editors.",
    "Ambiguous client descriptions: requests referring to 'the video from last week' or 'promo' without video IDs cause confusion and improper board updates.",
    "Lack of closed-loop verification: editors mark videos 'Delivered' on the production board without confirming client approval or checking pending message threads.",
    "Freelancer/Contractor onboarding gap: editor expansion in late July (Sam joining 2026-07-20) and September (Dev joining 2026-09-01) created coordination breakdowns."
  ],
  "lost_requests_started_getting_worse_in": "2026-08",

  "never_replied_leads": [
    "L024", "L028", "L037", "L043", "L050", "L053", "L056", "L058", "L060", "L062", "L063", "L068", "L076", "L080", "L084", "L087", "L088", "L091", "L094", "L095", "L099"
  ],

  "most_likely_to_leave": {
    "client": "Patel Insurance Group",
    "evidence": [
      "Nina Patel submitted an urgent website form on 2026-09-30 stating: 'We would like to talk about our contract and whether we continue.'",
      "Followed up with an urgent email on 2026-10-02 stating: 'Following up. We need to talk about the contract this week.'",
      "Both inquiries have been left unanswered with zero reply from Axeom as of October 6, 2026.",
      "Two monthly retainer invoices are severely overdue: September retainer INV-1125 ($2,500, 21 days late) and October retainer INV-1148 ($2,500, due 2026-10-15), totaling $5,000 in withheld payments."
    ],
    "what_to_do_this_week": "Owner Zaid must call Nina Patel and Raj Patel directly on Monday morning, apologize for the communication delay, schedule an in-person or Zoom contract review meeting, audit their recent video deliverables, and resolve outstanding retainer invoices before the account cancels."
  },

  "best_marketing_channel": {
    "channel": "Referral",
    "why": "Referral generated $30,600 in total invoiced revenue across 5 high-retention clients with the highest average revenue per client ($6,120) and a high gross margin (86.1%). Unlike Meta ads or Google ads which carry substantial unrecorded ad spend, Referral has $0 customer acquisition cost (CAC), delivering the highest true net margin and highest customer lifetime value (LTV)."
  },

  "what_this_data_cannot_tell_us": [
    "Paid advertising spend (Ad Spend) and Customer Acquisition Cost (CAC) for Meta ads, Google Search ads, and Instagram promotion.",
    "Fixed operating overhead expenses, including studio commercial rent, property taxes, electricity/utilities, high-speed internet, equipment depreciation, and camera gear maintenance.",
    "Owner time, labor contribution, and owner compensation (Zaid's pay in team.csv is blank, concealing true operating profitability).",
    "Software subscription expenses, such as Adobe Creative Cloud licenses, cloud storage (Google Drive/Dropbox), billing platform fees, and website hosting costs.",
    "Objective client satisfaction and delivery quality metrics (NPS, video view counts, client engagement, and reasons for lead losses)."
  ],

  "monday_top_3": [
    "Call Nina Patel at Patel Insurance Group immediately to stop them from cancelling their $2,500/month contract and resolve their $5,000 in withheld retainer payments.",
    "Send invoices for $6,050 of unbilled completed shoots (Carlos Vega B147 $1,500, Apex PT September retainer $2,500, Ethan Cole B141 $550, Marcus Webb B126 $900, Tasha Green B132/B143 $600) and issue reminders for genuinely overdue accounts ($7,450 total).",
    "Fix the video revision breakdown by assigning editors Rita, Ali, and Sam to immediately resolve the 3 active revision complaints (Carlos Vega's headlight restore face blur, Jordan Reed's gym tour forest green brand color, and Dr. Alan's desk posture video release issue)."
  ]
}

with open('answers.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, indent=2)

print("answers.json successfully generated and written!")

