func removeElement(nums []int, val int) int {
	i := 0
	k := 0

	for i < len(nums) {
		if nums[i] == val {
			i += 1
		} else {
			nums[k] = nums[i]
			i += 1
			k += 1
		}
	}

	return k
}