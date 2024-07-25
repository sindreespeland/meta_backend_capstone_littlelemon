# Meta backend capstone littlelemon
This is the littlelemon api created from the meta backend developer capstone project.

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
#### MenuItem
GET and POST menu items:
```bash
http://127.0.0.1:8000/restaurant/menu/items/
```

GET, PUT/PATCH and DELETE menu item:
```bash
http://127.0.0.1:8000/restaurant/menu/items/1/
```


#### Bookings
These endpoints needs authentication.

Run
```bash
http://127.0.0.1:8000/restaurant/api-token-auth/
```
With users credentials, then include the token in the authorization.

Now you can run the following endpoints

GET and POST bookings:
```bash
http://127.0.0.1:8000/restaurant/booking/tables
```

GET, PUT/PATCH and DELETE booking
```bash
http://127.0.0.1:8000/restaurant/booking/tables/1/
```


### Djoser endpoints
User List: http://127.0.0.1:8000/auth/users/ (needs authentication)

User login: http://127.0.0.1:8000/auth/token/login/ (needs user credentials in body)

User logout: http://127.0.0.1:8000/auth/token/logout/ (needs authentication)
