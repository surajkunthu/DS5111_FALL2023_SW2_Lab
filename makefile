default:
	@cat makefile

env:
	python3 -m venv env
	. env/bin/activate; pip install -r requirements.txt

run:	
	@. env/bin/activate; python3 bin/clockdemo_param.py

lint:
	@. env/bin/activate; pylint bin/perceptron.py

.PHONY: tests
tests:
	. env/bin/activate; pytest -vv tests
