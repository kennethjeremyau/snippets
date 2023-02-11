package main

import (
	"context"
	"errors"
	"fmt"
	"golang.org/x/sync/errgroup"
	"time"
)

func main() {
	ctx := context.Background()
	ewg, ewgCtx := errgroup.WithContext(ctx)

	ewg.Go(func() error {
		fmt.Println("goroutine 1 started")
		<-ewgCtx.Done()
		fmt.Println("goroutine 1 finished")
		return nil
	})

	ewg.Go(func() error {
		fmt.Println("goroutine 2 started")
		innerCtx, cancel := context.WithTimeout(ewgCtx, time.Second*3)
		<-innerCtx.Done()
		cancel()
		fmt.Println("goroutine 2 finished")
		return errors.New("goroutine 2 caused the error")
	})

	err := ewg.Wait()
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println("finished")
}
