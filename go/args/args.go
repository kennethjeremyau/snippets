package main

import (
    "flag"
    "fmt"
)

func main() {
    str := flag.String("str", "default", "description")
    flag.Parse()
    fmt.Println(*str)
}
