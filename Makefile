src = $(wildcard *.c)
obj = $(src:.c=.o)


binary:
	pyinstaller -F  --onefile  --name riuk main.py

clean:
	rm -rf dist/ build/ __pycache__ *.spec
