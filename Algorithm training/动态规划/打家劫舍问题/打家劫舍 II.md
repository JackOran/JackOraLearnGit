#### [打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/)

> 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
>
> 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
>
> 示例 1:
>
> 输入: [2,3,2]
> 输出: 3
> 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
> 示例 2:
>
> 输入: [1,2,3,1]
> 输出: 4
> 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
>      偷窃到的最高金额 = 1 + 3 = 4 。

#### 动态规划解决问题

1. 将环形房屋变为两个单排的房屋
   - 偷第一个房屋，不偷最后一个房屋获取的最大值Max1
   - 偷最后一个房屋，不偷第一个房屋获取的最大值Max2
   - return max(Max1, Max2)

```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        int n = nums.length;
        int[] dp1 = new int[n];
        int[] dp2 = new int[n];
        dp1[0] = nums[0];
        dp1[1] = Math.max(nums[0], nums[1]);

        dp2[n - 1] = nums[n - 1];
        dp2[n - 2] = Math.max(nums[n - 1], nums[n - 2]);
        int res1 = Math.max(dp1[0], dp1[1]);
        int res2 = Math.max(dp2[n-1], dp2[n-2]);
        //偷窃第一个房子的情况下
        for (int i = 2; i < n - 1; i++) {
            dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + nums[i]);
            res1 = Math.max(res1, dp1[i]);
        }
        //偷窃最后一个房子的情况下
        for (int j = n - 3; j > 0; j--) {
            dp2[j] = Math.max(dp2[j+1] + 0, dp2[j+2] + nums[j]);
            res2 = Math.max(res2,dp2[j]);
        }
        return Math.max(res1, res2);
    }
}
```

```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        int n = nums.length;
        int[] dp1 = new int[n];
        int[] dp2 = new int[n];
        dp1[0] = nums[0];
        dp1[1] = Math.max(nums[0], nums[1]);

        dp2[n - 1] = nums[n - 1];
        dp2[n - 2] = Math.max(nums[n - 1], nums[n - 2]);
        //int res1 = Math.max(dp1[0], dp1[1]);
        //int res2 = Math.max(dp2[n-1], dp2[n-2]);
        //偷窃第一个房子的情况下
        for (int i = 2; i < n - 1; i++) {
            dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + nums[i]);
            //res1 = Math.max(res1, dp1[i]);
        }
        //偷窃最后一个房子的情况下
        for (int j = n - 3; j > 0; j--) {
            dp2[j] = Math.max(dp2[j+1] + 0, dp2[j+2] + nums[j]);
            //res2 = Math.max(res2,dp2[j]);
        }
        //return Math.max(res1, res2);
      	return Math.max(dp1[n-2], dp2[1]);
    }
}
```

