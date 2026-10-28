package go_solutions

import "slices"

func permute(nums []int) [][]int {
    n := len(nums)

	// res := [][]in{} empty non-nil slice points to memory address, Go allocates memory great for encoding data to JSON.

	var res [][]int // empty nil  doesn't allocate/point to memory address
	var sol []int

	// func backtrack() showed error because named func inside another func is not allowed in Go

	// 1. Declare the nested func variable
	var backtrack func()

	// 2. Define the anonymous function
	backtrack = func() {
		if len(sol) == n {
			temp := make([]int, len(sol))
			copy(temp, sol) // ln 23-24 prevent mutation of res
			res = append(res, temp)
		}

		for _, val := range nums {
			if slices.Contains(sol, val){
				continue
			}

			sol = append(sol, val)
			backtrack()
			sol = sol[:len(sol)-1]
		}
	}

	backtrack()

	return res
}