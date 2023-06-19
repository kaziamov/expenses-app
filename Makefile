PORT ?=8000
HOST ?=0.0.0.0
APP ?=expenses_app

full-test:
	poetry run pytest --show-capture=stdout --showlocals -vv
light-test:
	poetry run pytest --no-summary --disable-pytest-warnings
lint:
	poetry run flake8 $(APP) tests
check: light-test lint
push: check
	git push


install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force
test-coverage:
	poetry run pytest --cov=$(APP) --cov-report xml


# DEV
stop:
	docker-compose stop

rm: stop
	docker-compose rm \
	&& sudo rm -rf pgdata/

migrate:
	alembic upgrade head \
	&& alembic revision --autogenerate -m "init" \
	&& alembic upgrade head

dev: stop run-db start


server:
	sudo service postgresql start

run-db: stop
	docker-compose -f docker-compose.db.yml up

#  PROD
start:
	poetry run uvicorn $(APP):app --host $(HOST) --port $(PORT) --reload
	# poetry run python $(APP)/main.py

py:
	poetry run python
