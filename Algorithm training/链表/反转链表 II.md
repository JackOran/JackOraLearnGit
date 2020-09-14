#### [反转链表 II](https://leetcode-cn.com/problems/reverse-linked-list-ii/)

> 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
>
> 说明:
> 1 ≤ m ≤ n ≤ 链表长度。
>
> 示例:
>
> 输入: 1->2->3->4->5->NULL, m = 2, n = 4
> 输出: 1->4->3->2->5->NULL

##### 递归

```java
class Solution {
    public ListNode reversedN(ListNode head, int n){
        if (head ==null || head.next == null){
            return head;
        }
        ListNode sc = null;
        ListNode successor = head;
        if (n == 1) {
            sc = head.next;
            return head;
        }
        for (int i=1; i<=n; i++){
            successor = successor.next;
        }
        ListNode last = reversedN(head.next, n-1);
        head.next.next = head;
        head.next = successor;
        return last;
    }
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (m == 1){
            return reversedN(head, n);
        }else{
            head.next = reverseBetween(head.next, m-1, n-1);
            return head;
        }
    }
}
```

```python

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        def reverseN(head, n):
            if head == None or head.next == None:
                return head
            sc = None
            successor = head;
            for _ in range(1,n+1):
                successor = successor.next
            if n == 1:
                sc = head.next
                return head
            last = reverseN(head.next, n - 1)
            head.next.next = head
            head.next = successor
            return last
        if m == 1:
            return reverseN(head, n)
        else:
            head.next = self.reverseBetween(head.next, m-1, n-1)
            return head
```



```python
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
				# 反转前n个节点
        def reverseN(head, n):
            if n == 1:
                return head
            last = reverseN(head.next, n - 1)
            #指反转区间外的下一个节点
            successor = head.next.next
            head.next.next = head
            head.next = successor
            return last
        # m = 1 相当于反转前n个节点
        if m == 1:
            return reverseN(head, n)
        # 头节点连接的下一个节点是反转的最后一个节点
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head
```



```python
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        self.successor = None
        def reverseN(head, n):
            if n == 1:
                self.successor = head.next
                return head
            last = reverseN(head.next, n - 1)
            print(head.next)
            # print(successor)
            head.next.next = head
            head.next = self.successor
            return last
        if m == 1:
            return reverseN(head, n)
        # 头节点连接的下一个节点是反转的最后一个节点
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head
```



##### 迭代算法

<img src="/Users/apple/Desktop/document/WechatIMG3.jpeg" alt="WechatIMG3" style="zoom: 33%;" />

```java
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;
        for (int i = 1; i < m; i++){
            pre = pre.next;
        }
        ListNode cur = pre.next;
        for (int j = m; j < n; j++){
            ListNode tmp = cur.next;
          
            cur.next = tmp.next;
            tmp.next = pre.next;
            pre.next = tmp;
        }
        return dummy.next;
    }
}
```

