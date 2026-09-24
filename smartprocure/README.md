
# SmartProcure Microservice

SmartProcure is a lightweight, high-performance procurement microservice built with **FastAPI**, **SQLAlchemy**, and **SQLite**. It features an automated multi-criteria optimization engine to evaluate suppliers based on cost, lead time, and defect rates, paired with a modern dark-mode frontend dashboard powered by **Tailwind CSS**.

---

## Tech Stack

- **Backend:** Python 3, FastAPI, Uvicorn
- **Database:** SQLite, SQLAlchemy ORM
- **Validation & Schemas:** Pydantic
- **Frontend:** Single-page dashboard (HTML5, Tailwind CSS, JavaScript)
- **Testing:** Pytest

---

## Project Structure


smartprocure/
├── app/
│   ├── init.py
│   ├── database.py       # DB connection and session configuration
│   ├── main.py           # FastAPI entry point & API endpoints
│   ├── models.py         # SQLAlchemy DB models
│   ├── optimizer.py      # Multi-criteria supplier scoring engine
│   ├── schemas.py        # Pydantic request/response schemas
│   └── static/
│       └── index.html    # Tailwind CSS web UI dashboard
├── tests/
│   └── test_optimizer.py # Unit tests for scoring logic
├── .gitignore
├── README.md
└── requirement.txt

---

## Quick Start Guide

### 1. Install Dependencies
```bash
pip install -r requirement.txt

2. Run the Server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

3. Access the Dashboard & API Docs
 * Web Dashboard: http://localhost:8000
 * Interactive Swagger Docs: http://localhost:8000/docs
  Running Tests
pytest


---

### How to update it in Termux:

Run these 3 commands in Termux to save and push the `README.md` update to GitHub:

```bash
git add README.md
git commit -m "docs: add complete project README"
git push

