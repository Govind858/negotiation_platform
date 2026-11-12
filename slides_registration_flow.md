# Presentation Slides Content: Registration & Hybrid Authentication Flow
## Ready-to-Use Content for Google Slides & Gemini

Use this structured content directly in Google Slides (or copy-paste into Gemini in Google Slides). It covers the **Hybrid Authentication Architecture, Dual-Door Onboarding Model, and Database Provisioning** from `section_06_registration_flow.md` in **2 high-impact, standard slides**.

---

### Slide 1: The Hybrid Strategy & Dual-Door Onboarding Model

* **Slide Title:** Registration Flow: Hybrid Authentication Architecture
* **Subtitle:** 100% Market Coverage: Google OAuth 2.0 + Universal Work Email & Password
* **Layout:** The Enterprise Reality Box + Dual-Door Flowchart

#### The Strategic Problem Solved:
> *Over 70% of manufacturing enterprises run on Microsoft 365 / Azure AD / Outlook. Corporate buyers with emails like `vikram@tataforge.com` cannot use Google OAuth. ProcureAI adopts a Hybrid Auth Model to guarantee 100% addressable market coverage.*

#### Visual Dual-Door Flowchart (Include on Slide):
```text
┌────────────────────────────────────────────────────────────────────────┐
│                        USER ARRIVES AT APP                             │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
     ┌─────────────────────────────┐ ┌─────────────────────────────┐
     │ DOOR 1: COMPANY CREATOR     │ │ DOOR 2: INVITED STAFF       │
     │ (Admin Registration)        │ │ (Staff Onboarding)          │
     ├─────────────────────────────┤ ├─────────────────────────────┤
     │ • Creates NEW Organization  │ │ • Joins EXISTING Org        │
     │ • Assigned role = 'admin'   │ │ • Uses Tokenized Invite Link│
     │ • Option A: Google OAuth    │ │ • Option A: Google OAuth    │
     │ • Option B: Work Email+Pwd  │ │ • Option B: Work Email+Pwd  │
     └──────────────┬──────────────┘ └──────────────┬──────────────┘
                    │                               │
                    └───────────────┬───────────────┘
                                    ▼
                    ┌───────────────────────────────┐
                    │ ATOMIC DATABASE PROVISIONING  │
                    │ 1. Creates Org + User         │
                    │ 2. Issues Signed Session JWT  │
                    │ 3. Redirects to Role Dashboard│
                    └───────────────────────────────┘
```

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, this slide covers our Registration and Authentication architecture. In manufacturing, over 70% of companies use Microsoft 365 or private corporate emails. If we only supported Google login, we would lose most of our enterprise market. Therefore, we built a Hybrid Authentication system: 1-click Google OAuth for startups, and universal Email plus Password with Bcrypt hashing for corporate domains.*
>
> *Users enter through two distinct doors: Door 1 allows business owners to register a new company as Admin. Door 2 allows staff members to join an existing company via invite links. Staff never create duplicate companies."*

---

### Slide 2: End-to-End Registration Flow & Future-Proof Schema

* **Slide Title:** Registration Sequence & Database Schema Provisioning
* **Subtitle:** "Verify First, Persist Second" Security with Atomic SQL Transactions
* **Layout:** Split View: End-to-End Sequence (Left) vs. Schema & Multi-Org Support (Right)

#### Slide Content:

```text
┌──────────────────────────────────────┐  ┌──────────────────────────────────────┐
│ 🔄 REGISTRATION EXECUTION PIPELINE   │  │ 🗄️ DATABASE SCHEMA & MULTI-ORG      │
├──────────────────────────────────────┤  ├──────────────────────────────────────┤
│ 1. Method A: Google OAuth 2.0        │  │ • Hybrid Users Table Design:         │
│    • Client gets Google ID Token     │  │   - auth_provider: 'local'|'google'  │
│    • Backend verifies signature via  │  │   - password_hash: Bcrypt (10 rounds)│
│      google-auth-library (OIDC)      │  │   - google_sub: Immutable Google ID │
│    • "Verify First, Persist Second"  │  │                                      │
│                                      │  │ • Scoped Uniqueness:                 │
│ 2. Method B: Work Email & Password   │  │   CONSTRAINT UNIQUE (org_id, email)  │
│    • Validates min 8 characters      │  │                                      │
│    • Hashes password with Bcrypt     │  │ • Future-Proofing Staff Members:     │
│      (10 salt rounds)                │  │   If Rahul (Negotiator at Company A) │
│                                      │  │   starts his own Company B later,    │
│ 3. Atomic SQL Transaction:           │  │   he can use the SAME email with an  │
│    BEGIN -> Insert Org -> Insert User│  │   instant Workspace Switcher!        │
│    -> COMMIT (Zero orphaned rows)   │  │                                      │
│                                      │  │ • Signed Session JWT:                │
│ 4. Issues Session JWT (7-Day Expiry):│  │   Claims: org_id, user_id, role.     │
│    { userId, orgId, role, email }    │  │   Enforces tenant isolation on APIs. │
└──────────────────────────────────────┘  └──────────────────────────────────────┘
```

#### Key Engineering Highlights:
* **Atomic Consistency:** Registration is enclosed in a single database transaction (`BEGIN ... COMMIT`). If creating the user fails, the organization creation rolls back automatically.
* **Workspace Switcher:** The `UNIQUE (org_id, email)` constraint allows one professional email to hold different roles across different companies over time.

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, on the technical implementation: For Google users, we follow the 'Verify First, Persist Second' standard—we cryptographically verify the Google token signature before writing any data. For email users, passwords are encrypted using Bcrypt with 10 salt rounds.*
>
> *Everything runs inside an atomic SQL transaction: the organization and root admin user are created together, eliminating broken or orphaned records. Finally, our schema uses scoped uniqueness on `(org_id, email)`. This means if a staff buyer later starts their own manufacturing company, they can use the same email and switch between companies effortlessly with our built-in Workspace Switcher."*
