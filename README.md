# did_django_google_api_tutorial
Django project that uses Googles APIs to auto populate fields, display maps and routes for multiple waypoints

1) cd to development directory
2) mkvirtualenv did_django_google_api_tutorial
3) mkdir did_django_google_api_tutorial
4) clone repository to new directory
5) pip install -r requirements.txt
6) Create and update settings.ini with your email API information

GOOGLE_API_KEY = "AIzaSyDIcmJ-M505THCYxPhNM4UDTZHjt395cxI"

RECAPTCHA_PUBLIC_KEY = "6LddMt0hAAAAAEYCmc2eJHq86ioM3D6qBot5BukR"

RECAPTCHA_PRIVATE_KEY = "6LddMt0hAAAAAFvKyPhVHmOPL0_lsd7mTptl9veE"

7) python manage.py makemigrations
8) python manage.py migrate
9) python manage.py runserver
10) https://localhost:8000 - Bob's your uncle!! 

Note: 

Don't forget to activate the following Google API's

reCAPTURE
Places API
Maps Javascript API
Directions API
Distance Matrix API
Geocoding API


