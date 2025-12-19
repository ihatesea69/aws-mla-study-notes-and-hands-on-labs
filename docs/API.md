# API Documentation

## Authentication

All API requests require a Bearer token in the header:

```
Authorization: Bearer <token>
```

## Endpoints

### Users

#### GET /users

Get a list of users.

**Response:**

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
]
```

#### POST /users

Create a new user.

**Request:**

```json
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

### Health Check

#### GET /health

Check if the service is running.

**Response:**

```json
{
  "status": "ok"
}
```
