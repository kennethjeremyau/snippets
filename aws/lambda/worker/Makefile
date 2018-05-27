build: clean
	virtualenv env
	mkdir build
	./env/bin/pip install -r requirements.txt -t build
	cp lambda.py build
	chmod -R a+r build
	cd build; zip -q -r ../build.zip *

clean:
	rm -rf env build build.zip output.log

invoke:
	aws lambda invoke --function-name worker output.log

ssh: export AWS_DEFAULT_REGION=us-east-1
ssh:
	ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ./worker.pem ec2-user@`aws ec2 describe-instances --filters Name=tag-key,Values="Name",Name=tag-value,Values="worker" | jq -r '.[][][][]? | select(.State.Name == "running") | .PublicIpAddress'`

upload: build
	aws lambda update-function-code --function-name worker --zip-file fileb://build.zip

.DEFAULT_GOAL := upload
.PHONY: build, clean, invoke, ssh, upload
