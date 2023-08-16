package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func judgePossibleOrImpossible(timePointList [][]int) string {
	prevTime, prevPointX, prevPointY := 0, 0, 0
	for _, list := range timePointList {
		time, pointX, pointY := list[0], list[1], list[2]
		movePossibleTime := int(math.Abs(float64(prevTime - time)))                                        // 移動可能時間
		minArrivalTime := int(math.Abs(float64(prevPointX-pointX)) + math.Abs(float64(prevPointY-pointY))) // 最短到着時間
		if (time+pointX+pointY)%2 != 0 || movePossibleTime < minArrivalTime {
			return "No"
		}
		// 今回の入力値を記録
		prevTime, prevPointX, prevPointY = time, pointX, pointY
	}
	return "Yes"
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	timePointList := make([][]int, n)
	for i := 0; i < n; i++ {
		scanner.Scan()
		values := strings.Fields(scanner.Text())
		t, _ := strconv.Atoi(values[0])
		x, _ := strconv.Atoi(values[1])
		y, _ := strconv.Atoi(values[2])
		timePointList[i] = []int{t, x, y}
	}

	fmt.Println(judgePossibleOrImpossible(timePointList))
}
