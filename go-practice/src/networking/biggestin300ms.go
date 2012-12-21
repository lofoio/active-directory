package main

import (
  "fmt"
  "math/rand"
  "time"
)

func main() {
  timeout := time.After(300 * time.Millisecond)
  numbers := make(chan int) // This channel will be used
  var numberCount int = 0
  var maxNumber int = 0

  // Start putting random numbers on the numbers channel
  go func() {
    for {
      numbers <- rand.Int()
    }
  }()

  for {
    select {
    case <- timeout:
      fmt.Printf("%v numbers generated. Max number found: %v.\n", numberCount, maxNumber)
      return

    case number := <- numbers:
      numberCount++
      if number > maxNumber {
        maxNumber = number
      }
    }
  }
}