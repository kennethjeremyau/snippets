package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"scratch/grpc/pb"
)

var (
	port = flag.Int("port", 8080, "Server port")
)

func main() {
	log.Printf("Running client")

	flag.Parse()

	conn, err := grpc.Dial(
		fmt.Sprintf("localhost:%d", *port),
		grpc.WithTransportCredentials(insecure.NewCredentials()),
	)
	if err != nil {
		log.Fatalf("Could not connect: %v", err)
	}
	defer conn.Close()

	client := pb.NewApiClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	res, err := client.Get(ctx, &pb.Request{Text: "hello"})
	if err != nil {
		log.Fatalf("Could not get: %v", err)
	}
	log.Printf("Client received %v", res.GetText())
}
