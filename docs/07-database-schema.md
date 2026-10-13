# Database Schema

**Document:** 07-database-schema.md
**Version:** 1.0
**Status:** Locked — Phase 1, Session 3
**Last Updated:** 2026-10-13

---

## 1. Purpose

This document defines the complete database schema for the portfolio website. Every table, column, data type, constraint, and relationship is specified here. It is the single source of truth for the SQLAlchemy models (V0.4) and migrations.

---

## 2. Design Principles

| Principle | Rule |
|---|---|
| **Dev/Prod parity** | SQLite for development, PostgreSQL for production — same schema |
| **Timestamps** | Every table has `created_at`; mutable tables also have `updated_at` |
| **Soft references** | Store `display_order` (int) instead of relying on insertion order |
| **Cascade carefully** | CASCADE for owned children; SET NULL for audit trail |
| **No business logic in DB** | Constraints at app level (Flask), not DB (for portability) |
| **Nullable by default** | Only require fields that truly must exist |
| **Store raw, display processed** | Keep subject marks; don't display publicly |

---

## 3. Conventions

| Aspect | Convention |
|---|---|
| Table names | `snake_case`, plural (`projects`, not `Project`) |
| Column names | `snake_case` (`created_at`, not `createdAt`) |
| Primary key | `id` (auto-increment integer) |
| Foreign key | `<parent>_id` (`project_id`, `semester_id`) |
| Booleans | `is_*` prefix (`is_featured`, `is_active`) |
| Timestamps | `*_at` suffix (`created_at`, `published_at`) |
| Dates | `*_date` suffix (`start_date`, `issue_date`) |
| URL slugs | `slug` column with UNIQUE constraint |

---

## 4. Tables Overview

| # | Table | Type | Public | Rows |
|---|---|---|---|---|
| 1 | `users` | Auth | ❌ | 1 |
| 2 | `profile` | Singleton | ✅ read | 1 |
| 3 | `education` | Entity | ✅ | 1–3 |
| 4 | `semesters` | Child | ⚠️ partial | 8 |
| 5 | `subjects` | Child | ❌ | ~40 |
| 6 | `skills` | Entity | ✅ | 30+ |
| 7 | `projects` | Entity | ✅ | 4–10 |
| 8 | `project_images` | Child | ✅ | 3–10 |
| 9 | `experience` | Entity | ✅ | 0+ |
| 10 | `certifications` | Entity | ✅ | 2+ |
| 11 | `courses` | Entity | ✅ | 2+ |
| 12 | `social_links` | Entity | ✅ | 4–6 |
| 13 | `posts` | Entity | ⏸️ deferred | 0+ |
| 14 | `contact_submissions` | Audit | ❌ | 0+ |
| 15 | `settings` | Key-Value | ❌ | 5–10 |

---

## 5. Table Definitions

### 5.1 `users`

Admin authentication. Only one row in practice.

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `email` | VARCHAR(120) | UNIQUE, NOT NULL | |
| `password_hash` | VARCHAR(255) | NOT NULL | Werkzeug generate_password_hash |
| `created_at` | DATETIME | DEFAULT now | |
| `last_login` | DATETIME | NULL | Updated on each login |

**Indexes:** `email` (unique)
**Notes:** No `username` — email is the identifier.

---

### 5.2 `profile`

Single-row table (id always = 1). Store all personal branding fields.

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `full_name` | VARCHAR(100) | NOT NULL | "Nadeem Ahmed Ghoto" |
| `title` | VARCHAR(120) | NOT NULL | "AI/ML Student & Aspiring Engineer" |
| `tagline` | VARCHAR(200) | NULL | LinkedIn tagline |
| `short_bio` | TEXT | NULL | ~50 words |
| `long_bio` | TEXT | NULL | ~200 words |
| `photo_url` | VARCHAR(255) | NULL | Path to uploaded photo |
| `city` | VARCHAR(80) | NULL | "Ghotki" |
| `province` | VARCHAR(80) | NULL | "Sindh" |
| `country` | VARCHAR(80) | NULL | "Pakistan" |
| `available_for_hire` | BOOLEAN | DEFAULT 0 | Toggle for hire badge |
| `updated_at` | DATETIME | DEFAULT now, ON UPDATE | |

---

### 5.3 `education`

Can hold multiple degrees (BS, MS). Public display: institution, degree, CGPA.

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `institution` | VARCHAR(200) | NOT NULL | Full university name |
| `short_name` | VARCHAR(80) | NULL | "Aror University, Sukkur" |
| `degree` | VARCHAR(120) | NOT NULL | "BS Artificial Intelligence" |
| `department` | VARCHAR(120) | NULL | "Emerging Sciences and Technology" |
| `start_year` | INTEGER | NOT NULL | 2025 |
| `end_year` | INTEGER | NULL | 2029 (NULL if ongoing) |
| `current_semester` | INTEGER | NULL | 3 |
| `cgpa` | FLOAT | NULL | 3.58 |
| `cgpa_scale` | FLOAT | DEFAULT 4.0 | 4.00 |
| `is_current` | BOOLEAN | DEFAULT 1 | Ongoing vs completed |
| `is_public` | BOOLEAN | DEFAULT 1 | Show on site |
| `display_order` | INTEGER | DEFAULT 0 | |
| `created_at` | DATETIME | DEFAULT now | |

---

### 5.4 `semesters`

Child of `education`. One row per semester.

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `education_id` | INTEGER | FK → education.id, CASCADE | |
| `semester_number` | INTEGER | NOT NULL | 1–8 |
| `year` | INTEGER | NOT NULL | 2025 |
| `gpa` | FLOAT | NULL | 3.59 |
| `is_displayed` | BOOLEAN | DEFAULT 0 | Public vs private |
| `created_at` | DATETIME | DEFAULT now | |

**Indexes:** `(education_id, semester_number)` — UNIQUE

---

### 5.5 `subjects`

Child of `semesters`. **Never displayed publicly** — used for internal tracking and transcript generation.

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `semester_id` | INTEGER | FK → semesters.id, CASCADE | |
| `name` | VARCHAR(150) | NOT NULL | "Data Structures" |
| `code` | VARCHAR(30) | NULL | "CS-201" |
| `marks` | FLOAT | NULL | 85 |
| `total_marks` | FLOAT | DEFAULT 100 | |
| `grade` | VARCHAR(10) | NULL | "A" |
| `is_relevant_course` | BOOLEAN | DEFAULT 0 | Featured on Education page |
| `created_at` | DATETIME | DEFAULT now | |

**Note:** `is_relevant_course = true` → appears in public "Relevant Courses" list.

---

### 5.6 `skills`

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `category` | VARCHAR(50) | NOT NULL | programming / library / database / tool / concept / soft |
| `name` | VARCHAR(80) | NOT NULL | "Python" |
| `level` | VARCHAR(20) | NOT NULL | beginner / intermediate / advanced / expert |
| `is_learning` | BOOLEAN | DEFAULT 0 | Currently Learning flag |
| `icon_class` | VARCHAR(80) | NULL | Optional icon (Devicon/FontAwesome) |
| `display_order` | INTEGER | DEFAULT 0 | |
| `created_at` | DATETIME | DEFAULT now | |

**Indexes:** `(category, display_order)`

**Category values (enum, app-enforced):**
`language`, `library`, `database`, `tool`, `concept`, `soft_skill`

---

### 5.7 `projects`

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `slug` | VARCHAR(120) | UNIQUE, NOT NULL | "car-price-prediction" |
| `title` | VARCHAR(150) | NOT NULL | |
| `one_liner` | VARCHAR(200) | NOT NULL | ~15 words |
| `description` | TEXT | NULL | Markdown allowed |
| `tech_stack` | VARCHAR(300) | NULL | Comma-separated or JSON |
| `role` | VARCHAR(100) | NULL | "Solo" / "Team of 2 — backend" |
| `duration` | VARCHAR(80) | NULL | "Jun 2025 – Aug 2025" |
| `github_url` | VARCHAR(300) | NULL | |
| `live_url` | VARCHAR(300) | NULL | |
| `status` | VARCHAR(30) | DEFAULT 'completed' | completed / ongoing / archived |
| `is_featured` | BOOLEAN | DEFAULT 0 | Show on homepage |
| `is_public` | BOOLEAN | DEFAULT 1 | |
| `display_order` | INTEGER | DEFAULT 0 | |
| `created_at` | DATETIME | DEFAULT now | |
| `updated_at` | DATETIME | DEFAULT now, ON UPDATE | |

**Indexes:** `slug` (unique), `is_featured`, `display_order`

---

### 5.8 `project_images`

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `project_id` | INTEGER | FK → projects.id, CASCADE | |
| `image_url` | VARCHAR(300) | NOT NULL | |
| `alt_text` | VARCHAR(200) | NULL | Accessibility |
| `display_order` | INTEGER | DEFAULT 0 | |
| `created_at` | DATETIME | DEFAULT now | |

**Indexes:** `(project_id, display_order)`

---

### 5.9 `experience`

Internships, freelance, research, TA. Table exists; content added later.

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `company` | VARCHAR(150) | NOT NULL | |
| `role` | VARCHAR(120) | NOT NULL | |
| `type` | VARCHAR(40) | NOT NULL | internship / part_time / freelance / research / volunteer / ta |
| `location` | VARCHAR(120) | NULL | "Sukkur, Pakistan" or "Remote" |
| `start_date` | DATE | NOT NULL | |
| `end_date` | DATE | NULL | NULL if current |
| `description` | TEXT | NULL | Bullet list in markdown |
| `tech_used` | VARCHAR(300) | NULL | |
| `achievement` | VARCHAR(300) | NULL | One measurable win |
| `is_current` | BOOLEAN | DEFAULT 0 | |
| `display_order` | INTEGER | DEFAULT 0 | |
| `created_at` | DATETIME | DEFAULT now | |

---

### 5.10 `certifications`

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `title` | VARCHAR(200) | NOT NULL | |
| `issuer` | VARCHAR(120) | NOT NULL | "CodeWithHarry" |
| `issue_date` | DATE | NOT NULL | |
| `credential_id` | VARCHAR(100) | NULL | |
| `verification_url` | VARCHAR(300) | NULL | |
| `skills_covered` | VARCHAR(300) | NULL | Comma-separated |
| `expiry_date` | DATE | NULL | NULL if no expiry |
| `display_order` | INTEGER | DEFAULT 0 | |
| `created_at` | DATETIME | DEFAULT now | |

---

### 5.11 `courses`

Can be merged with certifications in admin UI, but kept as separate table for future flexibility.

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `title` | VARCHAR(200) | NOT NULL | |
| `platform` | VARCHAR(80) | NOT NULL | coursera / udemy / edx / youtube / university / other |
| `instructor` | VARCHAR(120) | NULL | |
| `duration_hours` | INTEGER | NULL | |
| `completion_date` | DATE | NULL | NULL if in progress |
| `certificate_url` | VARCHAR(300) | NULL | |
| `has_certificate` | BOOLEAN | DEFAULT 0 | |
| `is_project_based` | BOOLEAN | DEFAULT 0 | |
| `is_completed` | BOOLEAN | DEFAULT 1 | |
| `display_order` | INTEGER | DEFAULT 0 | |
| `created_at` | DATETIME | DEFAULT now | |

---

### 5.12 `social_links`

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `platform` | VARCHAR(40) | NOT NULL | linkedin / github / kaggle / email / twitter / medium |
| `url` | VARCHAR(300) | NOT NULL | |
| `label` | VARCHAR(80) | NULL | Display label |
| `icon_class` | VARCHAR(80) | NULL | Optional icon |
| `is_active` | BOOLEAN | DEFAULT 1 | Hide without deleting |
| `display_order` | INTEGER | DEFAULT 0 | |
| `created_at` | DATETIME | DEFAULT now | |

---

### 5.13 `posts`

Blog posts. Public routes deferred until first published post.

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `slug` | VARCHAR(200) | UNIQUE, NOT NULL | |
| `title` | VARCHAR(200) | NOT NULL | |
| `content_md` | TEXT | NOT NULL | Markdown source |
| `excerpt` | VARCHAR(300) | NULL | Auto-generated if null |
| `cover_image` | VARCHAR(300) | NULL | |
| `tags` | VARCHAR(300) | NULL | Comma-separated |
| `status` | VARCHAR(20) | DEFAULT 'draft' | draft / published / archived |
| `published_at` | DATETIME | NULL | NULL if draft |
| `created_at` | DATETIME | DEFAULT now | |
| `updated_at` | DATETIME | DEFAULT now, ON UPDATE | |
| `author_id` | INTEGER | FK → users.id, CASCADE | |

**Indexes:** `slug` (unique), `status`, `published_at`

---

### 5.14 `contact_submissions`

Audit log of contact form submissions.

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `name` | VARCHAR(100) | NOT NULL | |
| `email` | VARCHAR(120) | NOT NULL | |
| `subject` | VARCHAR(200) | NULL | |
| `message` | TEXT | NOT NULL | |
| `submitted_at` | DATETIME | DEFAULT now | |
| `is_read` | BOOLEAN | DEFAULT 0 | |
| `ip_hash` | VARCHAR(64) | NULL | Hashed for spam detection (privacy) |

**Note:** `ip_hash` = SHA-256(ip + salt) — never store raw IPs.

---

### 5.15 `settings`

Key-value store for site-wide settings.

| Column | Type | Constraints | Notes |
|---|---|---|---|
| `id` | INTEGER | PK, AUTO | |
| `key` | VARCHAR(80) | UNIQUE, NOT NULL | "site_title", "meta_description" |
| `value` | TEXT | NULL | |
| `updated_at` | DATETIME | DEFAULT now, ON UPDATE | |

**Default keys:**
- `site_title`
- `meta_description`
- `analytics_id`
- `contact_email`
- `items_per_page`

---

## 6. Relationship Summary

```
users (1) ──< posts (many)
profile (1)
education (1) ──< semesters (many) ──< subjects (many)
projects (1) ──< project_images (many)
skills (standalone)
experience (standalone)
certifications (standalone)
courses (standalone)
social_links (standalone)
contact_submissions (audit)
settings (key-value)
```

---

## 7. Delete Behavior

| Parent Deleted | Children | Behavior |
|---|---|---|
| education | semesters | CASCADE — delete all semesters |
| semesters | subjects | CASCADE |
| projects | project_images | CASCADE |
| users | posts | CASCADE |
| users | contact_submissions | SET NULL (keep audit) |

**Implementation:** In SQLAlchemy, use `cascade="all, delete-orphan"` on relationships, and `ondelete` on FK.

---

## 8. Indexes

| Table | Index | Purpose |
|---|---|---|
| users | `email` (unique) | Login lookup |
| education | `display_order` | Sorted retrieval |
| semesters | `(education_id, semester_number)` unique | Prevent duplicates |
| skills | `(category, display_order)` | Grouped retrieval |
| projects | `slug` unique | URL lookup |
| projects | `is_featured` | Homepage query |
| project_images | `(project_id, display_order)` | Ordered gallery |
| posts | `slug` unique | URL lookup |
| posts | `status` + `published_at` | Public blog query |
| contact_submissions | `is_read` | Unread count |

---

## 9. SQLite vs PostgreSQL Notes

| Feature | SQLite (dev) | PostgreSQL (prod) |
|---|---|---|
| AUTO_INCREMENT | `INTEGER PRIMARY KEY` | `SERIAL` |
| Booleans | `INTEGER` (0/1) | `BOOLEAN` |
| DATETIME | `TEXT` ISO format | `TIMESTAMP` |
| JSON support | Limited | Native `JSONB` |

**SQLAlchemy handles all differences** — you write one model, both DBs work.

---

## 10. Migration Strategy

- **Tool:** Flask-Migrate (wraps Alembic)
- **Workflow:** `flask db init` → `flask db migrate -m "..."` → `flask db upgrade`
- **Rule:** Never edit the DB manually. Always go through migrations.
- **Rollback:** `flask db downgrade` — if a migration breaks, revert it.

---

## 11. Seed Data

A `seed.py` script will populate the DB with:

- 1 user (admin)
- 1 profile (Nadeem's data)
- 1 education (Aror University)
- 2 semesters (Sem 1, 2) + subjects
- 30 skills
- 4 projects + images
- 2 certifications
- 1 course (in-progress Data Analytics)
- 4 social links
- Default settings

**Run once:** `python seed.py`

---

## 12. Change Log

| Date | Change |
|---|---|
| 2026-10-13 | Initial version — Phase 1, Session 3 |