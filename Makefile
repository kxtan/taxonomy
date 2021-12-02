install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C modules taxonomy

test:
	@cd tests; pytest -vv --cov-report term-missing --cov=modules test_*.py

format:
	black modules/*.py taxonomy.py tests/*.py