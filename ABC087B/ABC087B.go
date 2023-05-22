package main

import (
	"fmt"
)

func getPatternSelectCoins(yen500Num int, yen100Num int, yen50Num int, yenSum int) int {
	const (
		FiveHundred = 500
		OneHundred  = 100
		Fifty       = 50
	)

	count := 0
	if yen500Num*FiveHundred+yen100Num*OneHundred+yen50Num*Fifty < yenSum {
		return 0
	} else if yenSum/Fifty%2 != 0 && yen50Num == 0 {
		return 0
	} else {
		for i := 0; i <= yen500Num; i++ {
			if FiveHundred*i > yenSum {
				break
			}
			remain500 := yenSum - FiveHundred*i
			for j := 0; j <= yen100Num; j++ {
				if OneHundred*j > remain500 {
					break
				}
				remain100 := remain500 - OneHundred*j
				if remain100 <= Fifty*yen50Num {
					if remain100%Fifty == 0 {
						count++
					}
				}
			}
		}
		return count
	}
}

func main() {
	var yen500Num, yen100Num, yen50Num, yenSum int
	fmt.Scan(&yen500Num, &yen100Num, &yen50Num, &yenSum)

	fmt.Println(getPatternSelectCoins(yen500Num, yen100Num, yen50Num, yenSum))
}
