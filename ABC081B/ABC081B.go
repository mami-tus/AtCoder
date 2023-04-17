package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	inputs := strings.Split(sc.Text(), " ")
	intValTuple := make([]int, n)
	for i, input := range inputs {
		intVal, _ := strconv.Atoi(input)
		intValTuple[i] = intVal
	}
	fmt.Println(getTimesDividableIn2(intValTuple))
}

func getTimesDividableIn2(intValTuple []int) int {
	zeroNum := make([]int, len(intValTuple))
	for i, intVal := range intValTuple {
		binVal := strconv.FormatInt(int64(intVal), 2)
		zeroNum[i] = len(binVal) - strings.LastIndexByte(binVal, '1') - 1
	}
	return min(zeroNum)
}

func min(nums []int) int {
	minVal := nums[0]
	for _, val := range nums[1:] {
		if val < minVal {
			minVal = val
		}
	}
	return minVal
}
