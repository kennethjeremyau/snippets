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
	    go func(id int) {
            defer wg.Done()
            for {
                fmt.Printf("looping %v\n", id)
                //raceMap[id] = fmt.Sprintf("value %v", id)
                raceMap.Store(i, fmt.Sprintf("value %v", id))
                select {
                case <-ctx.Done():
                    fmt.Printf("quitting %v\n", id)
                    return
                default:
                }
            }
	    }(i)
    }

    wg.Wait()
}
