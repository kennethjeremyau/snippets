package main

import (
    "context"
    "fmt"
    "time"
)

func closeChannel(ctx context.Context, ch chan interface{}) {
    <-ctx.Done()
    fmt.Println("closing channel")
    close(ch)
}

func main() {
    fmt.Println("start")

    ch := make(chan interface{})

    ctx, cancel := context.WithTimeout(context.Background(), 1 * time.Second)
    defer cancel()
    go closeChannel(ctx, ch)

    <-ch

    fmt.Println("end")
}
