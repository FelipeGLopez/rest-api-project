migrations:
	docker-compose run --rm web python manage.py makemigrations
	docker-compose run --rm web python manage.py migrate

preload_data:
	docker-compose run --rm web python manage.py populate_db_with_fixtures

run_tests:
	docker-compose run --rm web pytest

standup_db:
	cp .env.example .env
	docker-compose down --volumes
	docker volume rm -f rest-api-project_postgres_data
	docker-compose build db
	docker-compose up db -d

migrate_and_preload:
	make migrations preload_data
	
standup_app:
	cp .env.example .env
	docker-compose down web
	docker-compose build web
	docker-compose up web -d

setup_project:
	make standup_db standup_app migrate_and_preload

make open_swagger:
	open http://localhost:8000/swagger/
