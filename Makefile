include .env

full-test:
	poetry run pytest --show-capture=stdout --showlocals -vv
light-test:
	poetry run pytest --no-summary --disable-pytest-warnings
lint:
	poetry run flake8 expenses_app tests
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
	poetry run pytest --cov=expenses_app --cov-report xml


# DEV

dev:
	docker-compose -f docker-compose.dev.yml up

server:
	sudo service postgresql start


#  PROD
start:
	poetry run uvicorn expenses_app:app --host ${HOST} --port ${PORT} --reload

py:
	poetry run python

run-db:
	docker-compose up --force-recreate
