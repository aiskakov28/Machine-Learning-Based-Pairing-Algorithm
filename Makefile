ENV_FILE := .env.example

up:
	docker compose --env-file $(ENV_FILE) up -d redpanda elasticsearch cassandra api

consumers:
	docker compose --env-file $(ENV_FILE) up -d consumer_es consumer_cassandra

seed:
	docker compose --env-file $(ENV_FILE) run --rm producer_csv

logs:
	docker compose logs -f api

down:
	docker compose down -v

test-unit:
	python -m pytest -q tests/unit

test-int:
	python -m pytest -q tests/integration
