all: run
build: clean
	npm install
	zip -q -r build.zip *
clean:
	rm -rf build.zip
run:
	npm test
upload: build
	aws lambda update-function-code --function-name sample_mocha_lambda --zip-file fileb://build.zip
