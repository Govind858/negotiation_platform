-- =============================================================================
-- SAMPLE PROCUREMENT NEGOTIATION DATASET
-- Demonstrates: Deal WON, Deal LOST (Walkaway), and IN-PROGRESS (Multi-round)
-- =============================================================================

-- 1. Create a Sample Organization (Tenant)
INSERT INTO organizations (id, company_name, industry)
VALUES ('00000000-0000-0000-0000-000000000001', 'Precision Forge & Auto Ltd', 'Automotive & Heavy Machinery')
ON CONFLICT (id) DO NOTHING;

-- 2. Create Sample Staff Users (Admin & Negotiators)
INSERT INTO users (id, org_id, email, password_hash, full_name, role)
VALUES 
  ('11111111-1111-1111-1111-111111111111', '00000000-0000-0000-0000-000000000001', 'admin@precisionforge.com', '$2b$10$e8w...dummyhash', 'Vikram Malhotra', 'admin'),
  ('22222222-2222-2222-2222-222222222222', '00000000-0000-0000-0000-000000000001', 'rahul.v@precisionforge.com', '$2b$10$e8w...dummyhash', 'Rahul Verma', 'negotiator'),
  ('33333333-3333-3333-3333-333333333333', '00000000-0000-0000-0000-000000000001', 'sneha.p@precisionforge.com', '$2b$10$e8w...dummyhash', 'Sneha Patel', 'negotiator')
ON CONFLICT (id) DO NOTHING;


-- =============================================================================
-- SCENARIO 1: DEAL WON (Cold Rolled Stainless Steel Sheet)
-- Buyer: Rahul Verma | Supplier: Apex Steel Corp
-- Achieved $11,500 in savings by trading Net 30 payment terms
-- =============================================================================
INSERT INTO negotiations (
    id, org_id, created_by, status,
    item_name, item_grade_spec, customization_level, quality_criticality,
    quantity, unit, purchase_frequency, estimated_annual_volume, moq_flexibility,
    supplier_quote_price, target_price, walkaway_price, currency, preferred_payment_terms,
    required_lead_time_days, urgency_level, incoterms,
    supplier_name, supplier_relationship, has_alternatives, supplier_price_reason,
    current_round_number, latest_supplier_counter, latest_buyer_offer,
    rounds,
    buyer_leverage_score, ai_insights,
    final_unit_price, total_deal_value, total_savings_amount, agreed_payment_terms, agreed_lead_time_days,
    supplier_rating, winning_tactics,
    advice_for_future_buyers, closed_at
) VALUES (
    'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
    '00000000-0000-0000-0000-000000000001',
    '22222222-2222-2222-2222-222222222222',
    'closed_won',
    'Cold Rolled Stainless Steel Sheet',
    'Grade SS 304 / ASTM A240',
    'commodity',
    'high_precision',
    5000.00, 'kg', 'quarterly', 20000.00, 'flexible',
    14.50, 12.00, 13.50, 'USD', 'net_30',
    14, 'critical', 'CIF',
    'Apex Steel Corp', 'existing_regular', FALSE, 'Global nickel raw material price surge',
    2, 12.20, 12.20,
    '[
      {
        "round_number": 1,
        "date": "2026-10-10",
        "buyer_offer": 11.80,
        "supplier_counter": 13.60,
        "notes": "Offered $11.80. Supplier resisted citing nickel inflation; dropped quote to $13.60."
      },
      {
        "round_number": 2,
        "date": "2026-10-12",
        "buyer_offer": 12.20,
        "supplier_counter": 12.20,
        "notes": "Offered Net 30 payment terms in exchange for $12.20. Supplier sales director accepted."
      }
    ]'::jsonb,
    42,
    '{
      "leverage_score": 42,
      "weak_points": ["Critical production line urgency reduces walkaway threat", "No active backup supplier"],
      "tactics": {"anchor_price": 11.80, "trading_chip": "Offer accelerated Net 30 credit for price discount"}
    }'::jsonb,
    12.20,
    61000.00,  -- 5,000 kg * $12.20
    11500.00,  -- ($14.50 - $12.20) * 5,000 kg saved!
    'Net 30 Days',
    12,
    4.5,
    ARRAY['payment_terms_trade', 'volume_commitment'],
    'Apex Steel will drop to $12.20 if you offer Net 30 payment and commit to a quarterly schedule. Never accept their initial freight markup—they have 5% margin buffer built into CIF shipping.',
    CURRENT_TIMESTAMP - INTERVAL '5 days'
);


-- =============================================================================
-- SCENARIO 2: DEAL LOST / WALKAWAY (High Density Polyethylene Granules)
-- Buyer: Sneha Patel | Supplier: PolyChem International
-- Walked away because supplier refused to budge below walkaway ceiling ($1.90)
-- =============================================================================
INSERT INTO negotiations (
    id, org_id, created_by, status,
    item_name, item_grade_spec, customization_level, quality_criticality,
    quantity, unit, purchase_frequency, estimated_annual_volume, moq_flexibility,
    supplier_quote_price, target_price, walkaway_price, currency, preferred_payment_terms,
    required_lead_time_days, urgency_level, incoterms,
    supplier_name, supplier_relationship, has_alternatives, supplier_price_reason,
    current_round_number, latest_supplier_counter, latest_buyer_offer,
    rounds,
    buyer_leverage_score, ai_insights,
    loss_reason, supplier_lowest_counter_offer, loss_next_action,
    advice_for_future_buyers, closed_at
) VALUES (
    'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
    '00000000-0000-0000-0000-000000000001',
    '33333333-3333-3333-3333-333333333333',
    'closed_lost',
    'High Density Polyethylene Granules',
    'HDPE Blow Molding Grade B5600',
    'commodity',
    'standard',
    12000.00, 'kg', 'monthly', 144000.00, 'strict_limit',
    2.10, 1.75, 1.90, 'USD', 'net_60',
    21, 'low', 'FOB',
    'PolyChem International', 'new_supplier', TRUE, 'Crude oil petrochemical feedstocks tariff',
    3, 1.98, 1.85,
    '[
      {
        "round_number": 1,
        "date": "2026-10-05",
        "buyer_offer": 1.75,
        "supplier_counter": 2.05,
        "notes": "Countered at $1.75. Supplier claimed petrochemical price hikes."
      },
      {
        "round_number": 2,
        "date": "2026-10-07",
        "buyer_offer": 1.82,
        "supplier_counter": 2.00,
        "notes": "Showed market commodity benchmark. Supplier dropped to $2.00."
      },
      {
        "round_number": 3,
        "date": "2026-10-09",
        "buyer_offer": 1.88,
        "supplier_counter": 1.98,
        "notes": "Final attempt at $1.88. Supplier gave rock-bottom refusal at $1.98."
      }
    ]'::jsonb,
    78,
    '{
      "leverage_score": 78,
      "weak_points": ["Low urgency and active alternative quotes give buyer strong walkaway power"],
      "tactics": {"anchor_price": 1.75, "walkaway_warning": "Enforce ceiling of $1.90"}
    }'::jsonb,
    'price_exceeded_walkaway',
    1.98,
    'switched_to_alternative_supplier',
    'PolyChem sales manager was inflexible and refused to breach $1.98 citing crude oil tariffs. We exercised our BATNA and purchased from Gulf Polymers at $1.82. Do not negotiate with PolyChem without active competitive quotes.',
    CURRENT_TIMESTAMP - INTERVAL '9 days'
);


-- =============================================================================
-- SCENARIO 3: IN PROGRESS / ACTIVE NEGOTIATION (M8 Fasteners)
-- Buyer: Rahul Verma | Supplier: FastenFast Hardware Ltd
-- Currently in Round 2: Buyer offered $0.13, Supplier countered at $0.16
-- =============================================================================
INSERT INTO negotiations (
    id, org_id, created_by, status,
    item_name, item_grade_spec, customization_level, quality_criticality,
    quantity, unit, purchase_frequency, estimated_annual_volume, moq_flexibility,
    supplier_quote_price, target_price, walkaway_price, currency, preferred_payment_terms,
    required_lead_time_days, urgency_level, incoterms,
    supplier_name, supplier_relationship, has_alternatives, supplier_price_reason,
    current_round_number, latest_supplier_counter, latest_buyer_offer,
    rounds,
    buyer_leverage_score, ai_insights
) VALUES (
    'cccccccc-cccc-cccc-cccc-cccccccccccc',
    '00000000-0000-0000-0000-000000000001',
    '22222222-2222-2222-2222-222222222222',
    'in_progress',
    'M8 High-Tensile Zinc Plated Hex Bolts',
    'ISO 4014 Grade 8.8',
    'commodity',
    'standard',
    50000.00, 'pcs', 'annual_contract', 200000.00, 'flexible',
    0.18, 0.12, 0.15, 'USD', 'net_30',
    30, 'moderate', 'DDP',
    'FastenFast Hardware Ltd', 'existing_regular', TRUE, 'Zinc plating electroplating chemical cost increase',
    2, 0.16, 0.13,
    '[
      {
        "round_number": 1,
        "date": "2026-10-16",
        "buyer_offer": 0.12,
        "supplier_counter": 0.17,
        "notes": "Opened with target $0.12 based on annual 200k projection. Supplier countered at $0.17."
      },
      {
        "round_number": 2,
        "date": "2026-10-18",
        "buyer_offer": 0.13,
        "supplier_counter": 0.16,
        "notes": "Offered to increase initial batch from 50k to 75k pcs for $0.13. Supplier countered at $0.16."
      }
    ]'::jsonb,
    68,
    '{
      "leverage_score": 68,
      "weak_points": ["Zinc plating surcharge is partly legitimate due to energy costs"],
      "tactics": {
        "anchor_price": 0.13,
        "next_round_recommendation": "Offer split shipment: 50k pcs now at $0.14 and 25k pcs in 60 days to lock in deal below walkaway ceiling of $0.15."
      },
      "predicted_supplier_questions": [
        {
          "question": "Can you issue a firm purchase order for the full 200,000 annual volume today?",
          "recommended_response": "We will issue a Blanket PO for 200,000 units with scheduled quarterly call-offs, contingent on unit rate of $0.135."
        }
      ]
    }'::jsonb
);
