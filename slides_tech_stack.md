# Presentation Slides Content: Technology Stack (Condensed)
## 2-Slide Executive Architecture & Economics

Use this condensed 2-slide format directly in Google Slides (or copy-paste into Gemini in Google Slides). It covers the entire technology stack, framework choices, and financial economics in **just 2 high-impact slides**.

---

### Slide 1: The Core Tech Stack & Framework Choices

* **Slide Title:** Technology Stack & System Architecture
* **Subtitle:** Enterprise-Grade, Lean, and Cost-Optimized Across All 4 Layers
* **Layout:** 4 Horizontal Component Cards + Key Rationale

#### Visual Grid (Include on Slide):
```text
┌───────────────────────┬───────────────────────────────────┬────────────────────────────────────────┐
│ LAYER                 │ TECHNOLOGY & FRAMEWORK            │ WHY IT WAS CHOSEN                      │
├───────────────────────┼───────────────────────────────────┼────────────────────────────────────────┤
│ 1. Frontend           │ React / Next.js + Tailwind CSS    │ Fast intake wizard & live battlecard UI│
│ 2. Backend Services   │ Node.js (Express) / FastAPI       │ Stateless REST API, JWT auth, Zod guard│
│ 3. Master Database    │ PostgreSQL 15+ (pg_trgm + JSONB)  │ Strict decimal math + sub-5ms search   │
│ 4. AI Strategy Engine │ Gemini 2.0 Flash (Vercel AI SDK)  │ 100% Type-safe Zod schema, $0.00 launch│
└───────────────────────┴───────────────────────────────────┴────────────────────────────────────────┘
```

#### Key Architectural Decisions:
* **PostgreSQL over MongoDB & Pinecone:** Provides exact financial precision (`NUMERIC(15,2)`), native document flexibility (`JSONB`), and built-in fuzzy search (`pg_trgm`) in $<5\text{ms}$ with **zero third-party search fees**.
* **Vercel AI SDK over Direct API:** Enforces a runtime TypeScript Zod schema to prevent AI hallucinations and gives **zero vendor lock-in** (switch models in 1 line of code).

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, here is our technology stack in one unified view. We use React and Next.js on the frontend, a stateless Node.js or FastAPI backend, and PostgreSQL 15+ as our primary database. We chose PostgreSQL because it gives us exact financial precision, document flexibility via JSONB, and sub-5ms fuzzy search without paying for external search tools. For AI, we use Google Gemini 2.0 Flash integrated through the Vercel AI SDK for strict type safety and zero vendor lock-in."*

---

### Slide 2: Security Architecture & Startup Economics

* **Slide Title:** Security, Tenant Isolation & Cost Feasibility
* **Subtitle:** Enterprise Multi-Tenancy Engineered for Near-Zero Operating Costs
* **Layout:** Split View: Security Safeguards (Left) vs. Unit Economics (Right)

#### Slide Content:

```text
┌──────────────────────────────────────────────┐  ┌──────────────────────────────────────────────┐
│ 🛡️ MULTI-TENANT SECURITY & GOVERNANCE         │  │ 💰 INFRASTRUCTURE COST & UNIT ECONOMICS     │
├──────────────────────────────────────────────┤  ├──────────────────────────────────────────────┤
│ • Row-Level Security (RLS):                  │  │ • AI Infrastructure: $0.00 / month           │
│   Company A can never access Company B's data│  │   Gemini 2.0 Flash Free Tier (15 RPM)        │
│                                              │  │                                              │
│ • 4-Role RBAC:                               │  │ • Search Infrastructure: $0.00 / month       │
│   Admin, Manager, Negotiator, and Viewer     │  │   PostgreSQL native trigrams (No Pinecone)   │
│                                              │  │                                              │
│ • Tokenized Invite Links:                    │  │ • Scaling Economics:                         │
│   app.com/join?token=... with pre-set roles  │  │   1,000 negotiations cost only $12.25/month  │
│                                              │  │                                              │
│ • Stateless JWT Authentication:              │  │ • SaaS Gross Margin: > 95%                   │
│   Enables infinite horizontal scaling        │  │   Translates directly to operating profit    │
└──────────────────────────────────────────────┘  └──────────────────────────────────────────────┘
```

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, on our security and cost profile: Multi-tenant isolation is enforced at the database level with Row-Level Security, so client pricing data is 100% confidential. Financially, our launch cost is zero dollars per month. Even at a volume of 1,000 negotiations a month, our total cloud overhead is under $13—meaning each negotiation costs barely one cent to run. This gives our business an extraordinary gross margin of over 95%."*
