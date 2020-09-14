#### [N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/narytreeexample.png" alt="img" style="zoom:50%;" />

返回其层序遍历:

```
[
     [1],
     [3,2,4],
     [5,6]
]
```

##### 迭代

```python
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        res = []
        deque = [root]
        while deque:
          # 每一层
            current_layer = []
            for _ in range(len(deque)):
                root = deque.pop(0)
                current_layer.append(root.val)
                for child in root.children:
                    deque.append(child)
            res.append(current_layer)
        return res
```

