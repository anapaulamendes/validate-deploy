pyflakes:
	find -L . -name "*.py" | grep -v __init__ | xargs pyflakes

isort:
	isort .

black:
	black .

linters:
	isort .
	black .
	flake8 .

migrate:
	python manage.py makemigrations
	python manage.py migrate

test:
	python manage.py test

runserver:
	python manage.py runserver 0.0.0.0:8000

coverage:
	coverage run --source='.' manage.py test

html_coverage: coverage
	coverage html

report_coverage: coverage
	coverage report
