import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    # 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Color palette
    BG_COLOR = RGBColor(11, 15, 25)      # Deep Navy/Slate
    CARD_BG = RGBColor(22, 30, 49)       # Slate Card
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(148, 163, 184) # Slate 400
    ACCENT_GREEN = RGBColor(16, 185, 129) # Emerald Green
    ACCENT_AMBER = RGBColor(245, 158, 11) # Amber
    BORDER_COLOR = RGBColor(45, 55, 78)

    blank_slide_layout = prs.slide_layouts[6]

    def add_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.color.rgb = BG_COLOR
        return bg

    def add_header(slide, tag, title):
        # Category Tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.4))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag.upper()
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_GREEN

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(26)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_slide_layout)
    add_background(slide1)

    t_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11), Inches(3.8))
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
    p1.font.size = Pt(38)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(18)

    p2 = tf1.add_paragraph()
    p2.text = "Empowering procurement teams to win raw material negotiations with automated pre-call strategy,\nzero-cost historical deal benchmarks, and structured feedback loops."
    p2.font.size = Pt(16)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(24)

    p3 = tf1.add_paragraph()
    p3.text = "Technical Architecture & System Design Blueprint"
    p3.font.size = Pt(13)
    p3.font.color.rgb = ACCENT_GREEN

    # =========================================================================
    # SLIDE 2: THE PROBLEM
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_slide_layout)
    add_background(slide2)
    add_header(slide2, "01. The Problem", "Why Manufacturing Companies Overpay for Raw Materials")

    problems = [
        ("1. Unprepared Buyers", "Buyers enter supplier phone calls without knowing their true leverage, hidden weak points, or walkaway boundaries, leading to quick and costly concessions."),
        ("2. Institutional Amnesia", "When an experienced procurement manager leaves the company, years of supplier pricing tactics, concessions, and winning strategies vanish."),
        ("3. The New Employee Trap", "New staff buyers are unaware of historical prices. Suppliers easily charge them 15-20% higher rates for materials previously bought much cheaper.")
    ]

    for i, (title, desc) in enumerate(problems):
        x = Inches(0.8 + i * 3.95)
        box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.0), Inches(3.7), Inches(4.5))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = BORDER_COLOR
        
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.4)
        tf.margin_left = Inches(0.4)
        tf.margin_right = Inches(0.4)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(16)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(14)
        p2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 3: THE SOLUTION
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_slide_layout)
    add_background(slide3)
    add_header(slide3, "02. The Solution", "An Intelligent Negotiation CRM for Manufacturing Procurement")

    solutions = [
        ("Pre-Call AI Battlecards", "A 2-minute questionnaire analyzes price gaps, commodity dynamics, and line-stoppage urgency to produce counter-replies and concession playbooks before dialing."),
        ("Instant Deal Matching", "Automatically detects if the company bought this item before. Surfaces past winning prices and specific vendor tactics to junior staff on day one."),
        ("Closed-Loop Memory Bank", "Every Won deal records financial savings and winning tactics; every Lost deal records vendor floor prices and walkaway discipline to protect factory margins.")
    ]

    for i, (title, desc) in enumerate(solutions):
        x = Inches(0.8 + i * 3.95)
        box = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.0), Inches(3.7), Inches(4.5))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = ACCENT_GREEN
        
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.4)
        tf.margin_left = Inches(0.4)
        tf.margin_right = Inches(0.4)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.space_after = Pt(16)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(14)
        p2.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 4: THE 3 CORE FLOWS
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_slide_layout)
    add_background(slide4)
    add_header(slide4, "03. Domain Engine", "The 3 Core Workflows That Drive The System")

    core_flows = [
        ("Flow 1: Intake & Pre-Call AI Battlecard", "5-stage questionnaire capturing item specs, batch scale, quote vs target price, and supplier leverage. Google Gemini 2.0 Flash via Vercel AI SDK calculates leverage score (0-100) and predicts supplier pushbacks."),
        ("Flow 2: Historical Deal Matching Engine", "PostgreSQL Trigram (pg_trgm) runs natively in <5ms. Matches material names and specs against closed company deals to surface past winning benchmarks with zero external search subscriptions."),
        ("Flow 3: Multi-Round Logging & Deal Closeout", "Captures round-by-round commercial counter-offers (Price, Lead time, Terms, MOQ, Notes). Calculates verified financial savings on Won deals and logs vendor risk on Lost deals.")
    ]

    for i, (title, desc) in enumerate(core_flows):
        y = Inches(1.9 + i * 1.65)
        box = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(1.4))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = BORDER_COLOR
        
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.2)
        tf.margin_left = Inches(0.4)
        tf.margin_right = Inches(0.4)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.space_after = Pt(4)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(13)
        p2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 5: PRE-CALL BATTLECARD UI
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_slide_layout)
    add_background(slide5)
    add_header(slide5, "04. User Experience", "What the Buyer Sees: The Pre-Call Battlecard")

    # Main Card
    main_card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.9), Inches(11.7), Inches(5.0))
    main_card.fill.solid()
    main_card.fill.fore_color.rgb = CARD_BG
    main_card.line.color.rgb = BORDER_COLOR
    
    tf_m = main_card.text_frame
    tf_m.word_wrap = True
    tf_m.margin_left = Inches(0.5)
    tf_m.margin_top = Inches(0.4)
    tf_m.margin_right = Inches(0.5)

    p_item = tf_m.paragraphs[0]
    p_item.text = "Item: Cold Rolled Stainless Steel Sheet (Grade SS 304 / ASTM A240)"
    p_item.font.size = Pt(18)
    p_item.font.bold = True
    p_item.font.color.rgb = TEXT_WHITE

    p_sub = tf_m.add_paragraph()
    p_sub.text = "Order: 5,000 kg  |  Supplier Initial Quote: $14.50/kg  |  Target Price: $12.00/kg  |  Ceiling: $13.50/kg"
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = TEXT_MUTED
    p_sub.space_after = Pt(18)

    p_score = tf_m.add_paragraph()
    p_score.text = "BUYER LEVERAGE SCORE:  42 / 100  (Moderate-Low Leverage)"
    p_score.font.size = Pt(16)
    p_score.font.bold = True
    p_score.font.color.rgb = ACCENT_AMBER
    p_score.space_after = Pt(14)

    p_warn = tf_m.add_paragraph()
    p_warn.text = "CRITICAL WEAK POINTS DETECTED:"
    p_warn.font.size = Pt(14)
    p_warn.font.bold = True
    p_warn.font.color.rgb = ACCENT_AMBER
    p_warn_text = tf_m.add_paragraph()
    p_warn_text.text = "- Urgent factory line stoppage weakens your ability to delay orders.\n- No active alternative quotes; do not bluff a walkaway without preparation."
    p_warn_text.font.size = Pt(13)
    p_warn_text.font.color.rgb = TEXT_WHITE
    p_warn_text.space_after = Pt(14)

    p_bench = tf_m.add_paragraph()
    p_bench.text = "HISTORICAL BENCHMARK FOUND IN COMPANY MEMORY:"
    p_bench.font.size = Pt(14)
    p_bench.font.bold = True
    p_bench.font.color.rgb = ACCENT_GREEN
    p_bench_text = tf_m.add_paragraph()
    p_bench_text.text = "- 4 months ago, Rahul bought this from Apex Steel at $12.20/kg.\n- Winning Note: 'Apex drops price by 6% if you offer Net 30 payment and quarterly delivery schedule.'"
    p_bench_text.font.size = Pt(13)
    p_bench_text.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 6: TECHNICAL ARCHITECTURE
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_slide_layout)
    add_background(slide6)
    add_header(slide6, "05. Technology Architecture", "Lean, Scalable & Enterprise-Grade Tech Stack")

    tech_stack = [
        ("Frontend Application", "React / Next.js + Tailwind CSS", "Fast component wizards, responsive battlecard dashboards, and progressive UI streaming."),
        ("Backend Services", "Node.js (Express/Fastify) or Python", "Stateless REST API with JWT authentication, multi-tenant middleware, and Zod validation."),
        ("Primary Database", "PostgreSQL 15+ (JSONB + pg_trgm)", "Combines strict financial relational integrity with flexible document updates and sub-5ms fuzzy search."),
        ("AI Intelligence Engine", "Google Gemini 2.0 Flash via Vercel AI SDK", "Enterprise-grade type safety, zero vendor lock-in, free-tier launch ($0/mo), and sub-1.5s latency.")
    ]

    for i, (layer, tech, detail) in enumerate(tech_stack):
        col = i % 2
        row = i // 2
        x = Inches(0.8 + col * 5.95)
        y = Inches(2.0 + row * 2.4)
        
        box = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.75), Inches(2.1))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = BORDER_COLOR
        
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.25)
        tf.margin_left = Inches(0.35)
        tf.margin_right = Inches(0.35)

        p = tf.paragraphs[0]
        p.text = layer.upper()
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.space_after = Pt(4)

        p2 = tf.add_paragraph()
        p2.text = tech
        p2.font.size = Pt(16)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.space_after = Pt(6)

        p3 = tf.add_paragraph()
        p3.text = detail
        p3.font.size = Pt(12)
        p3.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 7: DATABASE DESIGN
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_slide_layout)
    add_background(slide7)
    add_header(slide7, "06. Database Design", "Lean 4-Table Architecture (No Over-Engineering)")

    tables = [
        ("1. organizations", "Tenants Table", "Isolates each manufacturing company. Enforces multi-tenant data boundaries so Company A never sees Company B's prices."),
        ("2. users", "Staff & Roles", "Stores employee credentials and RBAC roles: Admin, Manager, Negotiator, and Viewer."),
        ("3. invitations", "Tokenized Invite Links", "Enables frictionless staff onboarding via secure invite links (app.com/join?token=...) with pre-assigned roles."),
        ("4. negotiations", "Master Living Record", "Stores intake parameters, evolving rounds JSONB array, AI strategy, and final Won/Lost outcomes in a single indexed row.")
    ]

    for i, (name, role, desc) in enumerate(tables):
        col = i % 2
        row = i // 2
        x = Inches(0.8 + col * 5.95)
        y = Inches(2.0 + row * 2.4)
        
        box = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.75), Inches(2.1))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = BORDER_COLOR
        
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.25)
        tf.margin_left = Inches(0.35)
        tf.margin_right = Inches(0.35)

        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = role
        p2.font.size = Pt(12)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.space_after = Pt(6)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(12)
        p3.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 8: RBAC & GOVERNANCE
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_slide_layout)
    add_background(slide8)
    add_header(slide8, "07. Governance & Security", "Enterprise RBAC & Frictionless Onboarding")

    roles = [
        ("Admin", "Owner / VP", "Full company settings, subscription billing, invite/remove staff, view company-wide financial savings."),
        ("Manager", "Procurement Lead", "Invites negotiators/viewers, reviews junior negotiation plans, approves deals exceeding ceiling prices."),
        ("Negotiator", "Buyer / Staff", "Runs questionnaires, receives AI battlecard, logs call rounds, marks deals won/lost, views historical prices."),
        ("Viewer", "Auditor / Finance", "Read-only access to historical closed deals, vendor ratings, audit trails, and company savings analytics.")
    ]

    for i, (role, title, scope) in enumerate(roles):
        x = Inches(0.8 + i * 2.95)
        box = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.0), Inches(2.8), Inches(4.5))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = BORDER_COLOR
        
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.4)
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = role.upper()
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.space_after = Pt(4)

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.space_after = Pt(14)

        p3 = tf.add_paragraph()
        p3.text = scope
        p3.font.size = Pt(12)
        p3.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 9: STARTUP ECONOMICS
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_slide_layout)
    add_background(slide9)
    add_header(slide9, "08. Financial Feasibility", "Engineered for Near-Zero Operating Costs")

    stats = [
        ("$0.00 / mo", "AI Strategy Infrastructure", "Google Gemini 2.0 Flash free tier provides 15 RPM. Even at paid scale, 1,000 negotiations cost less than $0.25 total."),
        ("$0.00 / mo", "Search & Memory Engine", "PostgreSQL native Trigram indexing eliminates expensive third-party search subscriptions like Pinecone or Algolia."),
        ("> 95%", "SaaS Gross Margin", "Because cloud operating overhead is near zero, subscription revenue converts almost entirely into operating profit.")
    ]

    for i, (val, label, note) in enumerate(stats):
        x = Inches(0.8 + i * 3.95)
        box = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.0), Inches(3.7), Inches(4.5))
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
    slide10 = prs.slides.add_slide(blank_slide_layout)
    add_background(slide10)
    add_header(slide10, "09. Business Impact", "Measurable ROI for Manufacturing Clients")

    rois = [
        ("4 - 12%", "Direct Procurement Cost Reduction", "Average material cost savings achieved by arming buyers with historical benchmarks and structured concession trades."),
        ("< 1 Day", "Buyer Onboarding Time", "New employees immediately negotiate with the institutional memory, supplier insights, and past prices of senior directors."),
        ("100%", "Walkaway Discipline", "Prevents emotional overspending by enforcing strict walkaway ceiling prices and logging disciplined vendor walkaways.")
    ]

    for i, (stat, title, desc) in enumerate(rois):
        x = Inches(0.8 + i * 3.95)
        box = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.0), Inches(3.7), Inches(4.5))
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
    slide11 = prs.slides.add_slide(blank_slide_layout)
    add_background(slide11)
    add_header(slide11, "10. Delivery Roadmap", "Structured 4-Sprint Implementation Plan")

    sprints = [
        ("Sprint 1", "Auth, Multi-Tenancy & RBAC", "PostgreSQL schema, JWT auth middleware, and tokenized invite-link onboarding flow."),
        ("Sprint 2", "Intake Wizard & AI Engine", "5-stage intake questionnaire & Gemini 2.0 Flash Vercel AI SDK battlecard pipeline."),
        ("Sprint 3", "Matching & Rounds Logging", "PostgreSQL Trigram fuzzy search & multi-round call logging interface with active offers."),
        ("Sprint 4", "Closeout & Memory Bank", "Won/Lost feedback modals, automated financial savings calculator, and price archive explorer.")
    ]

    for i, (sprint, title, desc) in enumerate(sprints):
        x = Inches(0.8 + i * 2.95)
        box = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.0), Inches(2.8), Inches(4.5))
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

    output_path = r"c:\Users\Govind\Desktop\negotiation_recording_ai_tool\ProcureAI_Architecture.pptx"
    prs.save(output_path)
    print(f"Successfully generated PowerPoint presentation at: {output_path}")

if __name__ == "__main__":
    build_presentation()
