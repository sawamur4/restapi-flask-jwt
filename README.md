# restapi-flask-jwt
Login, Register, get from Fb

## lib requirement
Flask
Flask-JWT
Flask-MongoAlchemy
facebookads 2.8.1

## How to run
Running :

rest_api.py

register username :

post ke url "http://127.0.0.1:5000/daftar" dengan param username="" dan password""

untuk login :

post ke url "http://127.0.0.1:5000/login" dengan param username="" dan password""

untuk yg login ini belum generate token jwt nya

untuk mendapatkan token jwt :

post ke url "http://127.0.0.1:5000/auth" 
dengan header "content-type: application/json" 
dengan body raw {"username"="<username yg di register>", "password": "<password yg di register>"}

muncul response seperti dibawah:
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6Imp1bmlvciIsImlhdCI6MTQ5OTMwMzY2MSwibmJmIjoxNDk5MzAzNjYxLCJleHAiOjE0OTkzMDM5NjF9.SVG8gxLAr0c9yPSP5oURe8G5fCKMr_hyNhExPN5CSo0"
}

gunakan access_token untuk menjalan url "/user"

Get ke url "http://127.0.0.1:5000/user"
dengan headers key=Authorization Value=JWT <Access_token yg didapat>
