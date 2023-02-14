package main

import (
    "fmt"
)

func f1() error {
    err := f2()
    if err != nil {
        return fmt.Errorf("wrapped: %w", err)
    }
    return nil
}

func f2() error {
    return fmt.Errorf("test")
}

func main() {
    err := f1()
    fmt.Printf("%+v", err)
}
