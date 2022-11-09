package main

import (
    "context"
	"log"
	"net"

	"google.golang.org/grpc"
	"scratch/grpc/pb"
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

	conn, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterApiServer(s, &server{})

	if err := s.Serve(conn); err != nil {
		log.Fatalf("Failed to serve: %s", err)
	}
}
