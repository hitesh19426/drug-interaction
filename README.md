## Requirments:
- python
- pip

## How to install:
- Clone this repo
- Go to drug-interaction directory (main folder).
- Use `pip install -r requirements.txt` to install all the required packages
- To run the server `python manage.py runserver`

## How to use:
- Enter the names of drugs (Ex: Fentanyl, Midazolam, Vancomycin) in the ipnut field and add them one by one.
- When you are done, click on `submit the list` button.
- Please wait for the interactions to be fetched from the database.

## Note:
- It might take some time to fetch the interactions from the database since the database is hosted online. So please be patient. We are working on improving the time of query.
- The entered drug names should exactly match with names in database. It basically means that the name should be correct with first letter capital.