# Presentation Slides Content: Negotiation Intake & AI Battlecard Engine
## Ready-to-Use Content for Google Slides & Gemini

Use this structured content directly in Google Slides (or copy-paste into Gemini in Google Slides). It explains the entire flow in **5 clean, standard, doubt-free slides**, now including the **Past Deal Check** step in the flowchart.

---

### Slide 1: Flow Overview (Input $\rightarrow$ Past Deal Check $\rightarrow$ AI $\rightarrow$ Output)

* **Slide Title:** Flow 1: Negotiation Intake & AI Battlecard Engine
* **Subtitle:** Turning 2 Minutes of Form Input into an Instant Pre-Call Strategy
* **Layout:** Flowchart Diagram + 4 Summary Pillars

#### Visual Flowchart (Include on Slide):
```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│    1. INPUT     │  ──>  │  2. CHECK PAST  │  ──>  │    3. AI        │  ──>  │   4. OUTPUT     │
│ 19 Questionnaire│       │     DEALS       │       │ Exact Prompt    │       │ Battlecard UI   │
│     Answers     │       │ Review Benchmrk │       │ to Gemini Flash │       │ + Save in 1 Row │
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘
```

#### Slide Bullet Points:
* **Step 1: Input:** Buyer answers 19 standard questions about specs, quantity, price, and supplier.
* **Step 2: Instant Past Deal Check:** System automatically checks company records so the buyer can review past similar deals and historical prices before proceeding.
* **Step 3: AI Processing:** The exact answers (plus any past deal benchmark) are sent to Google Gemini 2.0 Flash.
* **Step 4: Output & Storage:** Generates a 1-page Pre-Call Battlecard (leverage score, weak points, scripts) and saves everything in a single PostgreSQL row.

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, here is the complete flow. The buyer fills a 2-minute questionnaire. Immediately, the system checks our company database so the buyer can review if we bought this item before. Then, the system sends the answers to Gemini to generate a Pre-Call Battlecard with leverage scores and counter-scripts, saving everything in one database row."*

---

### Slide 2: Step 1: The Input (The 5-Stage Questionnaire)

* **Slide Title:** Step 1: The Input (5-Stage Intake Questionnaire)
* **Subtitle:** 19 Standard Parameters Covering Every Commercial Dimension
* **Layout:** 5 Structured Cards / Columns

#### Slide Content:

1. **Stage 1: Item & Specifications**
   * *Fields:* Material Name (`Cold Rolled Steel Sheet`), Grade (`SS 304`), Customization (`Commodity`), Quality (`High Precision`).
   * *Purpose:* Tells AI if this is an off-the-shelf commodity or custom locked-in part.

2. **Stage 2: Scale & Volume**
   * *Fields:* Order Batch (`5,000 kg`), Unit (`kg`), Frequency (`Quarterly`), Annual Volume (`20,000 kg`), MOQ Flexibility (`Flexible`).
   * *Purpose:* Gives the buyer volume leverage for tiered price discounts.

3. **Stage 3: Commercial Boundaries**
   * *Fields:* Supplier Quote (`$14.50`), Target Price (`$12.00`), Walkaway Ceiling (`$13.50`), Currency (`USD`), Payment Terms (`Net 30`).
   * *Purpose:* Defines the negotiation gap ($17.2%) and strict walkaway boundary.

4. **Stage 4: Urgency & Delivery Logistics**
   * *Fields:* Lead Time Needed (`14 Days`), Urgency Level (`Critical - Line Stoppage Risk`), Incoterms (`CIF`).
   * *Purpose:* Detects hidden time traps that suppliers exploit.

5. **Stage 5: Supplier & BATNA**
   * *Fields:* Supplier Name (`Apex Steel Corp`), Relationship (`Existing`), Alternatives (`None`), Stated Reason (`Nickel price hike`).
   * *Purpose:* Identifies the supplier's stated excuse and checks if the buyer has a backup option.

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, here is the input stage. We capture 19 standard questions across 5 stages: Specs, Scale, Financials, Urgency, and Supplier context. These are standard manufacturing questions that take less than 2 minutes to fill out, giving the AI the complete commercial picture."*

---

### Slide 3: Step 2: The Exact Prompt Sent to Gemini

* **Slide Title:** Step 2: AI Processing & The Exact Prompt
* **Subtitle:** Injecting Structured Inputs + Historical Benchmark into the AI
* **Layout:** Code / Text Card Box + Instruction Checklist

#### Slide Content (The Exact Prompt Box):
```text
You are an expert manufacturing procurement negotiation director.
Analyze this negotiation context and provide actionable pre-call advice for the buyer.

[STAGE 1: ITEM & SPECIFICATIONS]
- Item: Cold Rolled Steel Sheet (Grade SS 304)
- Customization: Standard Commodity | Quality: High Precision

[STAGE 2: SCALE & VOLUME]
- Order Batch: 5,000 kg (Quarterly Regular)
- Estimated Annual Volume: 20,000 kg | MOQ Flexibility: Flexible

[STAGE 3: COMMERCIAL BOUNDARIES]
- Supplier Initial Quote: $14.50 USD / kg | Buyer Target Price: $12.00 USD / kg
- Walkaway Ceiling Price: $13.50 USD / kg | Preferred Payment Terms: Net 30 Days

[STAGE 4: URGENCY & DELIVERY]
- Lead Time Needed: 14 Days | Delivery Terms: CIF
- Urgency Level: Critical (Factory production line stoppage risk)

[STAGE 5: SUPPLIER & MARKET CONTEXT]
- Supplier: Apex Steel Corp (Existing Regular Supplier)
- Alternate Backup Quotes Available: None (Single source currently)
- Supplier Stated Price Justification: "Nickel prices increased globally"

[HISTORICAL BENCHMARK CONTEXT (If Found in Past Deals)]
- Past Deal: Rahul bought this from Apex Steel at $12.20/kg on Net 30 terms.

[INSTRUCTIONS]
Return STRICT JSON matching this exact structure:
{
  "buyer_leverage_score": <number 0-100>,
  "leverage_summary": "<1-sentence summary>",
  "weak_points": ["<trap 1>", "<trap 2>"],
  "recommended_opening_offer": <number>,
  "concession_to_trade": "<commercial term to offer for discount>",
  "predicted_supplier_question": "<objection supplier will say>",
  "recommended_response_script": "<word-for-word reply script>"
}
```

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, this is the exact prompt our backend sends to Google Gemini 2.0 Flash. Notice that if a past deal was found, we inject that benchmark directly into the prompt so the AI can instruct the buyer on how to use that past price on the call. The AI returns a strict JSON object with zero hallucinations."*

---

### Slide 4: Step 3: The Output (AI Battlecard & UI)

* **Slide Title:** Step 3: The Output (What the AI Delivers to the Buyer)
* **Subtitle:** 4 Actionable Deliverables Displayed on Screen Before Calling
* **Layout:** Interactive Battlecard UI Mockup

#### Visual Battlecard Card (Include on Slide):
```text
┌────────────────────────────────────────────────────────────────────────┐
│  🎯 PRE-CALL NEGOTIATION BATTLECARD                                    │
│  Item: Cold Rolled Steel Sheet (Grade SS 304)                          │
├────────────────────────────────────────────────────────────────────────┤
│  🏢 Supplier: Apex Steel Corp    │  📦 Batch: 5,000 kg (Quarterly)     │
│  💰 Quote: $14.50/kg             │  🎯 Target: $12.00/kg (Ceiling: $13.50)│
├────────────────────────────────────────────────────────────────────────┤
│  1. BUYER LEVERAGE:  42 / 100 (Moderate-Low)                           │
│     "Urgency limits walkaway power; trade payment terms for price."    │
├────────────────────────────────────────────────────────────────────────┤
│  2. CRITICAL WEAK POINTS (DO NOT REVEAL ON CALL):                      │
│     • Never mention your factory line stoppage deadline.               │
│     • Do not bluff backup quotes if you don't have them in hand.       │
├────────────────────────────────────────────────────────────────────────┤
│  3. RECOMMENDED OPENING MOVE:                                          │
│     • Counter-Offer Anchor: $11.80 / kg                                │
│     • Concession Trade: Offer Net 15 days payment for $1.20/kg cut.    │
├────────────────────────────────────────────────────────────────────────┤
│  4. ANTICIPATED SUPPLIER EXCUSE & EXACT REPLY SCRIPT:                  │
│     Supplier: "Nickel prices jumped 8% this month globally!"           │
│     YOUR SCRIPT: "Nickel is only 8% of SS 304 alloy, which is under    │
│     0.7% total cost. We will commit quarterly if you meet us at $12.20"│
└────────────────────────────────────────────────────────────────────────┘
```

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, within 1.5 seconds, the AI outputs this Pre-Call Battlecard on the buyer's screen. It gives them 4 critical advantages: their Leverage Score (42/100), weak points to hide, an opening anchor price of $11.80, and a word-for-word script that mathematically dismantles the supplier's nickel inflation excuse."*

---

### Slide 5: Step 4: Storage (Single Table, Single Row)

* **Slide Title:** Step 4: Persistence (Single Table, Zero Complexity)
* **Subtitle:** All 19 Inputs + AI Insights Stored Together in PostgreSQL
* **Layout:** SQL Code Snippet + 3 Architectural Benefits

#### Slide Content:
```sql
INSERT INTO negotiations (
    org_id, created_by, status,
    -- 19 Questionnaire Inputs
    item_name, item_grade_spec, customization_level, quality_criticality,
    quantity, unit, purchase_frequency, estimated_annual_volume, moq_flexibility,
    supplier_quote_price, target_price, walkaway_price, currency, preferred_payment_terms,
    required_lead_time_days, urgency_level, incoterms,
    supplier_name, supplier_relationship, has_alternatives, supplier_price_reason,
    -- AI Generated Insights
    buyer_leverage_score, ai_insights
) VALUES (
    :org_id, :user_id, 'in_progress',
    'Cold Rolled Steel Sheet', 'Grade SS 304', 'commodity', 'high_precision',
    5000, 'kg', 'quarterly', 20000, 'flexible',
    14.50, 12.00, 13.50, 'USD', 'net_30',
    14, 'critical', 'CIF',
    'Apex Steel Corp', 'existing_regular', FALSE, 'Nickel prices increased globally',
    42, :ai_output_json
);
```

#### Key Architecture Benefits:
* **Single Master Record:** No messy joins across 10 tables. Everything about this negotiation lives in one living row.
* **Instant Speed:** Lookups take $<5\text{ms}$ using PostgreSQL native indexes.
* **Prepares for Flow 2 & 3:** This row is now ready to log call rounds, calculate savings upon deal closeout, and act as a future benchmark.

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, finally, both the user's 19 inputs and the AI insights are saved together in one clean row in our PostgreSQL negotiations master table. This keeps the architecture ultra-clean, eliminates table joins, and ensures future employees can instantly search and retrieve this deal."*
