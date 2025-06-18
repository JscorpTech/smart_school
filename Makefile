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

.PHONY: up