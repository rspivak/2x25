// mcat.go
package main

import (
	"fmt"
	"os"
	"io"
)

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Fprintf(os.Stderr, "mcat: %v\n", err)
		os.Exit(1)
	}

	buffer := make([]byte, 1)  // 1-byte buffer
	for {
		bytesread, err := file.Read(buffer)
		if err == io.EOF {
			break
		}
		fmt.Print(string(buffer[:bytesread]))
	}
	file.Close()
}
