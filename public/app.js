// ProcureAI Client Controller

const PRESETS = {
  steel_urgent: {
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
    has_alternatives: "false",
    supplier_price_reason: "Nickel prices increased globally"
  },
  microcontroller_leverage: {
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
    has_alternatives: "true",
    supplier_price_reason: "Wafer foundry allocation crunch and inflation"
  },
  injection_mold_sole_source: {
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
    has_alternatives: "false",
    supplier_price_reason: "Tooling re-calibration and short turnaround rush fee"
  }
};

let currentResponseData = null;

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  loadScenarioPreset('steel_urgent');
  updateApiKeyDisplay();
  checkApiHealth();

  // Shortcut Ctrl+Enter or Cmd+Enter to submit
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      const submitBtn = document.getElementById('submit-btn');
      if (submitBtn) submitBtn.click();
    }
  });

  // Dynamic cURL update on input change
  const form = document.getElementById('intake-form');
  form.addEventListener('input', updateCurlViewerFromForm);
  form.addEventListener('change', updateCurlViewerFromForm);
});

/**
 * Checks server health and Gemini configuration status
 */
async function checkApiHealth() {
  try {
    const res = await fetch('/api/health');
    const data = await res.json();
    if (data.status === 'ok') {
      console.log('✅ ProcureAI API Server is online:', data);
    }
  } catch (err) {
    console.warn('API health check error:', err);
  }
}

/**
 * Loads a scenario preset into the 19 form fields
 */
function loadScenarioPreset(presetKey) {
  const preset = PRESETS[presetKey];
  if (!preset) return;

  // Highlight active preset button
  document.querySelectorAll('.preset-btn').forEach(b => {
    b.classList.remove('bg-emerald-500/20', 'text-emerald-300');
    b.classList.add('text-slate-300');
  });

  if (presetKey === 'steel_urgent') {
    document.getElementById('preset-btn-steel')?.classList.add('bg-emerald-500/20', 'text-emerald-300');
  } else if (presetKey === 'microcontroller_leverage') {
    document.getElementById('preset-btn-micro')?.classList.add('bg-emerald-500/20', 'text-emerald-300');
  } else if (presetKey === 'injection_mold_sole_source') {
    document.getElementById('preset-btn-die')?.classList.add('bg-emerald-500/20', 'text-emerald-300');
  }

  // Populate form fields
  for (const [key, value] of Object.entries(preset)) {
    const el = document.getElementById(key);
    if (el) {
      el.value = value;
    }
  }

  updateCurlViewerFromForm();
}

/**
 * Reads form data as an object
 */
function getFormData() {
  const fields = [
    'item_name', 'item_grade_spec', 'customization_level', 'quality_criticality',
    'quantity', 'unit', 'purchase_frequency', 'estimated_annual_volume', 'moq_flexibility',
    'supplier_quote_price', 'target_price', 'walkaway_price', 'currency', 'preferred_payment_terms',
    'required_lead_time_days', 'urgency_level', 'incoterms',
    'supplier_name', 'supplier_relationship', 'has_alternatives', 'supplier_price_reason'
  ];

  const payload = {};
  fields.forEach(f => {
    const el = document.getElementById(f);
    if (!el) return;
    if (f === 'has_alternatives') {
      payload[f] = el.value === 'true';
    } else if (['quantity', 'estimated_annual_volume', 'supplier_quote_price', 'target_price', 'walkaway_price', 'required_lead_time_days'].includes(f)) {
      payload[f] = el.value ? Number(el.value) : undefined;
    } else {
      payload[f] = el.value.trim();
    }
  });

  // Attach optional API key from localStorage if set
  const storedKey = localStorage.getItem('procureai_gemini_key');
  if (storedKey && storedKey.trim()) {
    payload.apiKey = storedKey.trim();
  }

  return payload;
}

/**
 * Submits the single API: POST /api/negotiation/insights
 */
async function handleFormSubmit(event) {
  if (event) event.preventDefault();

  const payload = getFormData();
  if (!payload.item_name || !payload.supplier_quote_price || !payload.target_price) {
    showToast('⚠️ Please enter Item Name, Supplier Quote, and Target Price.', 'error');
    return;
  }

  // Switch right pane to loading state
  document.getElementById('empty-state').classList.add('hidden');
  document.getElementById('battlecard-container').classList.add('hidden');
  document.getElementById('loading-state').classList.remove('hidden');

  const submitBtn = document.getElementById('submit-btn');
  const submitSpinner = document.getElementById('submit-spinner');
  const submitIcon = document.getElementById('submit-icon');
  const submitText = document.getElementById('submit-text');

  submitBtn.disabled = true;
  submitSpinner.classList.remove('hidden');
  submitIcon.classList.add('hidden');
  submitText.textContent = 'Generating Battlecard...';

  try {
    const startTime = performance.now();
    const response = await fetch('/api/negotiation/insights', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    const elapsed = Math.round(performance.now() - startTime);

    if (!response.ok) {
      const errData = await response.json().catch(() => ({}));
      throw new Error(errData.error || `Server returned ${response.status}`);
    }

    const result = await response.json();
    currentResponseData = result;

    // Render Battlecard
    renderBattlecard(result, elapsed);

    // Update raw JSON tab
    document.getElementById('json-viewer').textContent = JSON.stringify(result, null, 2);

    // Switch to battlecard tab
    switchTab('battlecard');

    showToast('⚡ AI Battlecard Generated Successfully!');
  } catch (error) {
    console.error('Error fetching insights:', error);
    showToast(`❌ Error: ${error.message}`, 'error');
    document.getElementById('loading-state').classList.add('hidden');
    document.getElementById('empty-state').classList.remove('hidden');
  } finally {
    submitBtn.disabled = false;
    submitSpinner.classList.add('hidden');
    submitIcon.classList.remove('hidden');
    submitText.textContent = 'Generate AI Pre-Call Battlecard';
  }
}

/**
 * Renders the returned AI strategy into the Battlecard UI
 */
function renderBattlecard(result, clientElapsedMs) {
  const data = result.data;
  const meta = result.meta || {};

  // Header
  document.getElementById('card-item-name').textContent = data.item_name || 'Procurement Item';
  document.getElementById('card-supplier-subtitle').textContent = `Supplier: ${data.supplier_name || 'Target Supplier'}`;

  // Engine badge
  const engineBadge = document.getElementById('card-engine-badge');
  if (meta.live_gemini) {
    engineBadge.textContent = '🟢 Google Gemini 2.0 Flash (Live)';
    engineBadge.className = 'text-[10px] font-mono px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
  } else {
    engineBadge.textContent = '⚡ ProcureAI Engine (Deterministic)';
    engineBadge.className = 'text-[10px] font-mono px-2 py-0.5 rounded-full bg-teal-500/20 text-teal-300 border border-teal-500/30';
  }

  // Execution Time
  const execTime = meta.execution_time_ms || clientElapsedMs;
  document.getElementById('card-exec-time').textContent = `⚡ ${execTime} ms`;

  // Pricing numbers
  const metrics = data.deal_metrics || {};
  const cur = metrics.currency || '$';
  const unit = metrics.unit || 'unit';

  document.getElementById('card-quote-price').textContent = `${cur} ${Number(metrics.quote_price).toFixed(2)} / ${unit}`;
  document.getElementById('card-target-price').textContent = `${cur} ${Number(metrics.target_price).toFixed(2)} / ${unit}`;
  document.getElementById('card-walkaway-price').textContent = `${cur} ${Number(metrics.walkaway_price || metrics.target_price * 1.1).toFixed(2)} / ${unit}`;

  document.getElementById('card-gap-pct').textContent = `${metrics.gap_percentage}% below quote`;
  document.getElementById('card-savings').textContent = `${cur} ${Number(metrics.batch_potential_savings || 0).toLocaleString()}`;
  document.getElementById('card-annual-savings').textContent = `${cur} ${Number(metrics.annual_potential_savings || 0).toLocaleString()} / yr`;

  // Leverage Score & Meter
  const score = Number(data.buyer_leverage_score) || 50;
  const leverageBadge = document.getElementById('card-leverage-badge');
  const leverageBar = document.getElementById('card-leverage-bar');

  leverageBar.style.width = `${score}%`;

  if (score >= 65) {
    leverageBadge.className = 'px-2.5 py-1 rounded-full text-xs font-bold border border-emerald-500/40 bg-emerald-500/10 text-emerald-400';
    leverageBadge.textContent = `${score} / 100 • High Buyer Leverage`;
    leverageBar.className = 'h-full rounded-full transition-all duration-700 bg-emerald-400';
  } else if (score >= 40) {
    leverageBadge.className = 'px-2.5 py-1 rounded-full text-xs font-bold border border-amber-500/40 bg-amber-500/10 text-amber-400';
    leverageBadge.textContent = `${score} / 100 • Moderate Leverage`;
    leverageBar.className = 'h-full rounded-full transition-all duration-700 bg-amber-400';
  } else {
    leverageBadge.className = 'px-2.5 py-1 rounded-full text-xs font-bold border border-rose-500/40 bg-rose-500/10 text-rose-400';
    leverageBadge.textContent = `${score} / 100 • Low Buyer Leverage`;
    leverageBar.className = 'h-full rounded-full transition-all duration-700 bg-rose-500';
  }

  // Leverage Summary
  document.getElementById('card-leverage-summary').textContent = data.leverage_summary || 'Analysis complete.';

  // Weak points list
  const weakList = document.getElementById('card-weak-points');
  weakList.innerHTML = '';
  if (Array.isArray(data.weak_points) && data.weak_points.length > 0) {
    data.weak_points.forEach(point => {
      const li = document.createElement('li');
      li.className = 'flex items-start gap-2 bg-slate-950/60 p-2.5 rounded-xl border border-rose-900/30';
      li.innerHTML = `<span class="text-rose-400 mt-0.5">•</span><span>${escapeHtml(point)}</span>`;
      weakList.appendChild(li);
    });
  } else {
    weakList.innerHTML = `<li class="text-slate-400 italic">No critical weak points flagged.</li>`;
  }

  // Opening counter-offer & concession
  document.getElementById('card-opening-offer').textContent = `${cur} ${Number(data.recommended_opening_offer).toFixed(2)} / ${unit}`;
  document.getElementById('card-concession').textContent = data.concession_to_trade || 'Trade payment terms for unit price cuts.';

  // Objection & reply script
  document.getElementById('card-predicted-question').textContent = data.predicted_supplier_question || 'Supplier cost justification.';
  document.getElementById('card-response-script').textContent = data.recommended_response_script || 'Standard counter script.';

  // Show battlecard container
  document.getElementById('loading-state').classList.add('hidden');
  document.getElementById('empty-state').classList.add('hidden');
  document.getElementById('battlecard-container').classList.remove('hidden');
}

/**
 * Tab switching
 */
function switchTab(tabKey) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.add('hidden'));
  document.querySelectorAll('.tab-btn').forEach(b => {
    b.classList.remove('bg-emerald-500/20', 'text-emerald-400');
    b.classList.add('text-slate-400');
  });

  const activePanel = document.getElementById(`tab-content-${tabKey}`);
  const activeBtn = document.getElementById(`tab-btn-${tabKey}`);

  if (activePanel) activePanel.classList.remove('hidden');
  if (activeBtn) {
    activeBtn.classList.remove('text-slate-400');
    activeBtn.classList.add('bg-emerald-500/20', 'text-emerald-400');
  }
}

/**
 * Copies the script text to clipboard
 */
function copyScriptToClipboard() {
  const scriptEl = document.getElementById('card-response-script');
  if (!scriptEl) return;
  navigator.clipboard.writeText(scriptEl.textContent.trim());
  showToast('📋 Rebuttal script copied to clipboard!');
}

/**
 * Copies raw JSON response to clipboard
 */
function copyJsonToClipboard() {
  const jsonViewer = document.getElementById('json-viewer');
  if (!jsonViewer) return;
  navigator.clipboard.writeText(jsonViewer.textContent);
  showToast('📋 JSON copied to clipboard!');
}

/**
 * Copies cURL command to clipboard
 */
function copyCurlToClipboard() {
  const curlViewer = document.getElementById('curl-viewer');
  if (!curlViewer) return;
  navigator.clipboard.writeText(curlViewer.textContent);
  showToast('📋 cURL command copied to clipboard!');
}

/**
 * Copies entire strategy to clipboard as formatted text
 */
function copyFullResponse() {
  if (!currentResponseData) {
    showToast('⚠️ Generate a battlecard first!', 'error');
    return;
  }
  const d = currentResponseData.data;
  const text = `🎯 PRE-CALL NEGOTIATION BATTLECARD: ${d.item_name}
Supplier: ${d.supplier_name}
Buyer Leverage Score: ${d.buyer_leverage_score}/100 (${d.leverage_summary})
Opening Offer: ${d.recommended_opening_offer}
Concession Trade: ${d.concession_to_trade}
Predicted Supplier Objection: ${d.predicted_supplier_question}
Recommended Reply Script: ${d.recommended_response_script}`;

  navigator.clipboard.writeText(text);
  showToast('📋 Full battlecard summary copied!');
}

/**
 * Prints the battlecard
 */
function printBattlecard() {
  if (document.getElementById('battlecard-container').classList.contains('hidden')) {
    showToast('⚠️ Generate a battlecard first to export!', 'error');
    return;
  }
  window.print();
}

/**
 * Updates the cURL terminal snippet based on current form inputs
 */
function updateCurlViewerFromForm() {
  const curlEl = document.getElementById('curl-viewer');
  if (!curlEl) return;

  const payload = getFormData();
  delete payload.apiKey; // Don't expose key in sample curl unless desired

  const curlText = `curl -X POST http://localhost:3000/api/negotiation/insights \\
  -H "Content-Type: application/json" \\
  -d '${JSON.stringify(payload, null, 2)}'`;

  curlEl.textContent = curlText;
}

/**
 * Resets the form to empty values
 */
function resetForm() {
  document.getElementById('intake-form').reset();
  document.getElementById('battlecard-container').classList.add('hidden');
  document.getElementById('loading-state').classList.add('hidden');
  document.getElementById('empty-state').classList.remove('hidden');
  currentResponseData = null;
  updateCurlViewerFromForm();
  showToast('Form reset.');
}

/**
 * API Key Modal Management
 */
function openApiKeyModal() {
  const stored = localStorage.getItem('procureai_gemini_key') || '';
  document.getElementById('apiKeyInput').value = stored;
  document.getElementById('apiKeyModal').classList.remove('hidden');
}

function closeApiKeyModal() {
  document.getElementById('apiKeyModal').classList.add('hidden');
}

function saveApiKey() {
  const val = document.getElementById('apiKeyInput').value.trim();
  if (val) {
    localStorage.setItem('procureai_gemini_key', val);
    showToast('🔑 Gemini API key saved for this browser session!');
  } else {
    localStorage.removeItem('procureai_gemini_key');
    showToast('Using default / built-in Procurement Engine.');
  }
  closeApiKeyModal();
  updateApiKeyDisplay();
}

function clearApiKey() {
  localStorage.removeItem('procureai_gemini_key');
  document.getElementById('apiKeyInput').value = '';
  showToast('API key cleared.');
  closeApiKeyModal();
  updateApiKeyDisplay();
}

function updateApiKeyDisplay() {
  const stored = localStorage.getItem('procureai_gemini_key');
  const textEl = document.getElementById('apiKeyStatusText');
  if (!textEl) return;
  if (stored && stored.length > 5) {
    textEl.textContent = 'Gemini 2.0 Live Key Active';
  } else {
    textEl.textContent = 'Dual Engine (Live / Built-in)';
  }
}

/**
 * Toast Notification Helper
 */
function showToast(message, type = 'success') {
  const toast = document.getElementById('toast');
  const toastMsg = document.getElementById('toast-message');
  const toastIcon = document.getElementById('toast-icon');

  toastMsg.textContent = message;
  toastIcon.textContent = type === 'error' ? '❌' : '✓';
  toast.className = `fixed bottom-6 right-6 z-50 transform translate-y-0 opacity-100 transition-all duration-300 bg-slate-900 border ${
    type === 'error' ? 'border-rose-500/60 text-rose-200' : 'border-emerald-500/60 text-white'
  } px-4 py-2.5 rounded-xl shadow-2xl text-xs flex items-center gap-2`;

  setTimeout(() => {
    toast.className = 'fixed bottom-6 right-6 z-50 transform translate-y-20 opacity-0 transition-all duration-300 bg-slate-900 border border-emerald-500/50 text-white px-4 py-2.5 rounded-xl shadow-2xl text-xs flex items-center gap-2 pointer-events-none';
  }, 3500);
}

function scrollToDocs() {
  switchTab('curl');
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/[&<>"']/g, function(m) {
    return {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#039;'
    }[m];
  });
}
