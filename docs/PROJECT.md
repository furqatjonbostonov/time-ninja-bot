# Project: Telegram Task & Reminder Bot + Mini App (Central Asia)

## Architecture Overview
A production-grade, 100% free-tier cloud architecture tailored for the Central Asian market (Uzbekistan, Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan), delivering a high-performance Telegram Task & Reminder system (Telegram Bot + Telegram Mini App).

```
                      +---------------------------------------+
                      |         Telegram Client (User)        |
                      +---------------------------------------+
                                  /                \
          Telegram Bot Updates   /                  \  HTTPS (Mini App Webview)
          (Webhook POST)        /                    \
                               v                      v
                +-------------------------+  +-------------------------+
                |  Telegram Cloud Servers |  | Cloudflare Pages (CDN)  |
                +-------------------------+  | Static React/TS Mini App|
                             |               | Tashkent & Almaty Edges |
                  HTTPS Webhook Push         +-------------------------+
                             v                            |
                +---------------------------------------+ |
                |      Cloudflare Workers (Edge API)    |<+
                |  - Bot Command Router & FSM           | (REST API + HMAC initData)
                |  - WebApp API & Auth Gateway          |
                |  - Rate Limiter (Token Bucket)        |
                +---------------------------------------+
                     |                     ^
         pg / REST   |                     | Scheduled Trigger (1 min)
                     v                     |
       +-------------------------+   +-----------------------------+
       | Supabase (PostgreSQL)   |   | Cloudflare Cron Triggers    |
       | - 500 MB Free Tier      |   | + Upstash QStash (Delayed)  |
       | - Supavisor Pooler:6543 |   | + Cron-job.org (Fallback)   |
       | - Row Level Security    |   +-----------------------------+
       +-------------------------+
```

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| F01 | Bot Command Navigation | Core bot commands (/start, /help, /tasks, /today, /add, /settings) with inline keyboards and persistent Menu Button | M1 (TZ.md) | Explorer 1 |
| F02 | Deep Linking Navigation | Deep linking support (`tg://resolve?domain=...&startapp=task_<uuid>`) directly opening specific tasks in TMA | M1 (TZ.md) | Explorer 1 |
| F03 | Fallback Text / FSM Mode | Full conversational task management in bot chat without opening TMA for slow connections or low-end devices | M1 (TZ.md) | Explorer 1 |
| F04 | NLP Quick Add Parser | Regex & NLP parser for fast text task entry (e.g., "Ertaga soat 10:00 da hisobot topshirish") | M1 (TZ.md) | Explorer 1 |
| F05 | TMA Dashboard Page | Central dashboard showing today's tasks, overdue count, completion progress bar, quick filter tabs, and Add button | M1 (TZ.md) | Explorer 1 |
| F06 | TMA Task Creation & Edit Modal | Rich task creation/edit modal with title, description, category selector, due date/time picker, reminder offsets, and recurrence | M1 (TZ.md) | Explorer 1 |
| F07 | TMA Calendar & Timeline Page | Monthly/weekly calendar grid and daily hourly timeline view showing scheduled tasks and deadlines | M1 (TZ.md) | Explorer 1 |
| F08 | TMA Categories & Tags Page | Customizable task categories with color tags, icons, task counts, and custom tag creation | M1 (TZ.md) | Explorer 1 |
| F09 | TMA User Settings Page | User preferences for language, default reminder offset, quiet hours, sound, and notification delivery channels | M1 (TZ.md) | Explorer 1 |
| F10 | TMA Premium Upgrade Page | In-app comparison of Free vs Premium tiers, subscription selector, and native payment checkout buttons | M1 (TZ.md) | Explorer 1 |
| F11 | Telegram Mini App Native SDK Integration | Deep integration with `@telegram-apps/sdk` (viewport expansion, theme matching, HapticFeedback, back button handling) | M1 (TZ.md) | Explorer 1 |
| F12 | Task Lifecycle & State Machine | 5-state lifecycle (pending, in_progress, completed, overdue, cancelled) with strict state transition validation | M1 (TZ.md) | Explorer 1 |
| F13 | Recurrence Engine (RRULE) | RFC 5545 recurrence rules (daily, weekdays, weekly, monthly, custom intervals) with automated next-occurrence generation | M1 (TZ.md) | Explorer 1 |
| F14 | Multi-Stage Notification Pipeline | 5-stage reminder dispatch (T-24h, T-1h, T-15m, T=0, T+1h overdue follow-up) with interactive action buttons | M1 (TZ.md) | Explorer 1 |
| F15 | Interactive Reminder Actions | Bot reminder messages with inline buttons: Complete, Snooze (15m/1h), Postpone to Tomorrow, Open in Mini App | M1 (TZ.md) | Explorer 1 |
| F16 | Central Asian Timezone Engine | Explicit support for Asia/Tashkent (UTC+5), Asia/Samarkand (UTC+5), Asia/Almaty (UTC+5 unified), Asia/Bishkek (UTC+6) with zero DST | M1 (TZ.md) | Explorer 1 |
| F17 | Multi-Language Localization | 4-language interface (Uzbek Latin, Uzbek Cyrillic, Russian, English) for bot messages and Mini App UI | M1 (TZ.md) | Explorer 1 |
| F18 | Production Relational Schema (PostgreSQL DDL) | Robust DDL schema for users, categories, tasks, task_reminders, and subscriptions with indexes and constraints | M1 (TZ.md) | Explorer 1 |
| F19 | Cloudflare Workers Edge Backend | 100% free serverless backend (100k req/day, 0ms cold start, TypeScript/Hono, commercial use permitted) | M2 (ARCHITECTURE.md) | Explorer 2 |
| F20 | Cloudflare Pages Frontend Hosting | 100% free static Mini App hosting (unlimited requests/bandwidth, edge nodes in Tashkent & Almaty) | M2 (ARCHITECTURE.md) | Explorer 2 |
| F21 | Supabase Serverless Database | 100% free managed PostgreSQL (500 MB storage, Supavisor connection pooling on port 6543, RLS, 50k MAU) | M2 (ARCHITECTURE.md) | Explorer 2 |
| F22 | Dual Cron & Scheduled Reminder Engine | Cloudflare Cron Triggers (1-min edge cron) + Cron-job.org external backup pinger + Upstash QStash delayed queue | M2 (ARCHITECTURE.md) | Explorer 2 |
| F23 | Free Tier Quota Limits & Cost Optimization | Exhaustive catalog of quotas, storage calculations (~1.5M tasks in 500MB), data archival policies, $0/month budget guarantee | M2 (ARCHITECTURE.md) | Explorer 2 |
| F24 | High-Concurrency Connection Pooling | Supavisor transaction pooling preventing connection exhaustion during serverless concurrent invocations | M2 (ARCHITECTURE.md) | Explorer 2 |
| F25 | Cold Start Elimination Architecture | Architectural blueprint eliminating 50s cold start timeouts and 750-hr monthly exhaustion present in container hosts | M2 (ARCHITECTURE.md) | Explorer 2 |
| F26 | Telegram WebApp initData HMAC-SHA256 Validation | Strict cryptographic authentication deriving SecretKey from "WebAppData" + bot_token, constant-time equality, 24h replay cutoff | M3 (SECURITY.md) | Explorer 3 |
| F27 | Webhook Ingress Defense & Secret Token | Ingress filtering using `X-Telegram-Bot-Api-Secret-Token` header, Telegram official CIDR filtering, fast 200 OK acknowledgment | M3 (SECURITY.md) | Explorer 3 |
| F28 | Anti-DDoS & Cloudflare Edge Protection | Cloudflare Free WAF rules, Bot Fight Mode, TLS 1.3, HTTP/2/3 edge protection against layer 7 DDoS | M3 (SECURITY.md) | Explorer 3 |
| F29 | Multi-Layer Rate Limiting & Bot Throttling | Edge IP rate limiting (100 req/10s), Token Bucket API rate limiting, and Telegram outbound leaky bucket (25 msg/s global, 1 msg/s chat) | M3 (SECURITY.md) | Explorer 3 |
| F30 | Tenant Scoping & Anti-IDOR Security | Zero-trust authentication binding, UUIDv4 task identifiers, mandatory tenant-scoped SQL queries (`WHERE user_id = :authUserId`) | M3 (SECURITY.md) | Explorer 3 |
| F31 | Central Asia Market Dynamics & Monetization Strategy | Detailed demographic, mobile-first banking, and willingness-to-pay analysis for Uzbekistan, Kazakhstan, and wider Central Asia | M4 (MONETIZATION.md) | Explorer 3 |
| F32 | Model 1: Freemium + Premium Subscription | Tiered feature matrix (Free vs Premium: unlimited tasks, recurring rules, voice-to-text, calendar sync, custom themes) | M4 (MONETIZATION.md) | Explorer 3 |
| F33 | Model 2: Hyper-Local Native Advertising | Sponsored reminder channels, local merchant discount banners, non-intrusive affiliate integration for free users | M4 (MONETIZATION.md) | Explorer 3 |
| F34 | Model 3: Pay-Per-Feature & Micro-Billing | Micro-transaction packs for AI task breakdown, SMS notification backups via regional gateways (Eskiz.uz), export reports | M4 (MONETIZATION.md) | Explorer 3 |
| F35 | Local Payment Gateway: Click.uz Integration | Click Shop API merchant protocol (Prepare and Complete action signatures, MD5/HMAC verification, status codes) | M4 (MONETIZATION.md) | Explorer 3 |
| F36 | Local Payment Gateway: Payme (Inspire Group) | Payme JSON-RPC 2.0 merchant protocol (CheckPerformTransaction, CreateTransaction, PerformTransaction, Soliq IKPU receipt code `10899001001000000`) | M4 (MONETIZATION.md) | Explorer 3 |
| F37 | Local Payment Gateway: Uzum Pay & Kaspi Pay | Uzum Bank QR/API checkout in Uzbekistan; Kaspi Pay / QR deep links and Halyk Epay in Kazakhstan | M4 (MONETIZATION.md) | Explorer 3 |
| F38 | Native In-App Currency: Telegram Stars | Telegram Stars (`XTR`) digital goods integration via Bot API 7.4+ `createInvoiceLink` / `sendInvoice`, zero-bureaucracy legal setup | M4 (MONETIZATION.md) | Explorer 3 |
| F39 | Localized Pricing Matrices & Unit Economics | Realistic regional pricing tiers in UZS (15,000-25,000 UZS/mo), KZT (790-1,200 KZT/mo), and Telegram Stars (50-75 Stars/mo) | M4 (MONETIZATION.md) | Explorer 3 |
| F40 | Executive Summary & Project Master Navigation | Master documentation index, technical navigation, system topology summary, deployment roadmap in README.md | M5 (README.md) | Synthesis |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Texnik Topshiriq (TZ.md) | Telegram Mini App UI/UX & Bot message logic, task lifecycle, notification sequence, database DDL, NFRs | Survey completed | IN_PROGRESS (8a14497f) |
| M2 | Bepul Infratuzilma Arxitekturasi (ARCHITECTURE.md) | 100% Free Cloud Infrastructure (Cloudflare Workers, Pages, Supabase, Cron/QStash), quotas, topology | Survey completed | IN_PROGRESS (9daaf1a2) |
| M3 | Kuchli Himoya va Xavfsizlik (SECURITY.md) | Telegram WebApp initData HMAC-SHA256, Webhook security, DDoS, Rate Limiting, Anti-IDOR | Survey completed | IN_PROGRESS (06ea3bea) |
| M4 | Monetizatsiya Strategiyasi (MONETIZATION.md) | Central Asia monetization models, Click, Payme, Uzum, Kaspi, Telegram Stars, pricing matrices | Survey completed | IN_PROGRESS (467f78a9) |
| M5 | Tizim Umumiy Qo'llanmasi (README.md) | Executive summary, master navigation, architecture diagram, deployment roadmap | M1, M2, M3, M4 | PLANNED |
| M6 | Sifat Nazorati va Audit (VERIFICATION & AUDIT) | Full independent verification of all Acceptance Criteria, adversarial review, forensic audit | M1, M2, M3, M4, M5 | PLANNED |

## Interface Contracts
### Mini App Frontend (Cloudflare Pages) ↔ Backend API (Cloudflare Workers)
- **Protocol**: HTTPS / REST JSON + Server-Sent Events (optional)
- **Authentication**: `Authorization: tma <raw_initData>` header on every API request.
- **Payload validation**: Backend validates HMAC-SHA256 before granting access to tenant resources.
- **Endpoints**:
  - `GET /api/v1/tasks` (Filter by date, category, status)
  - `POST /api/v1/tasks` (Create new task with reminder schedules)
  - `GET /api/v1/tasks/:id` (Get task detail)
  - `PATCH /api/v1/tasks/:id` (Update task, mark completed, reschedule)
  - `DELETE /api/v1/tasks/:id` (Soft-delete or purge task)
  - `GET /api/v1/categories` (Fetch user categories)
  - `GET /api/v1/user/settings` (Fetch notification preferences & timezone)
  - `PATCH /api/v1/user/settings` (Update timezone, quiet hours, language)

### Telegram Servers ↔ Backend Bot Gateway (Cloudflare Workers)
- **Protocol**: HTTPS Webhook POST
- **Security**: Header `X-Telegram-Bot-Api-Secret-Token: <SECRET_STRING>`
- **Response**: Immediate `HTTP 200 OK` within <100ms.

### Scheduler (Cloudflare Cron / Cron-job.org) ↔ Backend Reminder Dispatcher
- **Protocol**: HTTPS GET / Scheduled Event
- **Endpoint**: `/api/cron/dispatch-reminders`
- **Security**: Secret Bearer Token `CRON_SECRET_KEY` in Authorization header.
- **Execution**: Queries Supabase with `FOR UPDATE SKIP LOCKED`, batches outgoing alerts through Leaky Bucket queue.

## Document & Workspace Layout
```
telegram_task_bot/
├── ORIGINAL_REQUEST.md          # Immutable user requirements
├── PROJECT.md                   # Global project architecture & feature index
├── TZ.md                        # Milestone 1: Comprehensive Technical Specification
├── ARCHITECTURE.md              # Milestone 2: 100% Free Cloud Infrastructure Blueprint
├── SECURITY.md                  # Milestone 3: Cryptographic Validation & Cybersecurity
├── MONETIZATION.md              # Milestone 4: Central Asian Monetization & Payment Rails
├── README.md                    # Milestone 5: Executive Summary & System Navigation
└── .agents/teamwork/            # Agent metadata & execution logs
    ├── orchestrator_1/          # DISPATCH.md, BRIEFING.md, plan.md, progress.md, GATE_STATUS.md
    └── ...                      # Subagent workspaces
```
