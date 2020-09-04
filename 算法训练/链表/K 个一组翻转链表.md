### [K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)

> 给你一个链表，每 *k* 个节点一组进行翻转，请你返回翻转后的链表。
>
> *k* 是一个正整数，它的值小于或等于链表的长度。
>
> 如果节点总数不是 *k* 的整数倍，那么请将最后剩余的节点保持原有顺序。

##### 使用栈来实现

```java
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        
        Deque<ListNode> stack = new ArrayDeque<>();
        ListNode dummy = new ListNode(0);
        ListNode p = dummy;
        while (true){
            ListNode tmp = head;
            int count = 0;
            while (tmp != null && count < k){
                stack.push(tmp);
                tmp = tmp.next;
                count ++;
            }
            if (count != k){
                p.next = head;
                break;
            }
            while (!stack.isEmpty()){
                p.next = stack.pop();
                p = p.next;
            }
            p.next = tmp;
            head = tmp;
        }
        return dummy.next;
    }
}
```

##### 递归实现

```python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # 判断是否大于等于k个元素
        def cal_len(head, k):
            p = head
            count = 0
            while p is not None:
                p = p.next
                count += 1
                if count >= k:
                    return True
            return False

        # 对k个元素进行反转
        def reversedK(head, k):
            pre = None
            cur = head
            while k:
                tmp = cur.next
                cur.next = pre

                pre = cur
                cur = tmp
                k -= 1
            return pre, cur

        # 递归整个链表
        def dfs(head, k):
            if not cal_len(head):
                return head
            pre, cur = reversedK(head, k)
            head.next = dfs(cur, k)
            return pre
        return dfs(head, k)
```

<img src="https://pic.leetcode-cn.com/f63d5ca4d3f055ce8e4591c8bc51c288791f88da9ccec9617bc8bb51c26163a2.png" alt="img" style="zoom:50%;" />

```python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if head == None or head.next == None:
            return head
        tail = head
        # 剩余数量小于k不需要反转
        for i in range(k):
            if tail == None:
                return head
            tail = tail.next
        
        # 反转前k个元素
        last = self.reverse(head, tail)
        # 下一轮开始的位置就是tail
        head.next = self.reverseKGroup(tail, k)
        return last
      
    def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
        pre = None
        while head != tail:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre
```

![image-20200903170118879](/Users/apple/Library/Application%20Support/typora-user-images/image-20200903170118879.png)