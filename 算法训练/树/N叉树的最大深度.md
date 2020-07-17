#### [N叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/)

> 给定一个 N 叉树，找到其最大深度。
>
> 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
>
> 例如，给定一个 3叉树 :
>
>  <img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/narytreeexample.png" alt="img" style="zoom:50%;" />
>
> 我们应返回其最大深度，3。

#### 递归求解

```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        elif root.children == []:
            return 1
        else:
            depth = [self.maxDepth(child) for child in root.children]
            return max(depth) + 1
```

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int maxDepth(Node root) {
        List<Integer> depth = new ArrayList<>();
        if (root == null){
            return 0;
        }else if (root.children.isEmpty()){
            return 1;
        }else {
            for (Node child : root.children){
                depth.add(maxDepth(child));
            }
        }
        return Collections.max(depth) + 1;
    }
}
```

