test:
	pytest

pep8:
	pycodestyle anothertt

run:
	pip install .
	python -m anothertt -H 300 -W 200 -N 5 -K 0.2 --out fig.png

