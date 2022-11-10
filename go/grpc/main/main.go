package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"

	"google.golang.org/grpc"
	"scratch/grpc/pb"
)

var (
	port = flag.Int("port", 8080, "Server port")
)

type server struct {
	pb.UnimplementedApiServer
}

func (s *server) Get(ctx context.Context, req *pb.Request) (*pb.Response, error) {
	log.Printf("Received %v", req.GetText())
	return &pb.Response{Text: req.GetText()}, nil
}

func main() {
	log.Print("Starting server")

	flag.Parse()

	conn, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterApiServer(s, &server{})

	if err := s.Serve(conn); err != nil {
		log.Fatalf("Failed to serve: %s", err)
	}
}
