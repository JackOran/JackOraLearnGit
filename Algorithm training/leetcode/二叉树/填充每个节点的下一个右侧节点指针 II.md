### 填充每个节点的下一个右侧节点指针 II

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/117_sample.png)

```java
class Solution {
    public Node connect(Node root) {
        //队列
        if (root == null) return null;
        Queue<Node> queue = new LinkedList<>();
		queue.add(root);
		
		while (!queue.isEmpty()) {
			int size = queue.size();
			Node prev = null;
			for (int i = 0; i < size; i++) {
				Node node = queue.poll();
				node.next = prev;
				prev = node;
				
				if (node.right != null) {
					queue.add(node.right);
				}
                
				if (node.left != null) {
					queue.add(node.left);
				}
				
			}
		}
		
		return root;
    }
}
```

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        queue = [root]
        #层次遍历
        while queue:
            tmp = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                tmp.append(cur)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            for i in range(len(tmp)-1):
                tmp[i].next = tmp[i+1]
        return root
            
```

