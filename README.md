## Installation

Create a virtualenv
```
virtualenv -p python3 venv
```

Install Requirements
```
pip install -r requirements.txt
```


Migrate database
```
./manage.py migrate
```


Create superuser:
```
./manage.py createsuperuser
```


Run app:
```
./manage.py runserver
```

Run celery tasks:
Open 2 separate terminals and run each of these commands separately on each of the terminals
```
celery worker -A celery_demo --loglevel=info
celery -A celery_demo beat -l INFO
```

Admin URL:
This is where we store all the scraped data. Login with the credentials created on `./manage.py createsuperuser`
```
localhost:8000/admin
```

If you want to test out the celery scraping task on shorter periodic intervals, you can tinker on the periodic_task decorator that I commented out on "sales/tasks.py"
