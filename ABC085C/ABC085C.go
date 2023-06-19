package main

import (
	"fmt"
	"strconv"
	"strings"
)

func getBillCombination(numOfBills int, sumTotal int) []int {
	const (
		TenThousand  = 10000
		FiveThousand = 5000
		Thousand     = 1000
	)

	yen10000Num, yen5000Num, yen1000Num := -1, -1, -1
	for i := 0; i <= numOfBills; i++ {
		for j := 0; j <= numOfBills-i; j++ {
			if TenThousand*i+FiveThousand*j+Thousand*(numOfBills-i-j) == sumTotal {
				yen10000Num, yen5000Num, yen1000Num = i, j, numOfBills-i-j
			}
		}
	}
	return []int{yen10000Num, yen5000Num, yen1000Num}
}

func main() {
	var n, y int
	fmt.Scan(&n, &y)
	bills := getBillCombination(n, y)
	strBills := make([]string, len(bills))
	for i, bill := range bills {
		strBills[i] = strconv.Itoa(bill)
	}
	fmt.Printf(strings.Join(strBills, " "))
}
