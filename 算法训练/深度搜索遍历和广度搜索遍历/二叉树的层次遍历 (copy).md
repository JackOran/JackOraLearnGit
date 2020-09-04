### [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/)

给你一个二叉树，请你返回其按 **层序遍历** 得到的节点值。 （即逐层地，从左到右访问所有节点）。

#### BFS求解

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        res = []
        while queue:
          	# 储存每一层的节点
            current_layer = []
            for _ in range(len(queue)):
                root = queue.pop(0)
                current_layer.append(root.val)
                print(current_layer)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(current_layer)
            # print(res)
        return res
```



#### DFS递归求解

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(index, root):
            # terminator
            if len(res) < index:
                res.append([])
            # process current logic
            res[index - 1].append(root.val)
            # drill down
            if root.left:
                dfs(index + 1, root.left)
            if root.right:
                dfs(index + 1, root.right)
        dfs(1, root)
        return res
```

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        List<List<Integer>> res = new ArrayList<>();
        if (root == null){
            return res;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()){
            int size = queue.size();
            List<Integer> current_layer = new ArrayList<>();
            for (int i = 0; i < size; i++){
                root = queue.poll();
                current_layer.add(root.val);
                if (root.left != null){
                    queue.offer(root.left);
                }
                if (root.right != null){
                    queue.offer(root.right);
                }
            }
            res.add(current_layer);
        }
        return res;
    }
}
```

