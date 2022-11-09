# Makefile

.DEFAULT_GOAL := run

clean:
	rm pb/*.pb.go

fmt:
	go fmt ./...

pb:
	protoc --proto_path=pb --go_out=pb --go_opt=paths=source_relative --go-grpc_out=pb --go-grpc_opt=paths=source_relative **/*.proto

run: pb
	go run main/main.go

.PHONY: \
	clean \
	fmt \
	pb \
	run
