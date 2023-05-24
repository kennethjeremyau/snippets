package main

import (
	"crypto/ed25519"
	"encoding/hex"
	"fmt"
)

func main() {
	publ, priv, _ := ed25519.GenerateKey(nil)

    fmt.Println("Public Key: ", hex.EncodeToString(publ))
    fmt.Println("Private Key: ", hex.EncodeToString(priv))
}
