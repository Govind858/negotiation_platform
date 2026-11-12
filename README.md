# ⚡ ProcureAI — Core AI Strategy Battlecard Engine

> **AI-Powered Manufacturing Procurement Negotiation Intelligence & Institutional Memory**

This repository contains the standalone core feature implementation of **ProcureAI**:
1. **The Single REST API**: `POST /api/negotiation/insights`
2. **AI Integration**: Dual-engine integration supporting **Google Gemini 2.0 Flash** with a built-in zero-dependency deterministic procurement heuristic fallback.
3. **Interactive Sample Web Interface**: A modern dark-themed web dashboard where buyers can enter 19 procurement parameters (or load 1-click deal scenarios), view buyer leverage scores, see concealed vulnerabilities, review commercial concession trades, and copy word-for-word counter-scripts.

---

## 🚀 Quick Start

### 1. Prerequisites
- **Node.js**: v18+ (verified on Node.js v24)
- **npm**: v9+

### 2. Start the Server
The server is currently running locally, or you can start it anytime using:

```bash
# Start server
npm start
```

Once started, open your browser at:
👉 **`http://localhost:3000`**

---

## 📡 The Single API Endpoint Specification

### `POST /api/negotiation/insights`
*(Alias: `POST /api/insights`)*

Takes the 19 procurement intake parameters and returns structured pre-call strategy JSON.

#### Request Headers:
```http
Content-Type: application/json
x-gemini-api-key: <optional_gemini_api_key>
```

#### Request Body (JSON):
```json
{
  "item_name": "Cold Rolled Steel Sheet",
  "item_grade_spec": "Grade SS 304",
  "customization_level": "commodity",
  "quality_criticality": "high_precision",
  "quantity": 5000,
  "unit": "kg",
  "purchase_frequency": "quarterly",
  "estimated_annual_volume": 20000,
  "moq_flexibility": "flexible",
  "supplier_quote_price": 14.50,
  "target_price": 12.00,
  "walkaway_price": 13.50,
  "currency": "USD",
  "preferred_payment_terms": "net_30",
  "required_lead_time_days": 14,
  "urgency_level": "critical",
  "incoterms": "CIF",
  "supplier_name": "Apex Steel Corp",
  "supplier_relationship": "existing_regular",
  "has_alternatives": false,
  "supplier_price_reason": "Nickel prices increased globally"
}
```

#### Response Body (200 OK):
```json
{
  "success": true,
  "data": {
    "item_name": "Cold Rolled Steel Sheet",
    "supplier_name": "Apex Steel Corp",
    "buyer_leverage_score": 43,
    "leverage_summary": "Supplier-dominant leverage due to tight delivery urgency and lack of qualified backup sources. Focus on payment terms and volume bundling.",
    "weak_points": [
      "Urgent delivery timeline (14 days) exposes high stockout risk. Never disclose internal production downtime deadlines.",
      "No active alternate quotes in hand; avoid hard walkaway ultimatums without prior backup qualification."
    ],
    "recommended_opening_offer": 11.75,
    "concession_to_trade": "Offer accelerated payment terms (Net 15 days or early settlement discount) in exchange for locking price at USD 12.00.",
    "predicted_supplier_question": "\"Nickel prices increased globally, how can we meet USD 12.00?\"",
    "recommended_response_script": "\"The underlying commodity index only accounts for a portion of the total component cost breakdown. A standard index fluctuation impacts net landed manufacturing cost by less than 1.5%. We are prepared to commit to our quarterly volume of 20,000 kg if you meet us at USD 12.00.\"",
    "deal_metrics": {
      "currency": "USD",
      "quote_price": 14.5,
      "target_price": 12,
      "walkaway_price": 13.5,
      "unit": "kg",
      "gap_amount": 2.5,
      "gap_percentage": 17.2,
      "total_quote_value": 72500,
      "batch_potential_savings": 12500,
      "annual_potential_savings": 50000
    }
  },
  "meta": {
    "engine": "ProcureAI Heuristic Engine (Deterministic & Instant)",
    "live_gemini": false,
    "fallback_notice": null,
    "execution_time_ms": 107,
    "created_at": "2026-11-12T13:20:51.373Z"
  }
}
```

---

## 🧪 Testing the API from Terminal

You can test the endpoint using `curl`:

```bash
curl -X POST http://localhost:3000/api/negotiation/insights \
  -H "Content-Type: application/json" \
  -d '{
    "item_name": "Cold Rolled Steel Sheet",
    "item_grade_spec": "Grade SS 304",
    "customization_level": "commodity",
    "quality_criticality": "high_precision",
    "quantity": 5000,
    "unit": "kg",
    "purchase_frequency": "quarterly",
    "estimated_annual_volume": 20000,
    "moq_flexibility": "flexible",
    "supplier_quote_price": 14.50,
    "target_price": 12.00,
    "walkaway_price": 13.50,
    "currency": "USD",
    "preferred_payment_terms": "net_30",
    "required_lead_time_days": 14,
    "urgency_level": "critical",
    "incoterms": "CIF",
    "supplier_name": "Apex Steel Corp",
    "supplier_relationship": "existing_regular",
    "has_alternatives": false,
    "supplier_price_reason": "Nickel prices increased globally"
  }'
```

Or run the automated test suite:
```bash
npm test
```

---

## 🖥️ Web Interface Features

Visit `http://localhost:3000` to access the interactive dashboard:
1. **1-Click Deal Presets**:
   - 🔩 **Steel Sheet Deal**: High urgency, no BATNA (Moderate-Low leverage).
   - ⚙️ **Microcontroller Contract**: High annual volume, multi-source (High leverage).
   - 🧪 **Die-Cast Tooling**: Proprietary tooling, sole source (Low leverage).
2. **Visual Leverage Gauge**: Dynamic 0–100 score indicator with color-coded posture assessment.
3. **Weak Point Radar**: Pinpoints vulnerabilities the buyer must never leak on a negotiation call.
4. **Dialogue & Script Card**: Word-for-word counter-script with a 1-click **"Copy Script"** button.
5. **Raw JSON Inspector**: View the pure type-safe output payload.
6. **Print / Export PDF**: Clean, print-friendly layout for pre-call briefing sheets.
7. **Gemini Key Configuration**: Allows testing with live Google Gemini 2.0 Flash or switching to the built-in deterministic engine.
