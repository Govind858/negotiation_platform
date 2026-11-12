const express = require('express');
const cors = require('cors');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Sample scenarios matching project documentation
const SAMPLE_PRESETS = {
  steel_urgent: {
    name: "Cold Rolled Steel Sheet (Urgent / Single Source)",
    item_name: "Cold Rolled Steel Sheet",
    item_grade_spec: "Grade SS 304",
    customization_level: "commodity",
    quality_criticality: "high_precision",
    quantity: 5000,
    unit: "kg",
    purchase_frequency: "quarterly",
    estimated_annual_volume: 20000,
    moq_flexibility: "flexible",
    supplier_quote_price: 14.50,
    target_price: 12.00,
    walkaway_price: 13.50,
    currency: "USD",
    preferred_payment_terms: "net_30",
    required_lead_time_days: 14,
    urgency_level: "critical",
    incoterms: "CIF",
    supplier_name: "Apex Steel Corp",
    supplier_relationship: "existing_regular",
    has_alternatives: false,
    supplier_price_reason: "Nickel prices increased globally"
  },
  microcontroller_leverage: {
    name: "Automotive Microcontrollers (High Annual Volume)",
    item_name: "32-Bit Microcontroller IC",
    item_grade_spec: "AEC-Q100 Grade 1 Automotive",
    customization_level: "semi_custom",
    quality_criticality: "zero_defect",
    quantity: 25000,
    unit: "units",
    purchase_frequency: "annual_contract",
    estimated_annual_volume: 100000,
    moq_flexibility: "flexible",
    supplier_quote_price: 8.20,
    target_price: 6.50,
    walkaway_price: 7.40,
    currency: "USD",
    preferred_payment_terms: "net_60",
    required_lead_time_days: 45,
    urgency_level: "moderate",
    incoterms: "DDP",
    supplier_name: "SiliconEdge Semiconductor Ltd",
    supplier_relationship: "new_supplier",
    has_alternatives: true,
    supplier_price_reason: "Wafer foundry allocation crunch and inflation"
  },
  injection_mold_sole_source: {
    name: "Custom Die-Cast Aluminum Enclosure (Sole Source)",
    item_name: "Custom Die-Cast Enclosure",
    item_grade_spec: "A380 Alloy - IP67 Rated",
    customization_level: "custom_tooling",
    quality_criticality: "high_precision",
    quantity: 3000,
    unit: "units",
    purchase_frequency: "spot",
    estimated_annual_volume: 3000,
    moq_flexibility: "strict_limit",
    supplier_quote_price: 38.00,
    target_price: 31.00,
    walkaway_price: 35.00,
    currency: "USD",
    preferred_payment_terms: "split_advance",
    required_lead_time_days: 21,
    urgency_level: "critical",
    incoterms: "FOB",
    supplier_name: "PrecisionTool DieWorks",
    supplier_relationship: "sole_certified",
    has_alternatives: false,
    supplier_price_reason: "Tooling re-calibration and short turnaround rush fee"
  }
};

/**
 * Builds the exact LLM prompt specified in negotiation_intake_and_ai_battlecard_engine.md
 */
function buildGeminiPrompt(data) {
  return `You are an expert manufacturing procurement negotiation director.
Analyze this negotiation context and provide actionable pre-call advice for the buyer.

[STAGE 1: ITEM & SPECIFICATIONS]
- Item: ${data.item_name} (${data.item_grade_spec || 'Standard'})
- Customization: ${data.customization_level} | Quality: ${data.quality_criticality}

[STAGE 2: SCALE & VOLUME]
- Order Batch: ${Number(data.quantity).toLocaleString()} ${data.unit} (${data.purchase_frequency})
- Estimated Annual Volume: ${Number(data.estimated_annual_volume || data.quantity).toLocaleString()} ${data.unit} | MOQ Flexibility: ${data.moq_flexibility}

[STAGE 3: COMMERCIAL BOUNDARIES]
- Supplier Initial Quote: ${data.currency} ${Number(data.supplier_quote_price).toFixed(2)} / ${data.unit}
- Buyer Target Price: ${data.currency} ${Number(data.target_price).toFixed(2)} / ${data.unit}
- Walkaway Ceiling Price: ${data.currency} ${Number(data.walkaway_price).toFixed(2)} / ${data.unit}
- Preferred Payment Terms: ${data.preferred_payment_terms}

[STAGE 4: URGENCY & DELIVERY]
- Lead Time Needed: ${data.required_lead_time_days} Days | Delivery Terms: ${data.incoterms}
- Urgency Level: ${data.urgency_level}

[STAGE 5: SUPPLIER & MARKET CONTEXT]
- Supplier: ${data.supplier_name} (${data.supplier_relationship})
- Alternate Backup Quotes Available: ${data.has_alternatives ? 'Yes (Viable alternative quotes present)' : 'None (Single / Sole source currently)'}
- Supplier Stated Price Justification: "${data.supplier_price_reason || 'Standard market rates'}"

[INSTRUCTIONS]
Return STRICT JSON matching this exact structure:
{
  "buyer_leverage_score": <number between 0 and 100>,
  "leverage_summary": "<1-sentence summary of buyer power>",
  "weak_points": [
    "<vulnerability 1 to hide from supplier>",
    "<vulnerability 2 to hide from supplier>"
  ],
  "recommended_opening_offer": <number>,
  "concession_to_trade": "<what commercial term to trade in exchange for a price cut>",
  "predicted_supplier_question": "<what objection the supplier will push back with>",
  "recommended_response_script": "<exact word-for-word response the buyer should reply with>"
}`;
}

/**
 * Intelligent Rule-Based Engine (Fallback & Instant Zero-Key Execution)
 * Accurately models the procurement leverage heuristic formula from project spec.
 */
function generateHeuristicInsights(data) {
  let score = 50;

  // Customization leverage
  if (data.customization_level === 'commodity') score += 12;
  else if (data.customization_level === 'custom_tooling') score -= 18;

  // Volume & recurrence leverage
  if (data.purchase_frequency === 'annual_contract') score += 15;
  else if (data.purchase_frequency === 'quarterly') score += 10;
  else if (data.purchase_frequency === 'spot') score -= 8;

  if (Number(data.estimated_annual_volume) >= Number(data.quantity) * 3) score += 8;
  if (data.moq_flexibility === 'flexible') score += 5;

  // Urgency penalty (critical urgency severely weakens buyer posture)
  if (data.urgency_level === 'critical') score -= 22;
  else if (data.urgency_level === 'low') score += 12;

  // BATNA / Alternatives
  const hasBATNA = data.has_alternatives === true || data.has_alternatives === 'true' || data.has_alternatives === 'multiple_active_quotes';
  if (hasBATNA) score += 25;
  else score -= 20;

  // Supplier relationship
  if (data.supplier_relationship === 'sole_certified') score -= 12;
  else if (data.supplier_relationship === 'new_supplier') score += 8;

  // Clamp score
  score = Math.max(10, Math.min(95, Math.round(score)));

  // Generate dynamic strategic advice
  const quote = Number(data.supplier_quote_price);
  const target = Number(data.target_price);
  const walkaway = Number(data.walkaway_price);

  // Opening offer calculation: anchor lower if leverage is high, or just below target
  let openingOffer;
  if (score >= 65) {
    openingOffer = +(target - (quote - target) * 0.25).toFixed(2);
  } else if (score >= 40) {
    openingOffer = +(target - (quote - target) * 0.10).toFixed(2);
  } else {
    openingOffer = +(target).toFixed(2);
  }
  if (openingOffer <= 0) openingOffer = +(target * 0.95).toFixed(2);

  // Weak points identification
  const weakPoints = [];
  if (data.urgency_level === 'critical') {
    weakPoints.push(`Urgent delivery timeline (${data.required_lead_time_days} days) exposes high stockout risk. Never disclose internal production downtime deadlines.`);
  }
  if (!hasBATNA) {
    weakPoints.push(`No active alternate quotes in hand; avoid hard walkaway ultimatums without prior backup qualification.`);
  }
  if (data.customization_level === 'custom_tooling') {
    weakPoints.push(`Proprietary tooling with ${data.supplier_name} creates tooling re-qualification friction if switching.`);
  }
  if (data.purchase_frequency === 'spot') {
    weakPoints.push(`One-off spot purchase prevents using long-term annual run-rate volume as a pricing lever.`);
  }
  if (weakPoints.length === 0) {
    weakPoints.push(`Maintain poker face on supplier quote validity date; do not rush acceptance.`);
  }

  // Summary
  let summary = '';
  if (score >= 70) {
    summary = `Strong buyer position driven by high annual volume and competitive alternatives. Aggressively anchor near ${data.currency} ${openingOffer}.`;
  } else if (score >= 45) {
    summary = `Balanced to moderate leverage; urgency and single-sourcing limit hard bluffing, but annual repeat volume offers terms trading leverage.`;
  } else {
    summary = `Supplier-dominant leverage due to tight delivery urgency and lack of qualified backup sources. Focus on payment terms and volume bundling.`;
  }

  // Concession to trade
  let concession = '';
  if (data.preferred_payment_terms === 'net_30' || data.preferred_payment_terms === 'net_60') {
    concession = `Offer accelerated payment terms (Net 15 days or early settlement discount) in exchange for locking price at ${data.currency} ${target.toFixed(2)}.`;
  } else if (data.moq_flexibility === 'flexible') {
    concession = `Offer to increase immediate batch size by 20% in exchange for reaching your ${data.currency} ${target.toFixed(2)} target.`;
  } else {
    concession = `Offer multi-quarter repeat purchasing visibility in exchange for waiving supplemental surcharges.`;
  }

  // Predicted objection & scripted counter
  const reason = (data.supplier_price_reason || '').toLowerCase();
  let predictedQuestion = '';
  let responseScript = '';

  if (reason.includes('nickel') || reason.includes('metal') || reason.includes('raw material')) {
    predictedQuestion = `"${data.supplier_price_reason || 'Raw material index jumped globally'}, how can we meet ${data.currency} ${target.toFixed(2)}?"`;
    responseScript = `"The underlying commodity index only accounts for a portion of the total component cost breakdown. A standard index fluctuation impacts net landed manufacturing cost by less than 1.5%. We are prepared to commit to our ${data.purchase_frequency} volume of ${Number(data.estimated_annual_volume || data.quantity).toLocaleString()} ${data.unit} if you meet us at ${data.currency} ${target.toFixed(2)}."`;
  } else if (reason.includes('allocation') || reason.includes('crunch') || reason.includes('chip') || reason.includes('wafer')) {
    predictedQuestion = `"Capacity allocation is severely constrained across the supply chain, so our quote of ${data.currency} ${quote.toFixed(2)} is standard."`;
    responseScript = `"We recognize tier-1 fab capacity cycles. However, our forecast of ${Number(data.estimated_annual_volume || data.quantity).toLocaleString()} ${data.unit} represents predictable baseline capacity utilization for your lines. Lock in ${data.currency} ${target.toFixed(2)} and we will issue binding rolling forecasts."`;
  } else {
    predictedQuestion = `"Our quote of ${data.currency} ${quote.toFixed(2)} reflects our current production costs and delivery schedule for this specification."`;
    responseScript = `"We value ${data.supplier_name}'s quality, but our benchmark for ${data.item_name} across the industry is closer to ${data.currency} ${target.toFixed(2)}. In exchange for your commercial alignment on price, we can confirm our ${data.purchase_frequency} repeat schedule."`;
  }

  return {
    buyer_leverage_score: score,
    leverage_summary: summary,
    weak_points: weakPoints,
    recommended_opening_offer: openingOffer,
    concession_to_trade: concession,
    predicted_supplier_question: predictedQuestion,
    recommended_response_script: responseScript,
    engine_used: "ProcureAI Heuristic Engine (Deterministic & Instant)"
  };
}

/**
 * Calls Live Gemini via Google's official REST API
 * Supports active models with automatic fallback
 */
async function callGemini2Flash(apiKey, payload) {
  const prompt = buildGeminiPrompt(payload);
  const models = ['gemini-3-flash-preview', 'gemini-3.8-flash', 'gemini-2.5-flash-lite', 'gemini-flash-latest'];

  const requestBody = {
    contents: [
      {
        parts: [
          {
            text: prompt
          }
        ]
      }
    ],
    generationConfig: {
      temperature: 0.2,
      responseMimeType: "application/json"
    }
  };

  let lastError = null;

  for (const model of models) {
    try {
      const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(requestBody)
      });

      if (!response.ok) {
        const errorText = await response.text();
        lastError = new Error(`Model ${model} [${response.status}]: ${errorText}`);
        continue;
      }

      const data = await response.json();
      let rawText = data.candidates?.[0]?.content?.parts?.[0]?.text;
      if (!rawText) {
        lastError = new Error(`Model ${model} returned empty response`);
        continue;
      }

      // Clean markdown code fences if present
      rawText = rawText.trim();
      if (rawText.startsWith('```json')) {
        rawText = rawText.replace(/^```json\s*/, '').replace(/\s*```$/, '');
      } else if (rawText.startsWith('```')) {
        rawText = rawText.replace(/^```\s*/, '').replace(/\s*```$/, '');
      }

      const parsed = JSON.parse(rawText);
      return {
        ...parsed,
        engine_used: `Google Gemini (${model} Live AI)`
      };
    } catch (err) {
      lastError = err;
    }
  }

  throw lastError || new Error("Failed to call Gemini API across available models");
}

/**
 * Calculates financial metrics for the negotiation
 */
function calculateDealMetrics(data) {
  const quote = Number(data.supplier_quote_price) || 0;
  const target = Number(data.target_price) || 0;
  const walkaway = Number(data.walkaway_price) || 0;
  const quantity = Number(data.quantity) || 1;
  const annualVol = Number(data.estimated_annual_volume) || quantity;

  const gapAmount = +(quote - target).toFixed(2);
  const gapPercentage = quote > 0 ? +((gapAmount / quote) * 100).toFixed(1) : 0;
  const totalQuoteValue = +(quote * quantity).toFixed(2);
  const batchSavings = +(gapAmount * quantity).toFixed(2);
  const annualSavings = +(gapAmount * annualVol).toFixed(2);

  return {
    currency: data.currency || 'USD',
    quote_price: quote,
    target_price: target,
    walkaway_price: walkaway,
    unit: data.unit || 'units',
    gap_amount: gapAmount,
    gap_percentage: gapPercentage,
    total_quote_value: totalQuoteValue,
    batch_potential_savings: batchSavings,
    annual_potential_savings: annualSavings
  };
}

// -----------------------------------------------------------------------------
// ROUTES
// -----------------------------------------------------------------------------

// Presets endpoint
app.get('/api/negotiation/presets', (req, res) => {
  res.json({ success: true, presets: SAMPLE_PRESETS });
});

// Health check
app.get('/api/health', (req, res) => {
  const hasEnvKey = Boolean(process.env.GEMINI_API_KEY || process.env.GOOGLE_API_KEY);
  res.json({
    status: 'ok',
    service: 'ProcureAI Negotiation Intelligence Engine',
    gemini_key_configured: hasEnvKey,
    timestamp: new Date().toISOString()
  });
});

/**
 * CORE API: POST /api/negotiation/insights (and alias /api/insights)
 * Generates the AI pre-call battlecard from the 19 questionnaire fields
 */
const insightsHandler = async (req, res) => {
  const startTime = Date.now();
  try {
    const data = req.body;

    // Basic required field validations
    if (!data.item_name || !data.supplier_quote_price || !data.target_price) {
      return res.status(400).json({
        success: false,
        error: "Missing required procurement fields: item_name, supplier_quote_price, target_price are mandatory."
      });
    }

    // Determine API Key priority: request body -> header -> process.env
    const apiKey = data.apiKey ||
                   req.headers['x-gemini-api-key'] ||
                   process.env.GEMINI_API_KEY ||
                   process.env.GOOGLE_API_KEY;

    let aiResult;
    let usedLiveGemini = false;
    let geminiError = null;

    if (apiKey && apiKey.trim().length > 5) {
      try {
        aiResult = await callGemini2Flash(apiKey.trim(), data);
        usedLiveGemini = true;
      } catch (err) {
        console.warn(`[ProcureAI] Gemini API failed (${err.message}). Falling back to heuristic engine.`);
        geminiError = err.message;
        aiResult = generateHeuristicInsights(data);
      }
    } else {
      aiResult = generateHeuristicInsights(data);
    }

    // Attach calculated financial metrics
    const dealMetrics = calculateDealMetrics(data);

    // Build unified, strict response matching project spec
    const responsePayload = {
      success: true,
      data: {
        item_name: data.item_name,
        supplier_name: data.supplier_name || 'Target Supplier',
        buyer_leverage_score: aiResult.buyer_leverage_score,
        leverage_summary: aiResult.leverage_summary,
        weak_points: aiResult.weak_points || [],
        recommended_opening_offer: aiResult.recommended_opening_offer,
        concession_to_trade: aiResult.concession_to_trade,
        predicted_supplier_question: aiResult.predicted_supplier_question,
        recommended_response_script: aiResult.recommended_response_script,
        deal_metrics: dealMetrics
      },
      meta: {
        engine: aiResult.engine_used,
        live_gemini: usedLiveGemini,
        fallback_notice: geminiError ? `Live Gemini failed (${geminiError}). Served via built-in Procurement Engine.` : null,
        execution_time_ms: Date.now() - startTime,
        created_at: new Date().toISOString()
      }
    };

    res.json(responsePayload);
  } catch (error) {
    console.error('[ProcureAI] Error generating insights:', error);
    res.status(500).json({
      success: false,
      error: error.message || 'Internal server error processing negotiation insights'
    });
  }
};

app.post('/api/negotiation/insights', insightsHandler);
app.post('/api/insights', insightsHandler);

// Fallback to index.html for client-side routing
app.use((req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start Server (only when run directly or in regular container environments like Render)
if (!process.env.VERCEL) {
  app.listen(PORT, () => {
    console.log(`=======================================================`);
    console.log(`⚡ ProcureAI Negotiation Engine Server running!`);
    console.log(`🌐 Local Web UI: http://localhost:${PORT}`);
    console.log(`📡 Single API:   POST http://localhost:${PORT}/api/negotiation/insights`);
    console.log(`=======================================================`);
  });
}

module.exports = app;
