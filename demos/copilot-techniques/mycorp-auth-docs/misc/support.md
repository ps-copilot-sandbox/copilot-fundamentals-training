# Support for Getting a Refresh Token - 10 Step Process

## Overview
This guide walks you through obtaining a refresh token for the MyCorp-Auth system, which allows you to maintain authenticated sessions without requiring users to re-enter credentials.

## Prerequisites
- Valid MyCorp-Auth credentials
- Access to the authentication endpoint
- Client application registered in the system
- `auth-key-2025` public key configured

## Step-by-Step Process

### Step 1: Prepare Initial Authentication Request
```http
POST /auth/login
Content-Type: application/json

{
  "username": "your-username",
  "password": "your-password",
  "client_id": "your-client-id",
  "scope": "openid profile refresh_token"
}
```

### Step 2: Include Refresh Token Scope
Ensure your authentication request includes `refresh_token` in the scope parameter. This signals the server that you want a refresh token in addition to the access token.

### Step 3: Verify Client Time Synchronization
Check that your client system time is synchronized with NTP to avoid `401 Unauthorized` errors due to clock skew.

### Step 4: Submit Authentication Request
Send the POST request to the authentication endpoint and wait for the response.

### Step 5: Parse the Authentication Response
Extract the following from the successful response:
- `access_token`: Short-lived token for API requests
- `refresh_token`: Long-lived token for getting new access tokens
- `expires_in`: Access token expiration time (typically 24 hours)
- `token_type`: Usually "Bearer"

### Step 6: Securely Store the Refresh Token
Store the refresh token in a secure location:
- Use encrypted storage
- Never log refresh tokens
- Implement proper access controls
- Consider token rotation policies

### Step 7: Validate Token Signature
Verify the JWT signature using the `auth-key-2025` public key to ensure token authenticity.

### Step 8: Check LDAP Group Mappings
If roles appear empty, verify that your user account is properly mapped to the correct LDAP groups for role assignment.

### Step 9: Test Token Usage
Make a test API call using the access token to confirm successful authentication:
```http
GET /api/user/profile
Authorization: Bearer <access_token>
```

### Step 10: Implement Refresh Logic
Set up automatic token refresh before expiration:
```http
POST /auth/refresh
Content-Type: application/json

{
  "refresh_token": "your-refresh-token",
  "client_id": "your-client-id"
}
```

## Important Notes
- Refresh tokens typically have longer expiration times than access tokens
- Always validate the JWT payload and never modify the `exp` claim
- Monitor for common issues listed in the troubleshooting guide
- Implement proper error handling for refresh token failures

## Security Best Practices
- Rotate refresh tokens regularly
- Implement refresh token revocation
- Use HTTPS for all token exchanges
- Monitor for suspicious refresh patterns
- Log refresh token usage for audit purposes
