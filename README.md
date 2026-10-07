# Booking API

A small booking API built with FastAPI. Users, properties, and bookings are stored in memory while the server is running.

## Requirements

- Python 3.10 or newer

## Setup

Run these commands from the project root.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install fastapi uvicorn
```

If PowerShell blocks activation, use the virtual environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install fastapi uvicorn
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install fastapi uvicorn
```

## Run the API

With the virtual environment activated:

```bash
python -m uvicorn main:app --reload
```

On Windows without activation:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

The API runs at <http://127.0.0.1:8000>. Open <http://127.0.0.1:8000/docs> for interactive API documentation, <http://127.0.0.1:8000/redoc> for ReDoc, or <http://127.0.0.1:8000/openapi.json> for the OpenAPI schema. Press `Ctrl+C` to stop the server.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/users` | List users |
| `GET` | `/users/{user_id}` | Get a user by ID |
| `POST` | `/users` | Create a user |
| `GET` | `/properties` | List properties |
| `GET` | `/properties/{property_id}` | Get a property by ID |
| `POST` | `/properties` | Create a property |
| `GET` | `/bookings` | List bookings, including calculated total prices |
| `POST` | `/bookings` | Create a booking |

The API starts with no users or properties. Create both before creating a booking. Use `apartment` or `hotel_room` as the `property_type`; `price_per_night` and `number_of_nights` must be greater than zero.

### Example: create a booking

With the server running, send these requests in order from PowerShell:

```powershell
$baseUrl = "http://127.0.0.1:8000"

$user = @{
    user_id = 1
    name = "Demo User"
    email = "demo@example.com"
} | ConvertTo-Json
Invoke-RestMethod -Uri "$baseUrl/users" -Method Post -ContentType "application/json" -Body $user

$property = @{
    property_id = 1
    name = "Central Apartment"
    price_per_night = 100.0
    property_type = "apartment"
} | ConvertTo-Json
Invoke-RestMethod -Uri "$baseUrl/properties" -Method Post -ContentType "application/json" -Body $property

$booking = @{
    booking_id = 1
    user_id = 1
    property_id = 1
    number_of_nights = 2
} | ConvertTo-Json
Invoke-RestMethod -Uri "$baseUrl/bookings" -Method Post -ContentType "application/json" -Body $booking
```

The booking response includes `total_price` (`200.0` in this example). Creating a booking marks its property unavailable. There is currently no HTTP endpoint to cancel a booking or make a property available again.

All data is held in memory and is lost when the server restarts.
