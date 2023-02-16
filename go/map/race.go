package main

import (
    "context"
    "fmt"
    "sync"
    "time"
)

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 3 * time.Second)
	defer cancel()

    var wg sync.WaitGroup

    // raceMap := map[int]string{}
    raceMap := sync.Map{}

    for i := 1; i <= 5; i++ {
        wg.Add(1)
	    go func(ctx context.Context) {
            defer wg.Done()
            for {
                fmt.Printf("looping %v\n", i)
                //raceMap[i] = fmt.Sprintf("value %v", i)
                raceMap.Store(i, fmt.Sprintf("value %v", i))
                select {
                case <-ctx.Done():
                    fmt.Printf("quitting %v\n", i)
                    return
                default:
                }
            }
	    }(ctx)
    }

    wg.Wait()
}
