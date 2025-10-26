# 🛡️ SecurityLogs – Security Operations Management System

**SecurityLogs** is a full-stack security operations platform built to manage and monitor guard activity, incident reports, and shift performance — all through a modern web dashboard.  
Designed for scalability, modularity, and real-world enterprise architecture, this project demonstrates Daniel Sanchez’s full-stack engineering skills from backend API design to frontend UI and deployment.

---

## 🚀 Overview

SecurityLogs empowers security teams to:
- 📋 Record and track **Daily Activity Reports (DARs)**
- 🚨 Log and analyze **incidents**
- 👮 Manage **guards, shifts, and reports**
- 🧠 Automate alerts with **AI assistance**
- 📧 Send **email notifications** for missed reports or alerts
- 🔐 Provide **role-based access** for managers, supervisors, and guards

---

## 🧰 Tech Stack

### Backend (FastAPI)
- **FastAPI** – RESTful API framework  
- **SQLAlchemy** – ORM for database modeling  
- **Pydantic** – Data validation  
- **Uvicorn** – ASGI server  
- **Logging / Exception Handlers** – Centralized error handling  
- **SMTP or SendGrid** – Email notifications  
- **Pytest** – Testing suite  

### Frontend (React + Tailwind + Vite)
- **React 18** – Component-based UI  
- **TailwindCSS** – Responsive styling  
- **Vite** – Modern build tooling  
- **Axios** – API integration  
- **Recharts** – Analytics and data visualization  

### DevOps / Deployment
- **Docker** (future) – Containerized backend and frontend  
- **PostgreSQL** (future) – Production database  
- **Render / AWS / Vercel** – Hosting and CI/CD ready  

---

## ⚙️ Getting Started

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt
uvicorn app.main:app --reload

cd frontend
npm install
npm run dev


🧭 Development Roadmap

🧩 Phase 0 — Baseline Setup ✅

Project folders, FastAPI + React environments, virtual env, and Tailwind configured.

🧱 Phase 1 — Core Backend API 🔄

Models, routers, schemas for guards, incidents, and DARs.
Validation, error handling, and logging layer.

💻 Phase 2 — Frontend Dashboard

React UI for guard & manager portals.
Role-based dashboards, analytics charts, and data tables.

🔐 Phase 3 — Authentication & Role Access

JWT login, session storage, guard vs. admin permissions, password hashing.

🧠 Phase 4 — AI Assistant & Notifications

Automatic alerts for missing DARs, background tasks for monitoring, and email delivery.

⚙️ Phase 5 — Testing & Optimization

Pytest, performance profiling, and API rate-limiting.

☁️ Phase 6 — Deployment & Scalability

Dockerize, PostgreSQL migration, CI/CD, and cloud deployment.

🎨 Phase 7 — Polish & Portfolio Ready

Screenshots, live demo, documentation, and final README polish.

🧠 Architecture Highlights

Clean, modular design: separation of concerns between core, models, routers, and schemas

Error-handling strategy: global exception handler for consistent API responses

Validation: enforced data contracts via Pydantic models

Security first: JWT tokens, role checking, and future 2FA integration

Logging: automatic activity logs and error tracking

AI integration: monitors guard submissions, notifies supervisors

Email system: background task sends alerts to configured recipients

🧩 Future Enhancements

Real-time dashboard with WebSockets

Push notifications / PWA mode

Mobile companion app (React Native)

AI-generated report summaries

Audit logs & compliance tracking

🧑‍💻 Author

Daniel Sanchez
Full-Stack Developer | Security Engineer | Backend Enthusiast
🔗 GitHub
 | LinkedIn

📜 License

This project is open-source and available under the MIT License
.
