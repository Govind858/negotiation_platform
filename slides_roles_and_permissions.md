# Presentation Slides Content: Roles & Permissions (RBAC)
## Ready-to-Use Content for Google Slides & Gemini

Use this structured content directly in Google Slides (or copy-paste into Gemini in Google Slides). It covers the **4-Role Hierarchy, Permissions Matrix, and Governance Security** in **2 clean, standard, doubt-free slides**.

---

### Slide 1: The 4 Enterprise Roles & Operational Hierarchy

* **Slide Title:** Governance & Access: The 4 System Roles
* **Subtitle:** Clear Operational Boundaries from Executive Suite to Factory Floor
* **Layout:** 4 Horizontal Persona Cards with Clean Icons & Badges

#### Visual Hierarchy Cards (Include on Slide):

```text
┌──────────────────────────────┐  ┌──────────────────────────────┐
│ 👑 1. ADMIN                  │  │ 👔 2. MANAGER                │
│ Target: Business Owner / VP  │  │ Target: Procurement Lead     │
├──────────────────────────────┤  ├──────────────────────────────┤
│ • Full company settings      │  │ • Team oversight & reviews   │
│ • Subscription & billing     │  │ • Approves ceiling exceptions│
│ • Invite/remove any user     │  │ • Invites buyers & viewers   │
│ • Company-wide financial ROI │  │ • Full visibility into deals │
└──────────────────────────────┘  └──────────────────────────────┘

┌──────────────────────────────┐  ┌──────────────────────────────┐
│ 🎯 3. NEGOTIATOR             │  │ 👁️ 4. VIEWER                 │
│ Target: Staff Buyer / Sourcing│ │ Target: Finance / Auditor    │
├──────────────────────────────┤  ├──────────────────────────────┤
│ • Fills intake questionnaire │  │ • 100% Read-Only access      │
│ • Receives AI Battlecards    │  │ • Searches historical prices │
│ • Logs meeting call rounds   │  │ • Inspects closed deals      │
│ • Marks deals Won or Lost    │  │ • Reviews audit scorecards   │
└──────────────────────────────┘  └──────────────────────────────┘
```

#### Key Governance Principle:
* **Principle of Least Privilege:** Junior buyers get all the tactical AI tools they need to negotiate without having access to company billing, user management, or sensitive contract deletion.

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, this slide outlines our governance architecture. Manufacturing companies require strict separation of duties. We established 4 clear enterprise roles: Admin for business owners and VPs, Manager for procurement team leads, Negotiator for active buyers, and Viewer for finance and auditors. This ensures staff only have access to what they need for their daily job."*

---

### Slide 2: The RBAC Permissions Matrix & Security Guardrails

* **Slide Title:** Role-Based Access Control (RBAC) Permissions Matrix
* **Subtitle:** Fine-Grained API & Database Guardrails Protecting Commercial Secrets
* **Layout:** Clean Comparison Matrix Table + 2 Security Highlights

#### Slide Permissions Matrix Table:

| System Capability & API Action | `admin` | `manager` | `negotiator` | `viewer` |
|---|:---:|:---:|:---:|:---:|
| **Manage Company Settings & Billing** | ✅ | ❌ | ❌ | ❌ |
| **Invite Staff Members** | ✅ *(All)* | ✅ *(Buyers/Viewers)* | ❌ | ❌ |
| **Deactivate / Remove Staff** | ✅ | ❌ | ❌ | ❌ |
| **Run Intake Questionnaire & Trigger AI** | ✅ | ✅ | ✅ | ❌ |
| **Log Call Rounds & Close Deals (Won/Lost)**| ✅ | ✅ | ✅ | ❌ |
| **Search Historical Deal Memory & Prices** | ✅ | ✅ | ✅ | ✅ |
| **View Company-Wide Savings Analytics** | ✅ | ✅ | ✅ *(Full Visibility)* | ✅ |

#### 2 Core Security Highlights:
1. **Dual-Layer Enforcement:** Permissions are validated twice—first at the API Gateway level via signed JWT claims (`req.user.role`), and second at the database level via PostgreSQL Row-Level Security.
2. **Transparent Motivation:** By default, all roles (including `negotiator`) can view company-wide financial cost savings to encourage healthy team gamification and cross-category benchmarking, with an optional admin toggle for executive confidentiality.

#### 🎙️ Speaker Notes (What to say to Sir):
> *"Sir, here is our exact permissions matrix. Everything is enforced at both the API level and the database level. For example, creating negotiations and closing deals is reserved for buyers and managers, while finance viewers have read-only access. Negotiators have full visibility into company-wide savings to motivate performance, but cannot touch billing, user accounts, or company settings."*
