# UML Diagrams

**Document:** 06-uml-diagrams.md
**Version:** 1.0
**Status:** Locked — Phase 1, Session 2
**Last Updated:** 2026-10-13
**Tool:** Mermaid (text-based, renders on GitHub)

---

## 1. Purpose

This document contains the UML diagrams that define the structure and behavior of the portfolio website. All diagrams are written in **Mermaid** — a text-based diagramming syntax that renders natively on GitHub and is version-controlled alongside the code.

---

## 2. Actors

| Actor | Description | Access Level |
|---|---|---|
| **Visitor** | Any unauthenticated user — recruiters, professors, peers | Read-only public pages |
| **Admin** | Site owner (Nadeem Ahmed Ghoto) — authenticated | Full CRUD via admin panel |
| **System** | Automated processes — email sending, error handling | Internal only |

---

## 3. Use Case Diagram

```mermaid
graph LR
    V((Visitor))
    A((Admin))

    subgraph Public["Public Site"]
        UC1[View Home]
        UC2[Browse Projects]
        UC3[View Project Detail]
        UC4[View Education]
        UC5[View Certifications]
        UC6[View Resume]
        UC7[Download Resume PDF]
        UC8[Toggle Dark Mode]
        UC9[Submit Contact Form]
        UC10[Open Social Links]
        UC11[View Blog<br/>deferred]
    end

    subgraph AdminPanel["Admin Panel"]
        AC1[Login / Logout]
        AC2[Edit Profile]
        AC3[Toggle Hire Badge]
        AC4[Manage Education]
        AC5[Manage Skills]
        AC6[Manage Learning Items]
        AC7[Manage Projects]
        AC8[Manage Project Images]
        AC9[Manage Experience]
        AC10[Manage Certifications]
        AC11[Manage Courses]
        AC12[Manage Social Links]
        AC13[Manage Blog Posts<br/>content-only]
        AC14[View Contact Submissions]
        AC15[Edit Site Settings]
        AC16[Change Password]
    end

    V --> UC1
    V --> UC2
    V --> UC3
    V --> UC4
    V --> UC5
    V --> UC6
    V --> UC7
    V --> UC8
    V --> UC9
    V --> UC10
    V --> UC11

    A --> AC1
    A --> AC2
    A --> AC3
    A --> AC4
    A --> AC5
    A --> AC6
    A --> AC7
    A --> AC8
    A --> AC9
    A --> AC10
    A --> AC11
    A --> AC12
    A --> AC13
    A --> AC14
    A --> AC15
    A --> AC16

    UC9 -.->|sends email| SYS[[Email Service]]
    AC1 -.->|verifies credentials| DB[(Database)]
    UC2 -.->|queries| DB
```

**Notes:**
- `UC11` (Blog) is documented but **route not enabled in v1.0** — activated when first post is published.
- Contact form and login both touch the database.
- Email is a system-level actor — not shown as a human.

---

## 4. Entity Class Diagram

The following classes map to database tables. Relationships shown are 1-to-many unless noted.

```mermaid
classDiagram
    class User {
        +int id
        +string email
        +string password_hash
        +datetime created_at
        +datetime last_login
        +login()
        +logout()
        +check_password()
    }

    class Profile {
        +int id
        +string full_name
        +string title
        +string tagline
        +text short_bio
        +text long_bio
        +string photo_url
        +string city
        +string province
        +string country
        +bool available_for_hire
        +datetime updated_at
    }

    class Education {
        +int id
        +string institution
        +string short_name
        +string degree
        +string department
        +int start_year
        +int end_year
        +int current_semester
        +float cgpa
        +float cgpa_scale
        +bool is_current
        +int display_order
    }

    class Semester {
        +int id
        +int education_id
        +int semester_number
        +int year
        +float gpa
        +bool is_displayed
    }

    class Subject {
        +int id
        +int semester_id
        +string name
        +float marks
        +string grade
        +bool is_relevant_course
    }

    class Skill {
        +int id
        +string category
        +string name
        +string level
        +bool is_learning
        +int display_order
    }

    class Project {
        +int id
        +string slug
        +string title
        +string one_liner
        +text description
        +string tech_stack
        +string role
        +string duration
        +string github_url
        +string live_url
        +string status
        +bool is_featured
        +int display_order
        +datetime created_at
        +datetime updated_at
    }

    class ProjectImage {
        +int id
        +int project_id
        +string image_url
        +string alt_text
        +int display_order
    }

    class Experience {
        +int id
        +string company
        +string role
        +string type
        +string location
        +date start_date
        +date end_date
        +text description
        +string tech_used
        +string achievement
        +int display_order
    }

    class Certification {
        +int id
        +string title
        +string issuer
        +date issue_date
        +string credential_id
        +string verification_url
        +string skills_covered
        +date expiry_date
        +int display_order
    }

    class Course {
        +int id
        +string title
        +string platform
        +string instructor
        +int duration_hours
        +date completion_date
        +string certificate_url
        +bool has_certificate
        +bool is_project_based
        +int display_order
    }

    class SocialLink {
        +int id
        +string platform
        +string url
        +string icon_class
        +int display_order
        +bool is_active
    }

    class Post {
        +int id
        +string slug
        +string title
        +text content_md
        +string excerpt
        +string cover_image
        +string tags
        +string status
        +datetime published_at
        +datetime created_at
        +datetime updated_at
    }

    class ContactSubmission {
        +int id
        +string name
        +string email
        +string subject
        +text message
        +datetime submitted_at
        +bool is_read
        +string ip_hash
    }

    class Setting {
        +int id
        +string key
        +text value
        +datetime updated_at
    }

    User "1" --> "1" Profile : manages
    Education "1" --> "*" Semester : contains
    Semester "1" --> "*" Subject : contains
    Project "1" --> "*" ProjectImage : has
    Project ..> Skill : uses
    User "1" --> "*" Post : authors
    User "1" --> "*" ContactSubmission : reads
```

**Notes:**
- `User` is the admin table — only one row in practice.
- `Profile` is a single-row table (id = 1 always).
- `Subject` records are stored but **not publicly displayed** — used only for internal tracking.
- `Post` exists in DB but public routes are deferred until first post is written.

---

## 5. Entity Relationship Overview

High-level view of how the 15 tables connect:

```mermaid
erDiagram
    USER ||--|| PROFILE : manages
    EDUCATION ||--o{ SEMESTER : "has many"
    SEMESTER ||--o{ SUBJECT : "has many"
    PROJECT ||--o{ PROJECT_IMAGE : "has many"
    USER ||--o{ POST : authors

    USER {
        int id PK
        string email
        string password_hash
    }
    PROFILE {
        int id PK
        string full_name
        string title
        bool available_for_hire
    }
    EDUCATION {
        int id PK
        string institution
        float cgpa
    }
    SEMESTER {
        int id PK
        int education_id FK
        int semester_number
        float gpa
    }
    SUBJECT {
        int id PK
        int semester_id FK
        string name
        float marks
    }
    PROJECT {
        int id PK
        string slug
        string title
        bool is_featured
    }
    PROJECT_IMAGE {
        int id PK
        int project_id FK
        string image_url
    }
    POST {
        int id PK
        string slug
        string title
        string status
    }
```

**Full column-level ERD to follow in `07-database-schema.md`.**

---

## 6. Table Inventory

| # | Table | Rows Expected | Public-Facing? |
|---|---|---|---|
| 1 | `users` | 1 | No |
| 2 | `profile` | 1 | Yes (read) |
| 3 | `education` | 1–3 | Yes |
| 4 | `semesters` | 8 | Partial (CGPA visible, GPA optional) |
| 5 | `subjects` | ~40 | No (private) |
| 6 | `skills` | 30+ | Yes |
| 7 | `projects` | 4–10 | Yes |
| 8 | `project_images` | 3–10 | Yes |
| 9 | `experience` | 0+ | Yes (when populated) |
| 10 | `certifications` | 2+ | Yes |
| 11 | `courses` | 2+ | Yes |
| 12 | `social_links` | 4–6 | Yes |
| 13 | `posts` | 0+ | Deferred |
| 14 | `contact_submissions` | 0+ | No (admin only) |
| 15 | `settings` | 5–10 | No |

**Total: 15 tables.**

---

## 7. Relationship Rules

| Parent | Child | Cardinality | On Delete |
|---|---|---|---|
| User → Profile | 1-to-1 | CASCADE |
| Education → Semester | 1-to-many | CASCADE |
| Semester → Subject | 1-to-many | CASCADE |
| Project → ProjectImage | 1-to-many | CASCADE |
| User → Post | 1-to-many | CASCADE |
| User → ContactSubmission | 1-to-many | SET NULL |

**CASCADE:** Deleting the parent removes all children.
**SET NULL:** Deleting the user doesn't delete submissions (audit trail).

---

## 8. Change Log

| Date | Change |
|---|---|
| 2026-10-13 | Initial version — Phase 1, Session 2 |