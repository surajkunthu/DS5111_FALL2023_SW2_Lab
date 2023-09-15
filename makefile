default:
	@cat makefile

env:
	python3 -m venv env
	pip install -r requirements.txt

run:

tests:
	pytest -vv tests
