package main

import (
    "fmt"
)

func main() {
    m := map[string]string {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
    }
    i := 0
    keys := make([]string, len(m))
    for key := range m {
        keys[i] = key
        i++
    }
    fmt.Println(keys[0])
    fmt.Println(keys[1])
    fmt.Println(keys[2])
}
