package main

import (
    "flag"
    "fmt"
    "log"
    "net/http"
)

var (
    port = flag.Int("port", 8080, "Server port")
)

func hello(w http.ResponseWriter, req *http.Request) {
    log.Print("Received request")
    fmt.Fprintf(w, "hello\n")
}

func main() {
    log.Print("Starting server")
    flag.Parse()
    http.HandleFunc("/hello", hello)
    http.ListenAndServe(fmt.Sprintf(":%d", *port), nil)
}
