package main

import (
	"encoding/base64"
	"fmt"
)

// Base64 encoding/decoding of a byte array string using Go's quoted format.
func main() {
    data := "\x1es\x94\x12\r\x94\xcc\x00\u007f\x9f\vH\xd4"
    encoded := base64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(encoded)

    decoded, _ := base64.StdEncoding.DecodeString(encoded)
    fmt.Printf("%q\n", decoded)
}
