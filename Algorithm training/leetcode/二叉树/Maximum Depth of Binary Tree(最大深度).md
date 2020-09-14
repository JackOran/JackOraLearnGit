### Maximum Depth of Binary Tree

***题目：给定二叉树，找到其最大深度。***

> 给定二叉树`[3,9,20,null,null,15,7]`，
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
>    
>  返回深度3
> ```

```java
//自下而上的递归
class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }
        int left_depth = maxDepth(root.left);
        int right_depth = maxDepth(root.right);
        return Math.max(left_depth,right_depth) + 1;
    }
}
```

```python
#自下而上的递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0;
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth,right_depth) + 1
```

