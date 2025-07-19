# MyCorp‑Auth Service Overview

**MyCorp‑Auth** is a lightweight authentication microservice that issues JSON Web Tokens (JWTs) for all first‑party apps in the MyCorp ecosystem.

| Feature | Details |
|---------|---------|
| Auth Methods | Basic (username/password), OAuth2 Client‑Creds |
| Token Type | JWT (HS256), 24 h TTL |
| Refresh Flow | `/refresh` endpoint rotates tokens |
| Version | v2.5.1 (2025‑06‑15) |

## Key Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| `POST` | `/login` | Validate credentials & issue JWT |
| `POST` | `/refresh` | Rotate expired token |
| `GET` | `/me` | Return user profile based on bearer token |
