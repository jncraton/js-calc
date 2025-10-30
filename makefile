all:

dev-deps:
	pip3 install pytest-playwright==0.7.1 && playwright install

format:
	npx prettier --write *.html

test:
	pytest

clean:
	rm -rf __pycache__ .pytest_cache
