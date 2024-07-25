# meta_backend_capstone_littlelemon

### Commands
Create venv - windows and mac:
```bash
python -m venv venv
```

Activate venv - windows:
```bash
venv\Scripts\activate
```

Activate venv - mac:
```bash
source venv/bin/activate
```

Creating requirements file
```bash
pip freeze > requirements.txt
```

Installing requirements
```bash
pip install -r requirements.txt
```
## Endpoints
### Booking endpoints
Bookings: http://127.0.0.1:8000/restaurant/booking/tables

### Djoser endpoints
User List: http://127.0.0.1:8000/auth/users/

User login: http://127.0.0.1:8000/auth/token/login/

User logout: http://127.0.0.1:8000/auth/token/logout/