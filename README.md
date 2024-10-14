# Product Management API

## Description
This is a product management API developed with Django and Django REST Framework. The application allows you to register, list, and calculate the promotional price of products based on their categories.

## Features
- Register new products with fields: name, description, color, category, and price.
- Automatic calculation of the promotional price based on the product category.
- Listing of registered products.

## Technologies Used
- Python 3.11
- Django 5.x
- Django REST Framework
- SQLite

## How to Set Up and Run the Application

Clone this repository to your local machine:
```
https://github.com/JulioRios00/apollo_backend.git
```


In the root directory of the project, create a virtual environment:
python -m venv venv source venv/bin/activate # For Mac/Linux

## Install the necessary dependencies:
```
pip install -r requirements.txt
```



### Configure the Database

Run the migrations to set up the database:
```
python manage.py migrate
```


## Run the Development Server
```
python manage.py runserver
```


The application will be available at http://127.0.0.1:8000/

## Available Routes

- GET /products/ – List all products.
- POST /products/ – Create a new product
    
Example POST Request for Product Registration:
URL: http://127.0.0.1:8000/products/
