package main

import (
	"context"
	"fmt"
	"log"
	"net"
)

type Server struct {
	addr string
}

func NewServer(port int) (*Server, error) {
	log.Println("New server created")
	return &Server{
		// Avoid using "localhost" because it relies on DNS.
		addr: fmt.Sprintf(":%v", port),
	}, nil
}

func (s *Server) Start(ctx context.Context) error {
	log.Println("Server started")

	listener, err := net.Listen("tcp", s.addr)
	if err != nil {
		return err
	}
	defer listener.Close()

	// Use goroutine since listening blocks, and we also want to detect quit signal.
	go listenForConnections(listener)

	<-ctx.Done()
	return nil
}

func listenForConnections(listener net.Listener) {
	for {
		conn, err := listener.Accept()
		if err != nil {
			// Ok to ignore this error.
			// If server terminates, this code will spam.
			continue
		}
		log.Println("Client connected")
		handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	defer func() {
		log.Println("Connection closed")
		conn.Close()
	}()

	buffer := make([]byte, 1024)
	_, err := conn.Read(buffer)
	if err != nil {
		log.Fatalf("Cannot read from connection: %v", err)
		return
	}

	_, err = conn.Write([]byte("bye"))
	if err != nil {
		log.Fatalf("Cannot write to connection: %v", err)
		return
	}
}
