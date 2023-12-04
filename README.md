# Shelf Identification Project

## Overview

This Django project is designed to identify the shape of products on a store shelf. It takes a two-dimensional layout of products as input and classifies each product's shape as a horizontal rectangle, vertical rectangle, square, or irregular polygon.

## Prerequisites

Before running the project, make sure you have the following prerequisites installed on your system:

- Python 3.10 or higher
- Django 3.2 or higher
- Docker (for containerization)

## Setup

1. Clone the project repository to your local machine.

2. Create a virtual environment to isolate project dependencies:

   -bash
   python -m venv venv

1. Activate the virtual environment: 
    
    On macOS and Linux :
        source venv/bin/activate

2. Install project dependencies:
        pip install -r requirements.txt

3. Start the development server:
        python3 manage.py runserver

4. The API should now be accessible at http://127.0.0.1:8000/api/identify-shelf-shapes/


## Usage

--> To use the API, make a POST request to http://127.0.0.1:8000/api/identify-shelf-shapes/ with the following JSON data format:

        {
            "layout_data": [
                ["G", "G", "G", "M", "M", "M", "M"],
                ["G", "B", "G", "M", "N", "N", "M"],
                ["G", "G", "G", "M", "N", "N", "M"],
                ["B", "B", "B", "B", "B", "N", "N"]
            ]
        }

    Output/Response : This will return a JSON response containing the identified shapes and their locations on the shelf.


## Implementation 

--> The core logic for identifying shapes is implemented in the identify_shelf_shapes view in views.py.
-->The project uses Django REST framework for handling API requests and responses.
-->Shape identification functions (check_perfect_square, check_horizontal_rect, check_vertical_rect, find_location, etc.) are defined in views.py.
-->The project includes error handling and validation using serializers in serializers.py.

## Testing
--> Run test.py file present in app (shelf_identification)

    python request.py


## Dockerization

Run the docker command given in cmds_torun_docker.txt

    1. --->  docker build -t my-django-app .
    2. ---> docker run -d -p 8000:8000 my-django-app

    The API will be accessible at http://localhost:8000/api/identify-shelf-shapes/ when running inside the Docker container.






