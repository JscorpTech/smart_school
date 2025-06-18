up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

deploy:
	docker compose down
	docker compose up -d

logs:
	docker compose logs -f

makemigration:
	docker compose exec web python manage.py makemigrations --noinput

migrate:
	docker compose exec web python manage.py migrate

makemigrate: makemigration migrate

.PHONY: up