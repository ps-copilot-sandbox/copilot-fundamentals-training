# MyCorp‑Auth Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `401 Unauthorized` on every request | Clock skew between client and server | Ensure client time is synced via NTP |
| `signature is invalid` when decoding JWT | Wrong signing key | Verify you're using `auth‑key‑2025` public key |
| Login succeeds but roles are empty | LDAP group not mapped | Add user to correct LDAP group or update role mapping |
| Token expires earlier than 24 h | `exp` claim altered | Clients must not modify JWT payload |
| `400 Bad Request` when using refresh token | Refresh token expired or revoked | Request new refresh token through full authentication flow |
