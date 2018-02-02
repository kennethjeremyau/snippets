all: update
build: clean
	mkdir build
	cp *.py build
	cp -R ./devenv/lib/python2.7/site-packages/* build
	cd build; zip -r9 ../build.zip *
clean:
	rm -rf build build.zip
create: build
	aws lambda create-function --function-name FUNCTION_NAME --runtime python2.7 --role ROLE_ARN --handler handler.handler --region us-east-1 --timeout 300 --zip-file fileb://build.zip
devenv:
	virtualenv devenv
update: build
	aws lambda update-function-code --function-name FUNCTION_NAME --zip-file fileb://build.zip
