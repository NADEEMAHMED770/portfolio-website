# Wireframes

**Document:** 08-wireframes.md
**Version:** 1.0
**Status:** Locked — Phase 1, Session 4
**Last Updated:** 2026-10-13
**Format:** ASCII wireframes (renders in monospace)

---

## 1. Purpose

Low-fidelity layout mockups for every non-trivial page. Define structure and information hierarchy **before** visual design (Session 5) and code (V0.1+).

**Conventions used in these wireframes:**

| Symbol | Meaning |
|---|---|
| `[NA]` | Site logo / monogram |
| `[Button]` | Clickable button |
| `[Chip]` | Skill tag / small label |
| `[IMG]` | Image placeholder |
| `[📷]` | Icon |
| `─`, `│`, `┌` etc. | Container boundaries |

---

## 2. Home — Desktop

Primary impression. Hero must communicate **who, what, credibility** in under 10 seconds.

```
┌────────────────────────────────────────────────────────────────────────────┐
│ [NA]   Home  About  Projects  Education  Certs  Contact        [☀/🌙]     │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│    ┌──────────────────┐       ┌──────────────────────────────────────┐    │
│    │                  │       │                                      │    │
│    │                  │       │  Nadeem Ahmed Ghoto                  │    │
│    │                  │       │                                      │    │
│    │      [PHOTO]     │       │  AI/ML Student & Aspiring Engineer   │    │
│    │                  │       │                                      │    │
│    │                  │       │  Aspiring AI/ML Engineer | Learning  │    │
│    │                  │       │  Python & Data Analytics | Building  │    │
│    │                  │       │  projects from scratch               │    │
│    │                  │       │                                      │    │
│    └──────────────────┘       │  [ View Projects ]  [ Resume ]       │    │
│                               │                                      │    │
│                               └──────────────────────────────────────┘    │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Featured Projects                                                         │
│                                                                            │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐          │
│  │   [IMG]    │  │   [IMG]    │  │   [IMG]    │  │   [IMG]    │          │
│  │            │  │            │  │            │  │            │          │
│  │ Title      │  │ Title      │  │ Title      │  │ Title      │          │
│  │ One-liner  │  │ One-liner  │  │ One-liner  │  │ One-liner  │          │
│  │ [chip][chip]│ │ [chip][chip]│ │ [chip][chip]│ │ [chip][chip]│          │
│  │ [Live][Code]│ │ [Live][Code]│ │ [Live][Code]│ │ [Live][Code]│          │
│  └────────────┘  └────────────┘  └────────────┘  └────────────┘          │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Skills                                                                    │
│  [Python] [SQL] [Pandas] [NumPy] [Flask] [scikit-learn]                   │
│  [Git] [Jupyter] [Matplotlib] [Seaborn]                                    │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Education                                                                 │
│  ┌──────────────────────────────────────────────────────────────────┐    │
│  │  Aror University of Art, Architecture, Design & Heritage, Sukkur │    │
│  │  BS Artificial Intelligence · CGPA: 3.58 / 4.00                  │    │
│  └──────────────────────────────────────────────────────────────────┘    │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│                    Ready to work together?                                 │
│                    [ Get in Touch ]                                        │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│  Navigate          Connect             Legal                               │
│  ─────────         ───────             ─────                               │
│  Home              LinkedIn            MIT License                         │
│  About             GitHub              © 2026 Nadeem Ahmed Ghoto           │
│  Projects          Kaggle                                                  │
│  Education         Email                                                   │
│  Certifications                                                            │
│  Contact                                                                   │
└────────────────────────────────────────────────────────────────────────────┘
```

**Layout notes:**
- Hero: 2 columns (photo left, text right) — 40/60 split
- Featured projects: 4-column grid (desktop)
- Skills: wrapping chip flow
- Hire badge appears inside hero text area when enabled
- Footer: 3-column layout

---

## 3. Home — Mobile

Same content, transformed for narrow viewport (≤ 640px).

```
┌──────────────────────────────────┐
│ [NA]                       [☰]   │
├──────────────────────────────────┤
│                                  │
│          ┌────────────┐          │
│          │            │          │
│          │   [PHOTO]  │          │
│          │            │          │
│          └────────────┘          │
│                                  │
│      Nadeem Ahmed Ghoto          │
│                                  │
│   AI/ML Student & Aspiring       │
│            Engineer              │
│                                  │
│   Aspiring AI/ML Engineer |      │
│   Learning Python & Data         │
│   Analytics | Building           │
│   projects from scratch          │
│                                  │
│       [ View Projects ]          │
│       [ Resume ]                 │
│                                  │
├──────────────────────────────────┤
│  Featured Projects               │
│                                  │
│  ┌────────────────────────────┐  │
│  │         [IMG]              │  │
│  │  Title                     │  │
│  │  One-liner                 │  │
│  │  [chip] [chip]             │  │
│  │  [Live] [Code]             │  │
│  └────────────────────────────┘  │
│                                  │
│  ┌────────────────────────────┐  │
│  │         [IMG]              │  │
│  │  ...                       │  │
│  └────────────────────────────┘  │
│                                  │
├──────────────────────────────────┤
│  Skills                          │
│  [Python] [SQL] [Pandas]         │
│  [NumPy] [Flask] [Git]           │
├──────────────────────────────────┤
│  Education                       │
│  ┌────────────────────────────┐  │
│  │ Aror University, Sukkur    │  │
│  │ BS AI · CGPA 3.58/4.00     │  │
│  └────────────────────────────┘  │
├──────────────────────────────────┤
│  [ Get in Touch ]                │
├──────────────────────────────────┤
│  Footer (stacked links)          │
└──────────────────────────────────┘
```

**Key transformations:**
- Navbar → hamburger menu
- Hero: side-by-side → **stacked**
- Featured projects: 4-column → **single-column scroll**
- Footer: 3-column → **stacked**
- Padding reduced (16px vs 32px on desktop)

---

## 4. Projects List

Full project catalog with client-side filtering.

```
┌────────────────────────────────────────────────────────────────────────────┐
│ [NA]   Home  About  Projects  Education  Certs  Contact        [☀/🌙]     │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Projects                                                                  │
│  Things I've built — end to end.                                           │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│  Filter:  [All]  [Python]  [Flask]  [ML]  [Java]  [EDA]                    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌──────────────────────────┐   ┌──────────────────────────┐              │
│  │         [IMG]            │   │         [IMG]            │              │
│  │                          │   │                          │              │
│  │ Car Price Prediction     │   │ Local Skill Marketplace  │              │
│  │ Flask ML deployment      │   │ Java Swing + MySQL       │              │
│  │                          │   │                          │              │
│  │ [Python][Flask][ML]      │   │ [Java][MySQL][OOP]       │              │
│  │                          │   │                          │              │
│  │ [Live] [Code]            │   │ [Code]                   │              │
│  └──────────────────────────┘   └──────────────────────────┘              │
│                                                                            │
│  ┌──────────────────────────┐   ┌──────────────────────────┐              │
│  │         [IMG]            │   │         [IMG]            │              │
│  │ Unemployment Analysis    │   │ Iris Classification      │              │
│  │ EDA on Indian data       │   │ Random Forest 93.33%     │              │
│  │ [Python][Pandas][EDA]    │   │ [Python][sklearn][ML]    │              │
│  │ [Code]                   │   │ [Code]                   │              │
│  └──────────────────────────┘   └──────────────────────────┘              │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│  Footer                                                                    │
└────────────────────────────────────────────────────────────────────────────┘
```

**Interaction:** Clicking a filter chip filters cards **client-side** (JS). No page reload.

---

## 5. Project Detail

Deep dive on a single project.

```
┌────────────────────────────────────────────────────────────────────────────┐
│ [NA]   Home  About  Projects  Education  Certs  Contact        [☀/🌙]     │
├────────────────────────────────────────────────────────────────────────────┤
│  ← Back to Projects                                                        │
│                                                                            │
│  🚗 Car Price Prediction — End-to-End ML + Deployment                      │
│                                                                            │
│  Flask web app that predicts used-car selling prices using a trained       │
│  Multiple Linear Regression model.                                         │
│                                                                            │
│  [ 🔴 Live Demo ]   [ 📦 GitHub Repo ]                                     │
│                                                                            │
│  Role: Solo  ·  Status: Completed  ·  Test R²: 0.77                        │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                                                                     │  │
│  │                    [HERO SCREENSHOT]                                │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  [thumb] [thumb] [thumb] [thumb]                                           │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  About This Project                                                        │
│  ─────────────────                                                         │
│  [3-5 paragraph description in markdown]                                   │
│                                                                            │
│  Tech Stack                                                                │
│  [Python] [Flask] [scikit-learn] [Pandas] [NumPy] [Joblib]                 │
│                                                                            │
│  Key Features                                                              │
│   • Real-time predictions                                                  │
│   • Input validation                                                       │
│   • Responsive UI                                                          │
│   • Graceful error handling                                                │
│                                                                            │
│  Challenges & Solutions                                                    │
│  [text]                                                                    │
│                                                                            │
│  Results                                                                    │
│  Test R²: 0.77  ·  MAE: 1.41  ·  RMSE: 2.44                                │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│  Other Projects                                                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                                  │
│  │ [IMG]    │  │ [IMG]    │  │ [IMG]    │                                  │
│  │ Title    │  │ Title    │  │ Title    │                                  │
│  └──────────┘  └──────────┘  └──────────┘                                  │
├────────────────────────────────────────────────────────────────────────────┤
│  Footer                                                                    │
└────────────────────────────────────────────────────────────────────────────┘
```

**Notes:**
- Hero screenshot is large and prominent
- Thumbnails below the hero = gallery
- Clicking a thumbnail swaps the hero image

---

## 6. Admin Dashboard

Content statistics + quick actions + sidebar navigation.

```
┌─────────────┬──────────────────────────────────────────────────────────────┐
│             │                                                              │
│  [NA]       │  Dashboard                                                   │
│             │                                                              │
│  📊 Dashboard│                                                             │
│             │  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐            │
│  Profile    │  │   4    │  │   30   │  │   2    │  │   0    │            │
│   └ Edit    │  │Projects│  │ Skills │  │ Certif.│  │ Posts  │            │
│   └ Social  │  └────────┘  └────────┘  └────────┘  └────────┘            │
│   └ Settings│                                                              │
│             │  ┌────────┐  ┌────────┐  ┌────────┐                        │
│  Content    │  │   0    │  │   2    │  │   0    │                        │
│   └ Education│ │Expert. │  │Courses │  │ Contac.│                        │
│   └ Semesters│ └────────┘  └────────┘  └────────┘                        │
│   └ Subjects│                                                              │
│   └ Skills  │  Recent Activity                                             │
│   └ Learning│  ─────────────────                                           │
│   └ Projects│  • Project "Car Price Prediction" updated — 2 hours ago      │
│   └ Experien.│ • Skill "Power BI" added — yesterday                        │
│             │  • Login — today                                             │
│  Credentials│                                                              │
│   └ Certif. │  Quick Actions                                               │
│   └ Courses │  [ Add Project ]  [ Add Skill ]  [ View Live Site ]         │
│             │                                                              │
│  Blog       │                                                              │
│   └ Posts   │                                                              │
│             │                                                              │
│  [ Logout ] │                                                              │
│             │                                                              │
└─────────────┴──────────────────────────────────────────────────────────────┘
```

**Notes:**
- Sidebar: fixed 220px, dark
- Stats: 2 rows × 4 columns
- "Recent Activity" = last 5 edits
- Quick Actions: most-used admin functions

---

## 7. Education

Prominent CGPA display + relevant courses.

```
┌────────────────────────────────────────────────────────────────────────────┐
│ [NA]   Home  About  Projects  Education  Certs  Contact        [☀/🌙]     │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Education                                                                 │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐     │
│  │                                                                  │     │
│  │  🎓  Aror University of Art, Architecture, Design & Heritage     │     │
│  │                                                                  │     │
│  │  BS Artificial Intelligence                                      │     │
│  │  Department of Emerging Sciences and Technology                  │     │
│  │                                                                  │     │
│  │  July 2025 – May 2029  ·  Currently in 3rd semester              │     │
│  │                                                                  │     │
│  │  ┌─────────────────┐   ┌─────────────────┐                       │     │
│  │  │                 │   │                 │                       │     │
│  │  │      3.58       │   │      3.59       │                       │     │
│  │  │                 │   │                 │                       │     │
│  │  │    CGPA         │   │  Year 1 GPA     │                       │     │
│  │  │   / 4.00        │   │                 │                       │     │
│  │  └─────────────────┘   └─────────────────┘                       │     │
│  │                                                                  │     │
│  └──────────────────────────────────────────────────────────────────┘     │
│                                                                            │
│  Relevant Courses                                                          │
│  [Data Structures] [Algorithms] [Machine Learning]                         │
│  [Databases] [Linear Algebra] [Calculus] [Statistics]                      │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│  Footer                                                                    │
└────────────────────────────────────────────────────────────────────────────┘
```

**Notes:**
- CGPA in **large stat card** — visually dominant
- Semester-wise GPA appears only when `is_displayed = true`
- Relevant courses = subjects where `is_relevant_course = true`

---

## 8. Login

Focused single-purpose page. No navbar, no footer.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│                                                              │
│                                                              │
│                                                              │
│              ┌────────────────────────────┐                  │
│              │                            │                  │
│              │         [ NA ]             │                  │
│              │                            │                  │
│              │      Admin Login           │                  │
│              │                            │                  │
│              │   Email                    │                  │
│              │   ┌──────────────────────┐ │                  │
│              │   │                      │ │                  │
│              │   └──────────────────────┘ │                  │
│              │                            │                  │
│              │   Password                 │                  │
│              │   ┌──────────────────────┐ │                  │
│              │   │                      │ │                  │
│              │   └──────────────────────┘ │                  │
│              │                            │                  │
│              │   [     Log In     ]       │                  │
│              │                            │                  │
│              │   Forgot password?         │                  │
│              │                            │                  │
│              └────────────────────────────┘                  │
│                                                              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Notes:**
- Centered card on empty background
- No navigation — prevents "escaping" from auth
- CSRF token hidden field
- Error messages appear above the form

---

## 9. Admin CRUD Form (Generic Pattern)

**One wireframe covers all admin edit/create forms** (project, skill, cert, course, experience, education, etc.).

```
┌─────────────┬──────────────────────────────────────────────────────────────┐
│             │                                                              │
│  [NA]       │  ← Back to Projects                                          │
│             │                                                              │
│  📊 Dashboard│  Add New Project                                            │
│             │                                                              │
│  Content    │  ┌──────────────────────────────────────────────────────┐   │
│   └ Projects│  │                                                      │   │
│             │  │  Title *                                             │   │
│             │  │  ┌────────────────────────────────────────────────┐ │   │
│             │  │  │                                                │ │   │
│             │  │  └────────────────────────────────────────────────┘ │   │
│             │  │                                                      │   │
│             │  │  Slug *                                              │   │
│             │  │  ┌────────────────────────────────────────────────┐ │   │
│             │  │  │                                                │ │   │
│             │  │  └────────────────────────────────────────────────┘ │   │
│             │  │                                                      │   │
│             │  │  One-liner *                                         │   │
│             │  │  ┌────────────────────────────────────────────────┐ │   │
│             │  │  │                                                │ │   │
│             │  │  └────────────────────────────────────────────────┘ │   │
│             │  │                                                      │   │
│             │  │  Description (Markdown)                              │   │
│             │  │  ┌────────────────────────────────────────────────┐ │   │
│             │  │  │                                                │ │   │
│             │  │  │                                                │ │   │
│             │  │  │                                                │ │   │
│             │  │  └────────────────────────────────────────────────┘ │   │
│             │  │                                                      │   │
│             │  │  Tech Stack                                          │   │
│             │  │  ┌────────────────────────────────────────────────┐ │   │
│             │  │  │                                                │ │   │
│             │  │  └────────────────────────────────────────────────┘ │   │
│             │  │                                                      │   │
│             │  │  GitHub URL                Live URL                  │   │
│             │  │  ┌──────────────────────┐  ┌──────────────────────┐ │   │
│             │  │  │                      │  │                      │ │   │
│             │  │  └──────────────────────┘  └──────────────────────┘ │   │
│             │  │                                                      │   │
│             │  │  Role               Status                           │   │
│             │  │  ┌────────────────┐ ┌────────────────┐               │   │
│             │  │  │                │ │                │               │   │
│             │  │  └────────────────┘ └────────────────┘               │   │
│             │  │                                                      │   │
│             │  │  [✓] Featured on homepage   [✓] Public               │   │
│             │  │                                                      │   │
│             │  │  [ Cancel ]              [ Save Project ]            │   │
│             │  │                                                      │   │
│             │  └──────────────────────────────────────────────────────┘   │
│             │                                                              │
└─────────────┴──────────────────────────────────────────────────────────────┘
```

**Pattern reused for:**
- Projects, Skills, Certifications, Courses, Experience, Education, Social Links, Blog Posts

**Conventions:**
- Required fields marked with `*`
- Labels above inputs
- Wide textareas for markdown content
- Two-column layout for short related fields
- Primary action on right, secondary on left
- Flash messages appear above the form

---

## 10. Wireframes Not Included (and Why)

| Page | Reason |
|---|---|
| About | Simple text + optional photo — no complex layout |
| Certifications | Card grid — same pattern as Projects |
| Contact | Standard form — same pattern as Login/Admin Form |
| Resume | Preview + download button — obvious |
| 404 / 500 | Centered message — trivial |

**If a page uses a pattern already shown, no dedicated wireframe is needed.**

---

## 11. Change Log

| Date | Change |
|---|---|
| 2026-10-13 | Initial version — Phase 1, Session 4 |