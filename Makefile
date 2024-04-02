# RUN TESTS FROM docker-compose.yml
make test:
	docker-compose run --rm --entrypoint "pytest -vv" school-api
