package main

import (
	"fmt"
	"strconv"
)

func getSumTotal(n, minSumDigits, maxSumDigits int) int {
	sumTotal := 0
	for i := 1; i <= n; i++ {
		sumDigits := getSumDigits(i)
		if minSumDigits <= sumDigits && sumDigits <= maxSumDigits {
			sumTotal += i
		}
	}
	return sumTotal
}

func getSumDigits(n int) int {
	sumDigits := 0
	for _, r := range strconv.Itoa(n) {
		digit, _ := strconv.Atoi(string(r))
		sumDigits += digit
	}
	return sumDigits
}

func main() {
	var n, a, b int
	fmt.Scan(&n, &a, &b)
	fmt.Println(getSumTotal(n, a, b))
}
