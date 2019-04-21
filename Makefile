test:
	pytest

pep8:
	pycodestyle main.py tests/*

run:
	python main.py -H 300 -W 200 -N 5 -K 0.2 --out fig.png
