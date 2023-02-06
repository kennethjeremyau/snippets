package main

import (
	"context"
	"log"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	log.Println("Starting server")

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	quitSignal := make(chan os.Signal, 1)
	signal.Notify(
		quitSignal,
		syscall.SIGHUP,
		syscall.SIGINT,
		syscall.SIGTERM,
		syscall.SIGQUIT,
	)
	go func() {
		defer cancel()
		<-quitSignal
		log.Println("Quit signal received")
	}()

	server, err := NewServer(8080)
	if err != nil {
		log.Println("Cannot create server")
	}

	err = server.Start(ctx)
	if err != nil {
		log.Fatalf("Server terminated: %v\n", err)
	} else {
		log.Println("Server terminated")
	}
}
