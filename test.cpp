
#include "aux.cpp"
// #include "c.cpp"
// #include "416.partition-equal-subset-sum.cpp"
#include "494.target-sum.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	VI nums = {1, 5, 11, 9};
		// nums = {100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100};
	nums = {1, 1, 1, 1, 1};
	// say(s.canPartition(nums));
	s.findTargetSumWays(nums, 3);
	return 0;
}

