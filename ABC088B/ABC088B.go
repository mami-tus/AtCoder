package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func getScoreDiff(scores []int) int {
	var scoreDiff int
	sort.Sort(sort.Reverse(sort.IntSlice(scores)))
	for i, score := range scores {
		if i%2 == 0 {
			scoreDiff += score
		} else {
			scoreDiff -= score
		}
	}
	return scoreDiff
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	sc.Scan()
	aStr := strings.Split(sc.Text(), " ")
	a := make([]int, n)
	for i, aStr := range aStr {
		a[i], _ = strconv.Atoi(aStr)
	}
	fmt.Println(getScoreDiff(a))
}
