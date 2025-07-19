# MyCorp‑Auth Token Flow

The following describes how a client obtains and refreshes authentication tokens.

1. **Login**  
   Client sends `POST /login` with Basic credentials in the `Authorization` header.  
2. **JWT Issuance**  
   Service validates credentials against LDAP and returns a **JWT** signed with key `auth‑key‑2025`.

### JWT Claims

| Claim | Description |
|-------|-------------|
| `sub` | User ID (UUID) |
| `roles` | CSV list of roles (e.g., `admin,finance`) |
| `iat` | Issued‑at epoch seconds |
| `exp` | Expiry epoch seconds (24 h) |

3. **Authenticated Requests**  
   Client includes `Authorization: Bearer <jwt>` for all subsequent API calls.

4. **Refresh**  
   After 24 h, client calls `POST /refresh` with the Bearer token to obtain a new JWT.  
   Tokens are invalidated server‑side to prevent replay.
