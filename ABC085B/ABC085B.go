package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func getNumOfTiered(diameter []int) int {
	set := make(map[int]bool)
	for _, value := range diameter {
		set[value] = true
	}
	return len(set)
}

func main() {
	var n int
	fmt.Scan(&n)

	diameter := make([]int, n)
	scanner := bufio.NewScanner(os.Stdin)

	for i := range diameter {
		scanner.Scan()
		diameter[i], _ = strconv.Atoi(scanner.Text())
	}

	fmt.Println(getNumOfTiered(diameter))
}
