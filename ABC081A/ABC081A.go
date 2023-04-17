package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	input := sc.Text()
	fmt.Println(getNumberOfMarbles(input))
}

func getNumberOfMarbles(input string) int {
	count := 0
	for _, r := range input {
		if r == '1' {
			count++
		}
	}
	return count
}
