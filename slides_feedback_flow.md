# Presentation Slides Content: Multi-Round & Feedback Flow
## Ready-to-Use Content for Google Slides & Gemini

Use this structured content directly in Google Slides (or copy-paste into Gemini in Google Slides). It explains the entire **Feedback & Deal Closeout Flow** in **5 clean, standard, doubt-free slides**—matching the exact design and quality of Flows 1 and 2.

---

### Slide 1: Flow Overview & The Two Feedback Loops

* **Slide Title:** Flow 3: Multi-Round Execution & Feedback Loop
* **Subtitle:** Closing the Loop: From Mid-Call Tactics to Enterprise Institutional Memory
* **Layout:** Dual Feedback Loop Flowchart + Key Principles

#### Visual Flowchart (Include on Slide):
```text
                  ┌────────────────────────────────────────────────────────┐
                  │                 BUYER STARTS NEGOTIATION               │
                  └───────────────────────────┬────────────────────────────┘
                                              │
                                              ▼
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ LOOP 1: IN-FLIGHT ROUND FEEDBACK (During Calls)                                          │
│ Call 1 Notes  ──>  Buyer Logs Counter-Offers  ──>  AI Generates Round 2 Counter-Tactics │
└─────────────────────────────────────────────┬────────────────────────────────────────────┘
                                              │ (When Deal Concludes)
                                              ▼
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ LOOP 2: DEAL CLOSEOUT MEMORY (Post-Negotiation Institutional Memory)                    │
│                                                                                          │
│  [🏆 IF DEAL WON]  ──>  Calculate Verified $ Savings  ──>  Indexes as Golden Benchmark   │
│  [🛑 IF DEAL LOST] ──>  Log Vendor Floor Price ($1.98) ──>  Flags Supplier Pricing Risk   │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Slide Bullet Points:
* **The Reality:** Negotiations in manufacturing are never 1-call deals. They take multiple rounds across several days.
* **Loop 1 (Mid-Negotiation):** Logs evolving vendor counters, payment terms, and meeting notes, which refresh the AI tactics for Round 2.
* **Loop 2 (Post-Deal Closeout):** Won deals record verified dollar savings; Lost deals record vendor floor prices. This feedback feeds right back into the search engine for future buyers.

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, this is our third core flow: the Multi-Round and Feedback Loop. Negotiations in manufacturing take multiple rounds. Our architecture handles two feedback loops: Loop 1 logs what happened during the phone call and refreshes the AI advice for Round 2. Loop 2 triggers when the deal closes: Won deals calculate verified dollar savings, while Lost deals log vendor floor prices to protect future buyers."*

---

### Slide 2: Step 1: In-Flight Round Logging (During Calls)

* **Slide Title:** Step 1: Round-by-Round Negotiation Logging
* **Subtitle:** Tracking Commercial Counters, Delivery Windows, and Meeting Observations
* **Layout:** Interactive Round Logger UI Mockup + 4 Commercial Levers

#### Visual UI Card (Include on Slide):
```text
┌────────────────────────────────────────────────────────────────────────┐
│  📝 LOG RESULTS FOR ROUND 1 MEETING                                    │
├────────────────────────────────────────────────────────────────────────┤
│  🏢 Supplier Name:              [ Apex Steel Corp                ]     │
│                                                                        │
│  💰 COMMERCIAL COUNTER-OFFERS:                                         │
│  • Supplier Counter Price:      [ $13.80        ] per kg (Down from $14.50)│
│  • Buyer Last Counter Offer:    [ $12.20        ] per kg               │
│  • Promised Delivery Lead Time: [ 21 ] days (Buyer needed 14 days)     │
│  • Supplier Payment Demand:     [ 30% Advance + Net 30         ▼ ]     │
│                                                                        │
│  📦 MOQ / BATCH CONDITION:                                             │
│  • Did supplier demand higher MOQ for lower price?                     │
│    [x] Yes -> Demanded [ 8,000 ] kg minimum for any further discount   │
│                                                                        │
│  🗣️ DETAILED MEETING FEEDBACK & OBSERVATIONS (Text Field):             │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ "Sales rep Amit was firm on $13.80 citing nickel inflation, but  │  │
│  │  hinted that if we commit to an 8-ton Blanket PO over 6 months,  │  │
│  │  he can get factory approval for $12.50. Worried about our cash."│  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  [ Save Round 1 & Refresh AI Strategy for Round 2 ]                    │
└────────────────────────────────────────────────────────────────────────┘
```

#### Key Architecture Points:
* **Appends to Living Record:** Each meeting appends to the `rounds` JSONB array on the single master row.
* **Feeds AI for Next Round:** The AI reads the buyer's meeting notes and immediately recommends the counter-move for Round 2 (e.g., *"Offer an 8-ton Blanket PO split across 2 shipments, but demand $12.30"*).

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, after every phone call, the buyer opens the app and logs the meeting results. They record the supplier's new counter-price, delivery lead time, payment terms demanded, and qualitative notes. The AI reads these meeting notes and immediately updates the tactical playbook for Round 2."*

---

### Slide 3: Step 2: The Deal WON Flow (`closed_won`)

* **Slide Title:** Step 2: Deal WON Closeout & Automated Savings
* **Subtitle:** Verified Financial Cost Savings & Golden Advice Capture
* **Layout:** Mathematical Formula Banner + Won Modal UI Mockup

#### Automated Cost Savings Formula:
$$\text{Verified Financial Savings} = (\text{Supplier Initial Quote} - \text{Final Agreed Price}) \times \text{Order Quantity}$$
$$\mathbf{(\$14.50 - \$12.20) \times 5,000\text{ kg} = \$11,500\text{ Verified Direct Savings!}}$$

#### Visual Won Modal UI (Include on Slide):
```text
┌────────────────────────────────────────────────────────────────────────┐
│  🏆 FINALIZE AGREEMENT & RECORD WINNING DEAL                           │
├────────────────────────────────────────────────────────────────────────┤
│  1. Final Agreed Unit Price:    [ $12.20        ] per kg               │
│     Initial Quote was: $14.50   -->  Instant Savings: $11,500 Total!   │
│                                                                        │
│  2. Agreed Payment Terms:       [ Net 30 Days               ▼ ]        │
│  3. Agreed Delivery Lead Time:  [ 12 ] days                            │
│  4. Supplier Rating:            [ ★ ★ ★ ★ ☆ ] (4.5 / 5.0)              │
│                                                                        │
│  5. Winning Tactics Used:       [x] Payment terms trade                │
│                                 [x] Volume commitment                  │
│                                                                        │
│  6. 💡 Golden Advice for the Next Buyer:                               │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ "Apex Steel will drop to $12.20 if you offer Net 30 payment and  │  │
│  │  a quarterly schedule. Never accept their first freight estimate │  │
│  │  because they have a 5% margin buffer built into CIF shipping."  │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  [ Save & Publish to Company Memory Bank ]                             │
└────────────────────────────────────────────────────────────────────────┘
```

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, when the deal is won, the system does two critical things: First, it automatically calculates the verified dollar savings—here, saving $11,500 compared to the initial quote. Second, it captures Rahul's golden advice on how he convinced Apex Steel. This deal is immediately indexed as the active Golden Benchmark for all future buyers."*

---

### Slide 4: Step 3: The Deal LOST / Walkaway Flow (`closed_lost`)

* **Slide Title:** Step 3: Deal LOST Closeout & Vendor Risk Profiling
* **Subtitle:** Why Walking Away Is a Disciplined Manufacturing Victory
* **Layout:** Strategic Rationale Banner + Walkaway Modal UI Mockup

#### Strategic Principle:
> *"In manufacturing procurement, walking away from an overpriced vendor is a victory. It protects the factory's profit margins and teaches future buyers the supplier's limits."*

#### Visual Lost Modal UI (Include on Slide):
```text
┌────────────────────────────────────────────────────────────────────────┐
│  🛑 RECORD WALKAWAY / LOST NEGOTIATION                                 │
├────────────────────────────────────────────────────────────────────────┤
│  1. Primary Walkaway Reason:                                           │
│     [ Price exceeded our walkaway ceiling ($1.90)           ▼ ]        │
│     (Options: Price ceiling breached / Bad credit terms / Unresponsive)│
│                                                                        │
│  2. Supplier Rock-Bottom Floor Price:                                  │
│     [ $1.98 ] per kg  (Supplier sales director refused to budge below)│
│                                                                        │
│  3. Operational Next Step (BATNA):                                     │
│     [ Sourced from alternative vendor (Gulf Polymers at $1.82) ▼ ]     │
│                                                                        │
│  4. ⚠️ Vendor Risk Warning Notes for Future Buyers:                    │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ "PolyChem sales rep was inflexible citing crude oil tariffs.     │  │
│  │  Refused all concessions. Do not approach them without an active │  │
│  │  competing quote in hand."                                       │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  [ Record Walkaway & Update Vendor Risk Profile ]                      │
└────────────────────────────────────────────────────────────────────────┘
```

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, what if the negotiation fails? Walking away is a disciplined victory that protects company margins. The buyer records why they walked away, the supplier's rock-bottom floor price of $1.98, and their warning notes. In the future, when another buyer starts a deal with PolyChem, the system alerts them to this vendor's pricing rigidity."*

---

### Slide 5: Step 4: Database State Machine & The Closed Loop

* **Slide Title:** Step 4: Database State Machine & The Closed Loop
* **Subtitle:** How Evolving Negotiation Rows Permanently Enrich Institutional Memory
* **Layout:** State Machine Diagram + SQL Update Execution

#### Visual State Machine Diagram:
```text
                     ┌───────────────────────────────┐
                     │      STATE: in_progress       │
                     │  Active Rounds Logged in      │
                     │  rounds JSONB array           │
                     └──────────────┬────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
     ┌─────────────────────────────┐ ┌─────────────────────────────┐
     │      STATE: closed_won      │ │     STATE: closed_lost      │
     │  • final_unit_price: $12.20 │ │  • loss_reason: ceiling     │
     │  • savings: $11,500         │ │  • floor_price: $1.98       │
     │  • advice_for_future_buyers │ │  • vendor_risk_profile      │
     └──────────────┬──────────────┘ └──────────────┬──────────────┘
                    │                               │
                    └───────────────┬───────────────┘
                                    ▼
                    ┌───────────────────────────────┐
                    │  CONTINUOUS LEARNING LOOP     │
                    │  Feeds directly back into     │
                    │  Flow 1 (Historical Match)    │
                    └───────────────────────────────┘
```

#### Production SQL Finalization:
```sql
-- Finalizing a Won Deal on the Master Table
UPDATE negotiations 
SET status = 'closed_won',
    final_unit_price = 12.20,
    total_savings_amount = ((supplier_quote_price - 12.20) * quantity),
    agreed_payment_terms = 'Net 30',
    supplier_rating = 4.5,
    advice_for_future_buyers = 'Apex will drop to $12.20 if you offer Net 30 and quarterly schedule.',
    closed_at = CURRENT_TIMESTAMP
WHERE id = :negotiation_id AND org_id = :user_org_id;
```

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, finally, everything is handled by a clean state machine on our master negotiations table. When a deal is marked won or lost, a single SQL UPDATE command finalizes the row. This permanently closes the loop: every closed deal becomes the active benchmark or vendor risk warning for all future company negotiations."*
