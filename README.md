# DRF Docs - Demo
The demo for DRF Docs.

### Prerequisites

 - Postgres Database: `drfdocs`
 - Python 3 (`brew install python3`)
 - Django
 - Django Rest Framework


### Setup (Development)
Create the database (only needs to be done once):

    psql
    CREATE DATABASE drfdocs;
    # List the databases
    \l
    # Quit
    \q

There is a build script, that will do all the work for you. Then migrate.

    ./scripts/build
    ./scripts/migrate


### Development commands
There are several helper methods to run the project locally:

    # Build the project
    ./scripts/build

    # Run migrate
    ./scripts/migrate

    # Run the server
    ./scripts/runserver

    # Bring the Django shell
    ./scripts/shell

    # Run other commands using the environment - ./scripts/run echo "Hello Oleous!"
    ./scripts/run


### Generating demo data
It will only work if `DEBUG` is set to `True` and there are no users in the database.

    ./scripts/run python manage.py create_demo_data


### Tests
To run the tests:

    ./scripts/runtests

To generate the coverage in html:

    ./scripts/run coverage html
