# Behavioral & Deployment Diagrams

**Document:** 11-behavioral-diagrams.md
**Version:** 1.0
**Status:** Locked — Phase 1, Session 6
**Last Updated:** 2026-10-13
**Tool:** Mermaid

---

## 1. Purpose

UML **structural** diagrams (use case, class, ER) were covered in document 06. This document covers **behavioral** diagrams — how the system *acts* over time — plus the **deployment** diagram that shows how the pieces fit together at runtime.

---

## 2. Sequence Diagrams

Sequence diagrams show **the flow of a single interaction** between actors and system components, ordered by time.

### 2.1 Admin Login Flow

```mermaid
sequenceDiagram
    autonumber
    actor A as Admin
    participant B as Browser
    participant F as Flask App
    participant DB as Database

    A->>B: Visit /admin/login
    B->>F: GET /admin/login
    F->>F: Generate CSRF token
    F-->>B: Render login form + token

    A->>B: Enter email + password
    B->>F: POST /admin/login (form + CSRF)
    F->>F: Validate CSRF token
    alt Invalid CSRF
        F-->>B: 400 Bad Request
    end

    F->>F: Validate form fields
    alt Invalid input
        F-->>B: Re-render form with errors
    end

    F->>DB: SELECT * FROM users WHERE email=?
    DB-->>F: User row (or none)

    alt User not found
        F-->>B: Re-render form: "Invalid credentials"
    end

    F->>F: check_password_hash(input, stored_hash)
    alt Password mismatch
        F-->>B: Re-render form: "Invalid credentials"
    end

    F->>DB: UPDATE users SET last_login=now
    F->>F: Create session (login_user)
    F-->>B: 302 Redirect → /admin/
    B->>F: GET /admin/
    F-->>B: Render dashboard
```

**Notes:**
- **CSRF validation happens before** database queries.
- **Same error message** for "user not found" and "wrong password" — prevents username enumeration.
- **Session created server-side** using Flask-Login.

---

### 2.2 Contact Form Submission

```mermaid
sequenceDiagram
    autonumber
    actor V as Visitor
    participant B as Browser
    participant F as Flask App
    participant DB as Database
    participant M as Mail Service

    V->>B: Visit /contact
    B->>F: GET /contact
    F-->>B: Render form + CSRF token

    V->>B: Fill + submit form
    B->>F: POST /contact (form + CSRF)
    F->>F: Validate CSRF
    F->>F: Validate fields (name, email, subject, message)

    alt Invalid
        F-->>B: Re-render with errors
    end

    F->>DB: INSERT INTO contact_submissions
    DB-->>F: ID

    F-)M: Send notification email (async)
    F-)M: Send acknowledgment email (async)
    Note over F,M: Email failures do not block response

    F-->>B: Redirect to /contact?status=success
    B->>F: GET /contact?status=success
    F-->>B: Render success message

    V->>B: Sees confirmation
```

**Notes:**
- `-)` denotes **asynchronous** call — email sending doesn't block the response.
- If email fails, the submission is still saved. Logged for review.
- Rate limiting applied (Phase 5).

---

### 2.3 Project Detail Fetch (Public)

```mermaid
sequenceDiagram
    autonumber
    actor V as Visitor
    participant B as Browser
    participant F as Flask App
    participant DB as Database

    V->>B: Click project card
    B->>F: GET /projects/car-price-prediction
    F->>F: Extract slug from URL
    F->>DB: SELECT * FROM projects WHERE slug=? AND is_public=1
    DB-->>F: Project row

    alt Not found
        F-->>B: 404 page
    end

    F->>DB: SELECT * FROM project_images WHERE project_id=? ORDER BY display_order
    DB-->>F: Image list

    F->>DB: SELECT related projects (top 3)
    DB-->>F: Related rows

    F->>F: Render template with data
    F-->>B: HTML response
    B-->>V: Rendered project page
```

**Notes:**
- **Three queries** for one page — but each is a simple indexed lookup. Fast.
- Could be optimized into a single join + subquery if needed later.
- **Related projects** add stickiness — visitor explores more.

---

## 3. Activity Diagrams

Activity diagrams show **the full flow of a multi-step process** with branching logic.

### 3.1 Admin Adds a New Project

```mermaid
flowchart TD
    Start([Admin visits /admin/projects]) --> List[See list of all projects]
    List --> ClickAdd[Click 'Add New Project']
    ClickAdd --> Form[Empty form rendered]
    Form --> Fill[Admin fills: title, slug, description, tech, links]
    Fill --> Submit[Click 'Save']

    Submit --> CSRF{CSRF valid?}
    CSRF -->|No| Error1[Show error]
    CSRF -->|Yes| Validate{Fields valid?}

    Validate -->|No| ShowErr[Show field errors]
    ShowErr --> Form

    Validate -->|Yes| SlugUnique{Slug unique?}
    SlugUnique -->|No| SlugErr[Show 'slug exists' error]
    SlugErr --> Form

    SlugUnique -->|Yes| Insert[INSERT INTO projects]
    Insert --> Flash[Flash 'Project created']
    Flash --> Redirect[Redirect to projects list]
    Redirect --> List

    style Start fill:#ECFDF5
    style Insert fill:#D1FAE5
    style Error1 fill:#FEE2E2
    style ShowErr fill:#FEE2E2
    style SlugErr fill:#FEE2E2
```

**Notes:**
- **Three validation gates:** CSRF → field validation → slug uniqueness
- **Loop back to form** on any error — user's input preserved
- **Flash message** confirms success

---

### 3.2 Visitor Browses Projects with Filter

```mermaid
flowchart TD
    Start([Visitor at /projects]) --> Load[Page loads]
    Load --> Fetch[Fetch all projects from DB]
    Fetch --> Render[Render all project cards]
    Render --> Wait[Wait for user action]

    Wait --> Click{User clicks filter?}
    Click -->|Yes| Filter[JS: filter cards by tech]
    Filter --> Show[Show matching cards, hide others]
    Show --> Wait

    Click -->|No, clicked project| Detail[Navigate to /projects/slug]
    Detail --> End([View project detail])

    Click -->|No, leaves| Leave([Exit])

    style Filter fill:#FEF3C7
    style Show fill:#D1FAE5
```

**Notes:**
- **Filter is client-side** — no server round-trip.
- Fast and smooth for ~10 projects; would need server-side for 100+.
- URL doesn't change (could use `?tech=python` for shareability later).

---

### 3.3 Toggle Dark Mode

```mermaid
flowchart TD
    Start([Page loads]) --> Check{localStorage has theme?}
    Check -->|Yes| Apply[Apply stored theme]
    Check -->|No| System{prefers-color-scheme?}
    System -->|Dark| ApplyDark[Apply dark]
    System -->|Light| ApplyLight[Apply light]

    Apply --> Done[Page rendered]
    ApplyDark --> Done
    ApplyLight --> Done

    Done --> Click{User clicks toggle?}
    Click -->|Yes| Toggle[Toggle data-theme attribute]
    Toggle --> Save[Save to localStorage]
    Save --> Done

    Click -->|No| Done

    style Apply fill:#D1FAE5
    style ApplyDark fill:#1E293B,color:#fff
    style ApplyLight fill:#F8FAFC
```

**Notes:**
- **Priority:** stored preference → system preference → light default
- **Applied before render** to prevent flash of incorrect theme (FOUC)
- Script placed in `<head>` inline to avoid blocking

---

## 4. Deployment Diagram

Shows **where code runs**, from the visitor's browser to the database.

```mermaid
flowchart TB
    subgraph Client["Client (Visitor's Device)"]
        Browser[Web Browser<br/>Chrome / Firefox / Safari]
    end

    subgraph Render["Render Platform (Free Tier)"]
        subgraph Web["Web Service"]
            Gunicorn[Gunicorn<br/>WSGI Server]
            Flask[Flask App<br/>+ Blueprints]
            Static[Static Files<br/>CSS / JS / Images]
        end
        subgraph Data["Data Layer"]
            PG[(PostgreSQL<br/>Production DB)]
        end
    end

    subgraph External["External Services"]
        GitHub[GitHub<br/>Source + CI/CD Hook]
        Mail[SMTP Service<br/>Gmail / SendGrid]
        Fonts[Google Fonts CDN]
    end

    subgraph Dev["Development Machine"]
        VSCode[VS Code]
        LocalFlask[Local Flask<br/>127.0.0.1:5000]
        SQLite[(SQLite<br/>Dev DB)]
    end

    Browser -->|HTTPS| Gunicorn
    Gunicorn --> Flask
    Flask --> PG
    Flask --> Mail
    Browser -.->|Fonts| Fonts
    Browser -.->|Static assets| Static

    GitHub -->|Deploy on push| Gunicorn

    VSCode -.->|Edit locally| LocalFlask
    LocalFlask -.-> SQLite

    classDef dev fill:#FEF3C7
    classDef prod fill:#D1FAE5
    class VSCode,LocalFlask,SQLite dev
    class Gunicorn,Flask,Static,PG prod
```

**Notes:**

| Component | Role |
|---|---|
| **Browser** | Renders HTML/CSS/JS, calls HTTPS |
| **Render** | Hosts production Flask app + PostgreSQL |
| **Gunicorn** | WSGI server — runs Flask workers |
| **Flask** | Application — routes, templates, business logic |
| **PostgreSQL** | Production database |
| **GitHub** | Source control + auto-deploy on push |
| **Google Fonts** | Font delivery via CDN |
| **Local machine** | Dev environment (SQLite, local Flask) |

**Deploy trigger:** Push to `main` → Render auto-builds → runs migrations → restarts Gunicorn.

---

## 5. Environment Comparison

| Aspect | Development | Production |
|---|---|---|
| **URL** | `127.0.0.1:5000` | `nadeemahmed.dev` (or Render subdomain) |
| **WSGI server** | Flask dev server | Gunicorn |
| **Database** | SQLite | PostgreSQL |
| **Debug mode** | `True` | `False` |
| **HTTPS** | No | Yes (auto by Render) |
| **Environment vars** | `.env` file | Render dashboard |
| **Static files** | Served by Flask | Served by Gunicorn / CDN |
| **Logs** | Console | Render logs dashboard |
| **Auto-deploy** | N/A | Push to `main` triggers |

**The app code is identical.** Only configuration differs — this is what "12-factor app" means.

---

## 6. Error Handling Flow

Not drawn as a diagram, but documented here as a sequence rule:

| Error Type | Where Handled | User Sees |
|---|---|---|
| **404 Not Found** | `@app.errorhandler(404)` | Custom 404 page |
| **500 Server Error** | `@app.errorhandler(500)` | Custom 500 page + logged |
| **CSRF failure** | Flask-WTF | 400 + flash "Session expired" |
| **Form validation** | Flask-WTF validators | Form re-rendered with errors |
| **DB connection lost** | Global error handler | 503 + retry message |
| **Email failure** | Try/except in mail helper | Silent — logged only |

**Principle:** Never show a stack trace to users. Log it, show a friendly page.

---

## 7. Performance Considerations

| Interaction | Target | Notes |
|---|---|---|
| Home page load | < 2s | Cached DB queries, minimized assets |
| Project detail | < 1.5s | Pre-loaded relations |
| Login | < 500ms | Single indexed query |
| Contact form submit | < 1s | Async email |
| Static asset load | < 200ms | CDN-cached on Render |

**Caching strategy (future):**
- Cache home page for 5 min (Flask-Caching)
- Invalidate on admin edit
- Static assets: 1-year cache header

**Not implemented in v1.0** — deferred to Phase 5.

---

## 8. Security Boundaries

| Boundary | Protection |
|---|---|
| **Browser → Server** | HTTPS (Render auto) |
| **Form submissions** | CSRF tokens (Flask-WTF) |
| **Passwords** | Werkzeug hashing (SHA-256 + salt) |
| **Admin routes** | `@login_required` decorator |
| **SQL injection** | SQLAlchemy parameterized queries |
| **XSS** | Jinja2 auto-escaping |
| **Secrets** | Environment variables (never in repo) |

---

## 9. Change Log

| Date | Change |
|---|---|
| 2026-10-13 | Initial version — Phase 1, Session 6 |