# Django HTTPS Security Configuration

## What was implemented:
- Enforced HTTPS using SECURE_SSL_REDIRECT
- Implemented HSTS with 1-year expiry, subdomains included, preload enabled
- Set SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE to True
- Added security headers:
    - X_FRAME_OPTIONS = DENY
    - SECURE_CONTENT_TYPE_NOSNIFF = True
    - SECURE_BROWSER_XSS_FILTER = True
- Configured Nginx to redirect HTTP → HTTPS and serve SSL

## Why these changes:
- HTTPS ensures encrypted data transmission
- HSTS prevents downgrade attacks
- Secure cookies prevent session hijacking over HTTP
- Security headers protect against clickjacking, XSS, and MIME sniffing

## Deployment Notes:
- SSL certificates managed via Let's Encrypt
- Nginx configuration updated for SSL
