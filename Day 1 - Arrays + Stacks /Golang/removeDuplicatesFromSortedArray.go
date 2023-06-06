func removeDuplicates(nums []int) int {
	i := 1
	k := 1
	for i < len(nums) {
		if nums[i] == nums[i-1] {
			i = i + 1
		} else {
			nums[k] = nums[i]
			i += 1
			k += 1
		}
	}

	return k
}