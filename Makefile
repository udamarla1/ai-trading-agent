install:
	pip install -r requirements.txt

run:
	python -m src.main

test:
	pytest -q
