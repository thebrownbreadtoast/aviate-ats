# Assignment for Aviate

How to run this project?
- Can be run as a dockerized application and a simple local Django server.
	- Using docker
		- `docker-compose -f docker/compose/base.yml -f docker/compose/dev.yml up -d`
			- gunicorn will start listening on port :4444
	- Using default Django server
		- Activate virtualenv
		- Install dependencies
			- pipenv install
		- `python manage.py runserver 0.0.0.0:4444`
			- Django server will start listening on port :4444

Endpoints:
- /api/v1/candidates/<uuid>/ GET
- /api/v1/candidates/search/?q= GET
- /api/v1/candidates/ POST
- /api/v1/candidates/<uuid>/ DELETE
