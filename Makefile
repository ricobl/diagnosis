clean:
	find . -iname "*.pyc" -delete
test: clean
	./manage.py test url_access_check
