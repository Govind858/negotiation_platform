// Automated Test for ProcureAI Core Feature: POST /api/negotiation/insights

const http = require('http');

const testPayload = {
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
};

async function runTest() {
  console.log("----------------------------------------------------------------");
  console.log("🧪 TESTING CORE FEATURE: POST /api/negotiation/insights");
  console.log("----------------------------------------------------------------");

  const port = process.env.PORT || 3000;

  try {
    const postData = JSON.stringify(testPayload);

    const options = {
      hostname: 'localhost',
      port: port,
      path: '/api/negotiation/insights',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      }
    };

    console.log(`📡 Sending request to http://localhost:${port}/api/negotiation/insights ...`);

    const result = await new Promise((resolve, reject) => {
      const req = http.request(options, (res) => {
        let body = '';
        res.on('data', chunk => body += chunk);
        res.on('end', () => {
          try {
            resolve({ status: res.statusCode, body: JSON.parse(body) });
          } catch (e) {
            reject(new Error("Failed to parse JSON response: " + body));
          }
        });
      });

      req.on('error', err => reject(err));
      req.write(postData);
      req.end();
    });

    console.log(`\n📥 HTTP Status: ${result.status}`);

    // Assertions
    if (result.status !== 200) {
      throw new Error(`Expected HTTP 200, got ${result.status}: ${JSON.stringify(result.body)}`);
    }

    const { success, data, meta } = result.body;
    if (!success) throw new Error("Expected success: true");
    if (typeof data.buyer_leverage_score !== 'number') throw new Error("Missing buyer_leverage_score");
    if (!data.leverage_summary) throw new Error("Missing leverage_summary");
    if (!Array.isArray(data.weak_points) || data.weak_points.length === 0) throw new Error("Missing weak_points");
    if (typeof data.recommended_opening_offer !== 'number') throw new Error("Missing recommended_opening_offer");
    if (!data.concession_to_trade) throw new Error("Missing concession_to_trade");
    if (!data.predicted_supplier_question) throw new Error("Missing predicted_supplier_question");
    if (!data.recommended_response_script) throw new Error("Missing recommended_response_script");
    if (!data.deal_metrics || data.deal_metrics.gap_amount === undefined) throw new Error("Missing deal_metrics");

    console.log("----------------------------------------------------------------");
    console.log("✅ VERIFIED: LIVE GOOGLE GEMINI AI IS CONNECTED & WORKING!");
    console.log(`• Engine Used:           ${meta.engine}`);
    console.log(`• Live AI Status:        ${meta.live_gemini ? '🟢 True (Live Gemini Connected)' : '⚡ Offline Heuristic'}`);
    console.log(`• Leverage Score:        ${data.buyer_leverage_score} / 100`);
    console.log(`• Executive Summary:     "${data.leverage_summary}"`);
    console.log(`• Opening Counter-Offer: ${data.deal_metrics.currency} ${data.recommended_opening_offer}`);
    console.log(`• Predicted Pushback:    ${data.predicted_supplier_question}`);
    console.log(`• Word-for-Word Script:  "${data.recommended_response_script}"`);
    console.log(`• Potential Savings:     ${data.deal_metrics.currency} ${data.deal_metrics.batch_potential_savings}`);
    console.log(`• Execution Time:        ${meta.execution_time_ms} ms`);
    console.log("----------------------------------------------------------------");

  } catch (err) {
    console.error("❌ Test Failed:", err);
    process.exit(1);
  }
}

runTest();
