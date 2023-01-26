# Http Monitor

## Description

Http Monitor is a simple tool to monitor http requests. It can be used to monitor the health of a website or to monitor
the performance of a web application. It can also be used to monitor the health of a web server.

## Installation

Create a virtual environment and install the requirements:

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

## Dependencies

* Python 2.7
* Django 1.8
* Django Rest Framework 3.2.3

## Usage

    $ python manage.py runserver

to run background service for checking the status of the urls:

    $ python manage.py run_background_task

## API Endpoints
The following endpoints are available for use:

`/auth/login/` - Allows users to login to the application.

`/auth/register/` - Allows users to register for a new account on the application.

`/url/create/` - Allows users to create a new URL.

`/url/user/` - Returns a list of URLs created by the authenticated user.

`/url/delete/<int:pk>/` - Allows users to delete a specific URL.

`/url/alerts/` - Returns a list of alerts for the authenticated user.

`/url/stats/<int:url_id>/` - Returns statistics for a specific URL.

All endpoints require authentication, except /auth/login/ and /auth/register/.