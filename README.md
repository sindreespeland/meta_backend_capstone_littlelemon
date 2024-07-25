# meta_backend_capstone_littlelemon
In this project I have used a venv. Use the following commands below to create and activate a viritual environment followed by installing the requirements file

## Step 1 - create venv
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

## Step 2 - install requirements
Installing requirements
```bash
pip install -r requirements.txt
```

After setting your mysql credentials you should be able to migrate, createsuperuser and runserver.

## Endpoints
### Booking endpoints
Bookings: http://127.0.0.1:8000/restaurant/booking/tables

### Djoser endpoints
User List: http://127.0.0.1:8000/auth/users/

User login: http://127.0.0.1:8000/auth/token/login/

User logout: http://127.0.0.1:8000/auth/token/logout/