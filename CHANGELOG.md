# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- Phase 1 — Requirements, UML diagrams, wireframes, design system
- Phase 2 — Core build: V0.1 → V0.6 (including admin panel)
- Phase 3 — Advanced features: V0.7 → V0.9 (blog, API, UX polish)
- Phase 4 — Testing, deployment, resume → v1.0

---

## [0.0.2] — 2026-09-30

### Added
- GitHub profile polish: bio, README, pinned repos, topics, descriptions
- Migrated CodeAlpha Task 1 → standalone repo `unemployment-analysis-india`
- Migrated CodeAlpha Task 3 → standalone repo `iris-flower-classification`
- Added `.gitignore` files to all polished project repos
- GitHub profile README with tech stack badges and featured projects

### Changed
- Rewrote READMEs for 4 flagship project repos
  (`car-price-prediction-webapp`, `car_price_prediction`, `Local-Skill-Marketplace`, `unemployment-analysis-india`)
- Corrected R² metric in `docs/01-requirements.md`:
  now reports **Training R²: 0.90 | Test R²: 0.77** (previously reported only 0.90 as test score)
- Pinned 6 curated repos on GitHub profile

### Removed
- Deleted unused repos: `Git-and-GitHub-Learning`, `code-with-harry-courses`
- Archived legacy repos: `my-learning-journey`, `java-learning`, `CodeAlpha-DataScience-Internship`
- Untracked compiled `.class` files from `Local-Skill-Marketplace`

### Notes
- Phase 0.5 (GitHub Polish Week) completed
- All active repos now have: description, topics, README, `.gitignore`

---

## [0.0.1] — 2026-09-24

### Added
- Initial project structure
- `README.md` with project overview and roadmap
- `requirements.txt` with Flask 3.1.3 and dependencies
- `.gitignore` for Python, Flask, virtual environment, IDE, OS files
- `LICENSE` (MIT)
- `docs/` folder for project documentation:
  - `01-requirements.md` (full SRS)
  - `02-design.md` (placeholder)
  - `03-testing.md` (placeholder)
  - `04-deployment.md` (placeholder)

### Notes
- Phase 0 (Foundation & Setup) initiated
- Environment: Python 3.14.7, Git 2.55.0, Flask 3.1.3