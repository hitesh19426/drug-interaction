## Requirments:
- python3 (Please don't use python version < 3)
- pip

## How to install (Windows):
- Clone this repo using `git clone https://github.com/hitesh19426/drug-interaction`
- Go to drug-interaction directory (main folder).
- Use `pip install -r requirements.txt` to install all the required packages
- To run the server `python manage.py runserver`
- Go to the link of the development server mentioned in the terminal. By default, it should be `localhost:8000`

## How to install (Ubuntu):
- Clone this repo using `git clone https://github.com/hitesh19426/drug-interaction`
- Go to drug-interaction directory (main folder).
- Use command `pip install django` to install django
- Use command `sudo apt-get install python3-psycopg2` to install psycopg2
- To run the server `python manage.py runserver`
- Go to the link of the development server mentioned in the terminal. By default, it should be `localhost:8000`

## How to use:
- Enter the names of drugs (Ex: Fentanyl, Midazolam, Vancomycin) in the ipnut field and add them one by one.
- When you are done, click on `submit the list` button.
- Please wait for the interactions to be fetched from the database.

## Note:
- It might take some time to fetch the interactions from the database since the database is hosted online. So please be patient. We are working on improving the time of query.
- The entered drug names should exactly match with names in database. It basically means that the name should be correct with first letter capital.

## Example to view all interactions:
- Aluminum hydroxide
- Dolutegravir
- Aprepitant
- Abacavir
- Orlistat
- Calcium acetate
- Dexamethasone
