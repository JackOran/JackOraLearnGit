#### [N叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)

给定一个 N 叉树，返回其节点值的*后序遍历*。

例如，给定一个 `3叉树` :

 

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/narytreeexample.png" alt="img" style="zoom:50%;" />

 

返回其后序遍历: `[5,6,3,2,4,1]`.

##### 迭代

```python
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        stack=[root]
        res=[]
        while stack:
            root = stack.pop()
            res.append(root.val)
            for child in root.children:
                stack.append(child)
        return res[::-1]
```

