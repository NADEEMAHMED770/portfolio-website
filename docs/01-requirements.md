# Software Requirements Specification
## Portfolio Website — Nadeem Ahmed Ghoto

**Version:** 1.0
**Status:** Draft — Phase 0.4
**Last Updated:** 2026-09-24
**Author:** Nadeem Ahmed Ghoto

---

## 1. Introduction

### 1.1 Purpose
This document specifies the complete requirements for a personal portfolio website that will serve as a long-term professional asset for Nadeem Ahmed Ghoto, an AI/ML student and aspiring engineer.

### 1.2 Scope
The system is a full-stack web application built with Python, Flask, HTML, CSS, and JavaScript. It includes a public-facing portfolio and an admin panel for content management.

### 1.3 Intended Audience
- **Primary:** Recruiters and hiring managers in AI/ML, Data Science, and Software Engineering
- **Secondary:** Professors, collaborators, freelance clients
- **Tertiary:** The site owner (as author and maintainer)

### 1.4 Definitions
- **SRS** — Software Requirements Specification
- **MoSCoW** — Must / Should / Could / Won't prioritization
- **CGPA** — Cumulative Grade Point Average
- **FYP** — Final Year Project

---

## 2. Overall Description

### 2.1 Product Perspective
A public, self-hosted portfolio website with an authenticated admin panel. Content is database-driven so the owner can update it without code changes.

### 2.2 User Classes

| User Class | Description | Access |
|---|---|---|
| **Visitor** | Anyone — recruiters, professors, peers | Read-only public pages |
| **Admin (Owner)** | Nadeem Ahmed Ghoto | Full read/write via admin panel |

### 2.3 Operating Environment
- **Server:** Render (free tier)
- **Dev Environment:** Windows 11, Python 3.14.7, VS Code
- **Browsers:** Chrome, Firefox, Safari, Edge (modern versions)
- **Devices:** Desktop, tablet, mobile (responsive)

### 2.4 Design Constraints
- Must be built with Flask (educational goal)
- Must be deployable to free-tier hosting
- Must be version-controlled with Git/GitHub
- Must follow SDLC process (requirements → design → code → test → deploy)

---

## 3. Content Requirements (from Sections 1–17)

### 3.1 Identity & Branding

| Field | Value |
|---|---|
| Full name | Nadeem Ahmed Ghoto |
| Primary title | AI/ML Student & Aspiring Engineer |
| Tagline | "Aspiring AI/ML Engineer \| Learning Python & Data Analytics \| Building projects from scratch" |
| Location | Ghotki, Sindh, Pakistan |
| Languages | Sindhi (native), Urdu (fluent), English (fluent) |
| Status | Student — BS Artificial Intelligence, 3rd semester |
| Hire badge | Toggle-controlled via admin panel (ON during summer) |
| Profile photo | Deferred to design phase; palette-first approach |

### 3.2 Contact & Social Links

| Channel | Value | Display? |
|---|---|---|
| Email | nadeemahmedghoto06@gmail.com | Yes (contact form) |
| Phone | Not displayed | No |
| LinkedIn | linkedin.com/in/nadeem-ahmed-15033a328 | Yes |
| GitHub | github.com/NADEEMAHMED770 | Yes |
| Kaggle | kaggle.com/nadeemahmedghoto | Yes |
| Others (LeetCode, HackerRank, etc.) | Placeholder — DB field ready | Future |

### 3.3 Education

| Field | Value |
|---|---|
| University | Aror University of Art, Architecture, Design & Heritage, Sukkur |
| Short form | Aror University, Sukkur |
| Degree | BS Artificial Intelligence |
| Department | Emerging Sciences and Technology |
| Duration | July 2025 – May 2029 |
| Current semester | 3rd |
| CGPA | 3.58 / 4.00 |
| Semester breakdown | Sem 1: 3.59, Sem 2: 3.57 |
| FYP | Not started |
| Awards | None yet |
| Intermediate/High School | Not displayed |
| Transcript detail | Stored privately, not publicly displayed |

**Display decisions:**
- Overall CGPA shown publicly
- GPA progression chart deferred to V0.9 (needs 3–4 semesters of data)
- Subject-by-subject data stored in DB, never publicly displayed

### 3.4 Skills

**Programming Languages:** Python (Intermediate), SQL (Intermediate), Java (Intermediate), C++ (Beginner)

**Data Science & ML Libraries:** NumPy, Pandas, Matplotlib, Seaborn, scikit-learn, Flask (all Intermediate / Beginner–Intermediate)

**Databases:** MySQL (Intermediate)

**Tools & Platforms:** VS Code (Advanced), Advanced Excel (Advanced), Git, GitHub, Jupyter, Google Colab, Anaconda, Kaggle, Canva (all Intermediate), MS Office (Advanced)

**Domain Knowledge:** DSA, Machine Learning (foundations), Multivariable Calculus, Linear Algebra

**Soft Skills:** Self-Learning ⭐, Problem Solving, Communication, Time Management

**Currently Learning:** Data Analytics (CodeWithHarry), Power BI, Tableau

### 3.5 Projects (4 Featured)

#### 3.5.1 Car Price Prediction — End-to-End ML + Deployment ⭐
- **One-liner:** Flask web app predicting used-car prices using a trained ML model
- **Stack:** Python, Flask, scikit-learn, Pandas, NumPy, Joblib, HTML/CSS/JS
- **Role:** Solo
- **Result:** R² ≈ 0.77
- **Live:** car-price-prediction-webapp-eohl.onrender.com
- **GitHub:** NADEEMAHMED770/car-price-prediction-webapp + car_price_prediction
- **Features:** Real-time prediction, input validation, responsive UI, error handling
- **Status:** Completed & deployed
- **AI-assistance note:** Not mentioned on site; kept on GitHub README

#### 3.5.2 Local Skill Marketplace
- **One-liner:** Java Swing + MySQL desktop app connecting community members with local skill providers
- **Stack:** Java 17+, Java Swing, MySQL, JDBC
- **Role:** Team of 2 — **backend + database developer** (built auth, smart matching, MySQL schema, CRUD, CSV export)
- **Teammate:** GUI (Java Swing)
- **Status:** Completed (academic BSAI project)

#### 3.5.3 Unemployment Analysis in India
- **One-liner:** EDA on Indian unemployment data — regional, urban/rural, monthly trends
- **Stack:** Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter
- **Role:** Solo
- **GitHub:** Pending standalone repo migration
- **Status:** Completed

#### 3.5.4 Iris Flower Classification
- **One-liner:** Random Forest classifier predicting Iris species from measurements
- **Stack:** Python, scikit-learn, Pandas
- **Result:** 93.33% accuracy (stratified 80/20 split)
- **Role:** Solo
- **GitHub:** Pending standalone repo migration
- **Status:** Completed

### 3.6 Experience
**None yet.** DB table will be built; content added from admin panel as internships are obtained.

### 3.7 Certifications & Courses (merged section)

| # | Title | Issuer | Date | Platform |
|---|---|---|---|---|
| 1 | The Ultimate Job Ready Data Science Course | CodeWithHarry | 07/09/2025 | codewithharry.com |
| 2 | Complete 2025 Python Bootcamp: Learn Python from Scratch | CodeWithHarry | 07/09/2025 | codewithharry.com |

**Note:** International certifications (Google, IBM, Microsoft, Meta, DeepLearning.AI) to be added as earned.

**Deferred:** YouTube courses — DB field `has_certificate` ready.

### 3.8 Achievements, Extracurricular, Testimonials
**None yet.** DB tables built; empty by default.

### 3.9 Blog
**Yes.** Infrastructure built in V0.7; launches empty.

### 3.10 Resume
**Build during Phase 4 (v1.0).** Downloadable PDF.

---

## 4. Functional Requirements

### 4.1 Public Site

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Visitors can view homepage with hero, featured projects, skills | Must |
| FR-02 | Visitors can view About page (bio, education, background) | Must |
| FR-03 | Visitors can view Projects page with all projects | Must |
| FR-04 | Visitors can filter projects by tech stack | Should |
| FR-05 | Visitors can view individual project detail pages | Must |
| FR-06 | Visitors can view Education page (CGPA, university) | Must |
| FR-07 | Visitors can view Certifications & Courses page | Must |
| FR-08 | Visitors can submit contact form with validation | Must |
| FR-09 | Visitors receive acknowledgment email after contact | Should |
| FR-10 | Visitors can toggle dark/light mode (persisted) | Must |
| FR-11 | Visitors can download resume PDF | Must |
| FR-12 | Visitors can access all social links | Must |
| FR-13 | Visitors can read blog posts (V0.7) | Could |
| FR-14 | Site is fully responsive (mobile-first) | Must |
| FR-15 | Custom 404/500 error pages | Should |

### 4.2 Admin Panel

| ID | Requirement | Priority |
|---|---|---|
| AR-01 | Admin can log in with email + password | Must |
| AR-02 | Passwords stored hashed (never plaintext) | Must |
| AR-03 | Admin can toggle hire badge on/off | Must |
| AR-04 | Admin can CRUD projects | Must |
| AR-05 | Admin can CRUD skills | Must |
| AR-06 | Admin can CRUD certifications | Must |
| AR-07 | Admin can CRUD courses | Must |
| AR-08 | Admin can CRUD education/semester data | Must |
| AR-09 | Admin can CRUD experience entries | Must |
| AR-10 | Admin can CRUD blog posts (V0.7) | Could |
| AR-11 | Admin can update profile info (bio, tagline) | Must |
| AR-12 | Admin sessions expire after inactivity | Must |
| AR-13 | Admin has logout | Must |

---

## 5. Non-Functional Requirements

| ID | Requirement | Target |
|---|---|---|
| NFR-01 | Page load time (homepage) | < 2 seconds |
| NFR-02 | Lighthouse performance score | > 90 |
| NFR-03 | Lighthouse accessibility score | > 90 |
| NFR-04 | Responsive breakpoints | 320px, 768px, 1024px, 1440px |
| NFR-05 | Browser support | Last 2 versions of Chrome/Firefox/Safari/Edge |
| NFR-06 | Mobile-friendly | Fully responsive |
| NFR-07 | SEO | Meta tags, Open Graph, sitemap.xml, robots.txt |
| NFR-08 | Security | HTTPS, CSRF protection, password hashing, no secrets in repo |
| NFR-09 | Uptime (post-launch) | Best-effort on Render free tier |
| NFR-10 | Accessibility | WCAG 2.1 AA target |
| NFR-11 | Code quality | Consistent style, documented, testable |
| NFR-12 | Reproducibility | requirements.txt accurate, setup documented |

---

## 6. User Stories (Sample)

- **US-01:** As a recruiter, I want to see Nadeem's best projects within 10 seconds of landing, so I can quickly assess fit.
- **US-02:** As a hiring manager, I want to download his resume in one click.
- **US-03:** As a professor, I want to verify his university and CGPA.
- **US-04:** As a peer, I want to browse his GitHub from the portfolio.
- **US-05:** As the owner, I want to add a new certification from my phone without touching code.
- **US-06:** As the owner, I want to toggle my "available for hire" badge when summer starts.
- **US-07:** As a visitor on mobile, I want the site to load fast and be readable.

---

## 7. MoSCoW Prioritization

### Must Have (v1.0)
- Home, About, Projects, Education, Certifications, Contact pages
- Responsive design
- Dark/light mode
- Contact form with validation
- Admin panel with CRUD for all content
- Authentication with hashed passwords
- Resume PDF download
- Social links
- Custom error pages
- Database-backed content

### Should Have (v1.0 if time permits)
- Project filtering by tech stack
- Email acknowledgment on contact
- Hire badge toggle from admin
- SEO meta tags + Open Graph
- Sitemap + robots.txt

### Could Have (V0.7+)
- Blog
- Live project filtering without reload (V0.8)
- Scroll animations, skeleton loaders (V0.9)
- GPA progression chart (V0.9)
- Testimonials section
- Newsletter signup

### Won't Have (this version)
- Comments/guestbook
- Phone number display
- Multi-language
- Native mobile app
- E-commerce / payment
- Subject-by-subject transcript publicly displayed

---

## 8. Design Decisions (Locked)

| Decision | Choice | Rationale |
|---|---|---|
| Palette | **Palette-first**, photo-second | System drives assets |
| Theme default | System-detected + toggle | User preference respected |
| Font | Inter (UI), JetBrains Mono (code) | Industry standard |
| Style | Minimal + modern | Matches AI/DS positioning |
| Logo | "NA" monogram | Designed at Phase 1 |
| Favicon | Monogram derivative | At Phase 1 |
| Architecture | Flask app factory + blueprints | Scalable, industry pattern |
| Database | SQLite (dev) → PostgreSQL (prod) | Free, easy migration |

---

## 9. Domain, Hosting & SEO

| Field | Value |
|---|---|
| Domain | TBD at deployment (nadeemahmed.dev or nadeemahmedghoto.com) |
| Hosting | Render (free tier) |
| Budget | Free tier only |
| Site title | Nadeem Ahmed Ghoto — AI/ML Student & Aspiring Engineer |
| Meta description | Drafted at Phase 1 |
| Keywords | AI Engineer, Machine Learning, Data Science, Python Developer, Flask Developer, scikit-learn, Pandas, NumPy, Data Analyst, AI Student, ML Portfolio, End-to-End Machine Learning, Flask ML deployment |
| Content language | English only |

---

## 10. UML & Diagram Plan (Phase 1)

Tools: **Mermaid** (in markdown) + **draw.io** (wireframes)

| Diagram | Purpose |
|---|---|
| Use Case | Actors + actions |
| Class | DB models + relationships |
| ER | Full schema |
| Sequence | Login, contact form, project fetch |
| Activity | Admin adds a project |
| Deployment | Render + Gunicorn + DB |

---

## 11. Success Criteria

- **v1.0 live** within 5–7 weeks of Phase 0 start
- Recruiters can assess Nadeem within 30 seconds of landing
- Owner can update all content without code changes
- Site passes Lighthouse performance + accessibility > 90
- Repository is clean, documented, and presents well on GitHub

---

## 12. Version Roadmap

| Version | Scope |
|---|---|
| 0.0.1 | Project scaffold ✅ |
| 0.1.0 | Flask app factory + blueprint skeleton |
| 0.2.0 | Static pages (Home, About, Projects, Contact) |
| 0.3.0 | Design system + dark mode |
| 0.4.0 | Database models + migrations |
| 0.5.0 | Contact form + validation + email |
| 0.6.0 | Admin panel + auth |
| 0.7.0 | Blog |
| 0.8.0 | API + modern JS |
| 0.9.0 | UX polish |
| 1.0.0 | Production release |

---

## 13. Open Questions / Deferred Decisions

- Profile photo: to be selected after palette is defined
- Domain name: purchase at Phase 4
- Analytics: Plausible vs none — decide at Phase 4
- International certifications: pending acquisition

---

**End of SRS — v1.0**