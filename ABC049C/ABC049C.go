package main

import (
	"fmt"
	"strings"
)

func judgeStrMatch(s string) string {
	rs := reverse(s)
	wordList := []string{reverse("dream"), reverse("dreamer"), reverse("erase"), reverse("eraser")}

	for len(rs) != 0 {
		if strings.HasPrefix(rs, wordList[0]) {
			rs = rs[5:]
		} else if strings.HasPrefix(rs, wordList[1]) {
			rs = rs[7:]
		} else if strings.HasPrefix(rs, wordList[2]) {
			rs = rs[5:]
		} else if strings.HasPrefix(rs, wordList[3]) {
			rs = rs[6:]
		} else {
			return "NO"
		}
	}
	return "YES"
}

func reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func main() {
	var s string
	fmt.Scan(&s)
	fmt.Println(judgeStrMatch(s))
}
