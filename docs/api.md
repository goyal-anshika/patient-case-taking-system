# Patient Case-Taking System API

Base URL:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

---

# Authentication

## Register

POST `/api/auth/register`

Creates a new system user.

### Request

```json
{
  "full_name": "Demo Doctor",
  "email": "doctor@example.com",
  "password": "Doctor@123",
  "role": "doctor"
}