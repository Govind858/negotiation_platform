import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation_with_diagrams():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette
    BG_COLOR = RGBColor(11, 15, 25)         # Slate 950
    CARD_BG = RGBColor(22, 30, 49)          # Slate 900
    CARD_ALT = RGBColor(30, 41, 59)         # Slate 800
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(148, 163, 184)    # Slate 400
    ACCENT_GREEN = RGBColor(16, 185, 129)   # Emerald 500
    ACCENT_BLUE = RGBColor(56, 189, 248)    # Sky 400
    ACCENT_AMBER = RGBColor(245, 158, 11)   # Amber 500
    ACCENT_RED = RGBColor(239, 68, 68)      # Red 500
    BORDER_COLOR = RGBColor(45, 55, 78)

    blank_layout = prs.slide_layouts[6]

    def add_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.color.rgb = BG_COLOR
        return bg

    def add_header(slide, tag, title):
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag.upper()
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_GREEN

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.7))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE

    def add_arrow(slide, x, y, w, h, direction="right", color=ACCENT_GREEN):
        shape_type = MSO_SHAPE.RIGHT_ARROW if direction == "right" else MSO_SHAPE.DOWN_ARROW
        arrow = slide.shapes.add_shape(shape_type, x, y, w, h)
        arrow.fill.solid()
        arrow.fill.fore_color.rgb = color
        arrow.line.color.rgb = color
        return arrow

    # =========================================================================
    # SLIDE 1: COVER
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_background(s1)
    
    t_box = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11), Inches(3.8))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    
    p0 = tf1.paragraphs[0]
    p0.text = "AI-POWERED MANUFACTURING PROCUREMENT"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_GREEN
    p0.space_after = Pt(14)

    p1 = tf1.add_paragraph()
    p1.text = "ProcureAI: Negotiation Intelligence &\nInstitutional Memory Platform"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(18)

    p2 = tf1.add_paragraph()
    p2.text = "Empowering procurement teams with pre-call AI battlecards, native PostgreSQL deal matching,\nand structured multi-round feedback loops."
    p2.font.size = Pt(16)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(24)

    p3 = tf1.add_paragraph()
    p3.text = "Complete System Architecture & Visual Technical Blueprint"
    p3.font.size = Pt(13)
    p3.font.color.rgb = ACCENT_GREEN

    # =========================================================================
    # SLIDE 2: THE PROBLEM
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_background(s2)
    add_header(s2, "01. The Problem", "Why Manufacturing Companies Overpay for Materials")

    problems = [
        ("1. Unprepared Buyers", "Buyers enter supplier phone calls without quantitative leverage, hidden weak points, or walkaway boundaries, leading to quick concessions."),
        ("2. Institutional Amnesia", "When an experienced procurement manager leaves, years of supplier pricing tactics, concessions, and winning strategies disappear from the firm."),
        ("3. The New Staff Trap", "New staff buyers are unaware of historical prices. Suppliers easily charge them 15-20% higher rates for materials previously bought much cheaper.")
    ]
    for i, (title, desc) in enumerate(problems):
        x = Inches(0.8 + i * 3.95)
        box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.0), Inches(3.7), Inches(4.5))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = BORDER_COLOR
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.4)
        tf.margin_left = Inches(0.35)
        tf.margin_right = Inches(0.35)
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(14)
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(14)
        p2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 3: THE SOLUTION
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_background(s3)
    add_header(s3, "02. The Solution", "An Intelligent Negotiation CRM for Manufacturing")

    solutions = [
        ("Pre-Call AI Battlecards", "A 2-minute questionnaire analyzes price gaps, commodity dynamics, and urgency to produce model counter-replies and concession playbooks."),
        ("Instant Deal Matching", "Automatically detects if the company bought this item before. Surfaces past winning prices and specific vendor tactics to junior staff on day one."),
        ("Closed-Loop Memory Bank", "Every Won deal records financial savings and winning tactics; every Lost deal records vendor floor prices and walkaway discipline.")
    ]
    for i, (title, desc) in enumerate(solutions):
        x = Inches(0.8 + i * 3.95)
        box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.0), Inches(3.7), Inches(4.5))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = ACCENT_GREEN
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.4)
        tf.margin_left = Inches(0.35)
        tf.margin_right = Inches(0.35)
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.space_after = Pt(14)
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(14)
        p2.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 4: END-TO-END FLOWCHART (DIAGRAM SLIDE 1)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_background(s4)
    add_header(s4, "03. End-to-End User Journey", "Flowchart: From Questionnaire to Institutional Memory")

    steps = [
        ("1. Intake Wizard", "Item specs, volume,\nprices & urgency"),
        ("2. Trigram Match", "PostgreSQL pg_trgm\nfinds past benchmark"),
        ("3. AI Battlecard", "Gemini 2.0 Flash\nWeak points & scripts"),
        ("4. Active Rounds", "Log supplier counter,\nlead time & MOQ notes"),
        ("5. Closeout Memory", "Calculate $ savings\n& record vendor tip")
    ]

    box_w = Inches(1.9)
    box_h = Inches(2.4)
    y_pos = Inches(2.1)

    for i, (stitle, sdesc) in enumerate(steps):
        x_pos = Inches(0.8 + i * 2.45)
        box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_pos, y_pos, box_w, box_h)
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = ACCENT_GREEN if i in [1, 2, 4] else BORDER_COLOR
        tf = box.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = Inches(0.15)
        tf.margin_right = Inches(0.15)
        
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = stitle
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN if i in [1, 2, 4] else TEXT_WHITE
        p.space_after = Pt(8)

        p2 = tf.add_paragraph()
        p2.alignment = PP_ALIGN.CENTER
        p2.text = sdesc
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED

        if i < 4:
            add_arrow(s4, x_pos + box_w + Inches(0.1), y_pos + Inches(1.0), Inches(0.35), Inches(0.4), "right", ACCENT_GREEN)

    # Return Loop Banner
    loop_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.0), Inches(11.7), Inches(1.5))
    loop_box.fill.solid()
    loop_box.fill.fore_color.rgb = CARD_ALT
    loop_box.line.color.rgb = ACCENT_GREEN
    tf_loop = loop_box.text_frame
    tf_loop.word_wrap = True
    tf_loop.margin_left = Inches(0.4)
    tf_loop.margin_top = Inches(0.25)
    
    p_l1 = tf_loop.paragraphs[0]
    p_l1.text = "🔄 THE CONTINUOUS LEARNING LOOP (INSTITUTIONAL MEMORY)"
    p_l1.font.size = Pt(13)
    p_l1.font.bold = True
    p_l1.font.color.rgb = ACCENT_GREEN
    p_l1.space_after = Pt(4)

    p_l2 = tf_loop.add_paragraph()
    p_l2.text = "Step 5 (Closeout) feeds directly back into Step 2 (Matching)! Every time any buyer closes a deal, their negotiated price, payment terms, and vendor tips instantly become the active benchmark for all future buyers."
    p_l2.font.size = Pt(12)
    p_l2.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 5: PRE-CALL BATTLECARD UI
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_background(s5)
    add_header(s5, "04. User Experience", "What the Buyer Sees: The Pre-Call Battlecard")

    card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.1))
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = BORDER_COLOR
    tf_c = card.text_frame
    tf_c.word_wrap = True
    tf_c.margin_left = Inches(0.5)
    tf_c.margin_top = Inches(0.35)
    tf_c.margin_right = Inches(0.5)

    p = tf_c.paragraphs[0]
    p.text = "Cold Rolled Stainless Steel Sheet (Grade SS 304 / ASTM A240)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE

    p = tf_c.add_paragraph()
    p.text = "Batch: 5,000 kg  |  Supplier Initial Quote: $14.50/kg  |  Target Price: $12.00/kg  |  Ceiling: $13.50/kg"
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_after = Pt(14)

    p = tf_c.add_paragraph()
    p.text = "BUYER LEVERAGE SCORE:  42 / 100  (Moderate-Low Leverage)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(10)

    p = tf_c.add_paragraph()
    p.text = "⚠️ CRITICAL WEAK POINTS DETECTED:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p = tf_c.add_paragraph()
    p.text = "• Urgent factory line stoppage deadline weakens your ability to delay orders.\n• No active backup quotes; do not bluff a walkaway without preparation."
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(12)

    p = tf_c.add_paragraph()
    p.text = "💡 HISTORICAL BENCHMARK FOUND IN COMPANY MEMORY:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p = tf_c.add_paragraph()
    p.text = "• 4 months ago, Rahul bought this from Apex Steel at $12.20/kg.\n• Winning Advice: 'Apex drops price by 6% if you offer Net 30 payment and quarterly delivery schedule.'"
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 6: TECHNICAL ARCHITECTURE TOPOLOGY (DIAGRAM SLIDE 2)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_background(s6)
    add_header(s6, "05. Technical Architecture", "System Topology: Multi-Tier Architecture Diagram")

    # Layer 1: Client
    client_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(1.1))
    client_box.fill.solid()
    client_box.fill.fore_color.rgb = CARD_BG
    client_box.line.color.rgb = ACCENT_BLUE
    tf_cl = client_box.text_frame
    tf_cl.word_wrap = True
    tf_cl.margin_left = Inches(0.4)
    tf_cl.margin_top = Inches(0.15)
    p = tf_cl.paragraphs[0]
    p.text = "CLIENT LAYER: React / Next.js Web Application"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p2 = tf_cl.add_paragraph()
    p2.text = "Admin Management Portal  |  Buyer Intake Wizard  |  Live Battlecard Dashboard  |  Historical Price Archive"
    p2.font.size = Pt(12)
    p2.font.color.rgb = TEXT_WHITE

    # Arrow Down
    add_arrow(s6, Inches(6.3), Inches(3.0), Inches(0.7), Inches(0.35), "down", ACCENT_GREEN)

    # Layer 2: API Gateway & Services
    api_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.45), Inches(11.7), Inches(1.2))
    api_box.fill.solid()
    api_box.fill.fore_color.rgb = CARD_BG
    api_box.line.color.rgb = ACCENT_GREEN
    tf_api = api_box.text_frame
    tf_api.word_wrap = True
    tf_api.margin_left = Inches(0.4)
    tf_api.margin_top = Inches(0.15)
    p = tf_api.paragraphs[0]
    p.text = "BACKEND SERVICES LAYER: REST API (Node.js / FastAPI)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p2 = tf_api.add_paragraph()
    p2.text = "JWT & RBAC Middleware  |  Tenant Isolation Guard  |  Trigram Match Svc  |  Vercel AI SDK Svc  |  Closeout Engine"
    p2.font.size = Pt(12)
    p2.font.color.rgb = TEXT_WHITE

    # Arrows Down to DB and AI
    add_arrow(s6, Inches(3.3), Inches(4.75), Inches(0.6), Inches(0.35), "down", ACCENT_GREEN)
    add_arrow(s6, Inches(9.3), Inches(4.75), Inches(0.6), Inches(0.35), "down", ACCENT_AMBER)

    # Layer 3: Left = PostgreSQL, Right = AI Engine
    db_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.2), Inches(5.7), Inches(1.8))
    db_box.fill.solid()
    db_box.fill.fore_color.rgb = CARD_BG
    db_box.line.color.rgb = ACCENT_GREEN
    tf_db = db_box.text_frame
    tf_db.word_wrap = True
    tf_db.margin_left = Inches(0.35)
    tf_db.margin_top = Inches(0.2)
    p = tf_db.paragraphs[0]
    p.text = "DATA LAYER: PostgreSQL 15+"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p = tf_db.add_paragraph()
    p.text = "• pg_trgm fuzzy matching (< 5ms response)\n• Native JSONB for dynamic rounds & AI insights\n• Row-Level Security for multi-tenant isolation"
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_MUTED

    ai_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(5.2), Inches(5.7), Inches(1.8))
    ai_box.fill.solid()
    ai_box.fill.fore_color.rgb = CARD_BG
    ai_box.line.color.rgb = ACCENT_AMBER
    tf_ai = ai_box.text_frame
    tf_ai.word_wrap = True
    tf_ai.margin_left = Inches(0.35)
    tf_ai.margin_top = Inches(0.2)
    p = tf_ai.paragraphs[0]
    p.text = "AI ENGINE: Google Gemini 2.0 Flash"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p = tf_ai.add_paragraph()
    p.text = "• Integrated via enterprise Vercel AI SDK\n• 100% Type-safe Zod runtime schema validation\n• Free Tier (15 RPM) -> $0.00 launch cost"
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 7: DATABASE ERD DIAGRAM (DIAGRAM SLIDE 3)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_background(s7)
    add_header(s7, "06. Database Architecture", "Entity-Relationship Diagram (ERD): Lean 4-Table Schema")

    tables = [
        ("ORGANIZATIONS (Tenants)", "id (UUID PK)\ncompany_name (VARCHAR)\nindustry (VARCHAR)\ncreated_at (TIMESTAMP)", Inches(0.8), Inches(1.9), Inches(3.7), Inches(2.2)),
        ("USERS (Staff & RBAC)", "id (UUID PK)\norg_id (UUID FK)\nemail (VARCHAR UNIQUE)\nrole ('admin'|'manager'|'buyer'|'viewer')\npassword_hash (VARCHAR)", Inches(4.8), Inches(1.9), Inches(3.7), Inches(2.2)),
        ("INVITATIONS (Links)", "id (UUID PK)\norg_id (UUID FK)\nemail (VARCHAR)\nrole (VARCHAR)\ntoken (VARCHAR UNIQUE)\nstatus ('pending'|'accepted')", Inches(8.8), Inches(1.9), Inches(3.7), Inches(2.2)),
        ("NEGOTIATIONS (Master Table)", "id (UUID PK)  |  org_id (UUID FK)  |  created_by (UUID FK)  |  status ('in_progress'|'closed_won'|'closed_lost')\nitem_name, item_grade_spec, quantity, unit, quote_price, target_price, walkaway_price, supplier_name\nrounds (JSONB Array of meeting logs)  |  ai_insights (JSONB)  |  final_unit_price, savings_amount, advice_for_future_buyers", Inches(0.8), Inches(4.5), Inches(11.7), Inches(2.4))
    ]

    for tname, tfields, x, y, w, h in tables:
        box = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = ACCENT_GREEN if "NEGOTIATIONS" in tname else BORDER_COLOR
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.2)
        tf.margin_right = Inches(0.25)
        p = tf.paragraphs[0]
        p.text = tname
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN if "NEGOTIATIONS" in tname else ACCENT_BLUE
        p.space_after = Pt(4)
        p2 = tf.add_paragraph()
        p2.text = tfields
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 8: NEGOTIATION STATE MACHINE (DIAGRAM SLIDE 4)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_background(s8)
    add_header(s8, "07. Deal Lifecycle", "State Machine: Multi-Round Meetings to Won/Lost Closure")

    # State 1: Draft / Intake
    b1 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.3), Inches(2.5), Inches(1.8))
    b1.fill.solid()
    b1.fill.fore_color.rgb = CARD_BG
    b1.line.color.rgb = BORDER_COLOR
    tf = b1.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "1. INTAKE SUBMITTED\n\nRuns Trigram Match\n& Generates Battlecard"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE

    add_arrow(s8, Inches(3.4), Inches(2.9), Inches(0.4), Inches(0.4), "right", ACCENT_GREEN)

    # State 2: in_progress (Rounds)
    b2 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.9), Inches(2.1), Inches(3.2), Inches(2.2))
    b2.fill.solid()
    b2.fill.fore_color.rgb = CARD_BG
    b2.line.color.rgb = ACCENT_GREEN
    tf = b2.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "STATE: in_progress\n\n🔄 Active Negotiation Rounds\nRound 1 -> Round 2 -> Round 3\nLogs Price, Terms, Lead Time & Notes"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    add_arrow(s8, Inches(7.2), Inches(2.5), Inches(0.5), Inches(0.35), "right", ACCENT_GREEN)
    add_arrow(s8, Inches(7.2), Inches(3.5), Inches(0.5), Inches(0.35), "right", ACCENT_RED)

    # State 3: Won
    b3 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(1.8), Inches(4.7), Inches(1.8))
    b3.fill.solid()
    b3.fill.fore_color.rgb = CARD_BG
    b3.line.color.rgb = ACCENT_GREEN
    tf = b3.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "🏆 STATE: closed_won (Deal Agreed)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p = tf.add_paragraph()
    p.text = "• Calculates Dollar Savings: (Quote - Final Price) * Qty\n• Indexes as Active Golden Benchmark for next buyer\n• Captures winning tactic: 'What made supplier budge?'"
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_WHITE

    # State 4: Lost
    b4 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(3.8), Inches(4.7), Inches(1.8))
    b4.fill.solid()
    b4.fill.fore_color.rgb = CARD_BG
    b4.line.color.rgb = ACCENT_RED
    tf = b4.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]
    p.text = "🛑 STATE: closed_lost (Walked Away)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED
    p = tf.add_paragraph()
    p.text = "• Records Supplier Rock-Bottom Floor Price\n• Logs walkaway reason (price ceiling, bad credit terms)\n• Flags supplier as 'Rigid Pricing' for future buyers"
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_WHITE

    # Note
    note = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.9), Inches(11.7), Inches(0.9))
    note.fill.solid()
    note.fill.fore_color.rgb = CARD_ALT
    note.line.color.rgb = BORDER_COLOR
    tf = note.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.15)
    p = tf.paragraphs[0]
    p.text = "💡 Strategic Insight: Walking away is a disciplined victory. It protects the factory's manufacturing margins and teaches future buyers this vendor's limits."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 9: STARTUP ECONOMICS
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_background(s9)
    add_header(s9, "08. Financial Feasibility", "Engineered for Near-Zero Operating Costs")

    stats = [
        ("$0.00 / mo", "AI Strategy Infrastructure", "Google Gemini 2.0 Flash free tier provides 15 RPM. Even at paid scale, 1,000 negotiations cost less than $0.25 total."),
        ("$0.00 / mo", "Search & Memory Engine", "PostgreSQL native Trigram indexing eliminates expensive third-party search subscriptions like Pinecone or Algolia."),
        ("> 95%", "SaaS Gross Margin", "Because cloud operating overhead is near zero, subscription revenue converts almost entirely into operating profit.")
    ]
    for i, (val, label, note) in enumerate(stats):
        x = Inches(0.8 + i * 3.95)
        box = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.0), Inches(3.7), Inches(4.5))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = ACCENT_GREEN
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.4)
        tf.margin_left = Inches(0.35)
        tf.margin_right = Inches(0.35)
        p = tf.paragraphs[0]
        p.text = val
        p.font.size = Pt(32)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.space_after = Pt(8)
        p2 = tf.add_paragraph()
        p2.text = label
        p2.font.size = Pt(16)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.space_after = Pt(14)
        p3 = tf.add_paragraph()
        p3.text = note
        p3.font.size = Pt(13)
        p3.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 10: BUSINESS IMPACT & ROI
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_background(s10)
    add_header(s10, "09. Business Impact", "Measurable ROI for Manufacturing Clients")

    rois = [
        ("4 - 12%", "Direct Procurement Cost Reduction", "Average material cost savings achieved by arming buyers with historical benchmarks and structured concession trades."),
        ("< 1 Day", "Buyer Onboarding Time", "New employees immediately negotiate with the institutional memory, supplier insights, and past prices of senior directors."),
        ("100%", "Walkaway Discipline", "Prevents emotional overspending by enforcing strict walkaway ceiling prices and logging disciplined vendor walkaways.")
    ]
    for i, (stat, title, desc) in enumerate(rois):
        x = Inches(0.8 + i * 3.95)
        box = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.0), Inches(3.7), Inches(4.5))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = BORDER_COLOR
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.4)
        tf.margin_left = Inches(0.35)
        tf.margin_right = Inches(0.35)
        p = tf.paragraphs[0]
        p.text = stat
        p.font.size = Pt(36)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(8)
        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(16)
        p2.font.bold = True
        p2.font.color.rgb = ACCENT_GREEN
        p2.space_after = Pt(14)
        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(13)
        p3.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 11: IMPLEMENTATION ROADMAP
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_background(s11)
    add_header(s11, "10. Delivery Roadmap", "Structured 4-Sprint Implementation Plan")

    sprints = [
        ("Sprint 1", "Auth, Multi-Tenancy & RBAC", "PostgreSQL schema, JWT auth middleware, and tokenized invite-link onboarding flow."),
        ("Sprint 2", "Intake Wizard & AI Engine", "5-stage intake questionnaire & Gemini 2.0 Flash Vercel AI SDK battlecard pipeline."),
        ("Sprint 3", "Matching & Rounds Logging", "PostgreSQL Trigram fuzzy search & multi-round call logging interface with active offers."),
        ("Sprint 4", "Closeout & Memory Bank", "Won/Lost feedback modals, automated financial savings calculator, and price archive explorer.")
    ]
    for i, (sprint, title, desc) in enumerate(sprints):
        x = Inches(0.8 + i * 2.95)
        box = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.0), Inches(2.8), Inches(4.5))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = BORDER_COLOR
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.4)
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        p = tf.paragraphs[0]
        p.text = sprint.upper()
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.space_after = Pt(6)
        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(16)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.space_after = Pt(14)
        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(12)
        p3.font.color.rgb = TEXT_MUTED

    output_path = r"c:\Users\Govind\Desktop\negotiation_recording_ai_tool\ProcureAI_System_Architecture_Presentation.pptx"
    prs.save(output_path)
    print(f"Successfully generated PowerPoint with visual flowcharts and diagrams at: {output_path}")

if __name__ == "__main__":
    build_presentation_with_diagrams()
