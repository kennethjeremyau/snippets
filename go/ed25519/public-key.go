package main

import (
	"crypto/ed25519"
	"encoding/hex"
	"fmt"
)

func GeneratePublicKey(privateKeyHex string) (string, error) {
	// Decode the private key from hex string
	privateKeyBytes, err := hex.DecodeString(privateKeyHex)
	if err != nil {
		return "", err
	}

	// Generate the public key from the private key
	publicKeyBytes := ed25519.PrivateKey(privateKeyBytes).Public().(ed25519.PublicKey)

	// Encode the public key as a hex string
	publicKeyHex := hex.EncodeToString(publicKeyBytes)

	return publicKeyHex, nil
}

func main() {
	privateKeyHex := "65d704a1a9c41a47686fd3596205e39bd1d5eb8dcc27f40aef30cfc4f0560cfcb4c961b37f42a6d0fcbb067f9552dcdef86e7013eac80a46bd4f941426f4fb40"
	publicKeyHex, err := GeneratePublicKey(privateKeyHex)
	if err != nil {
		fmt.Printf("Error generating public key: %v\n", err)
		return
	}

	fmt.Printf("Public key: %s\n", publicKeyHex)
}
