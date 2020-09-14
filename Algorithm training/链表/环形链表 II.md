#### [ 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

> 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
>
> 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
>
> 说明：不允许修改给定的链表。

##### 双指针，快慢指针（slow and slow2）

```java
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if (fast == slow){
                ListNode slow2 = head;
                while (slow2 != slow){
                    slow = slow.next;
                    slow2 = slow2.next;
                }
                return slow;
            }
        }
        return null;
    }
}
```

还是前面的龟兔赛跑, 当兔子追到乌龟的时候, 假设有**另外一只乌龟**从头节点开始往前爬, 每次也只爬一个节点, 那么**两只乌龟会在入环的节点相遇**

<img src="https://pic.leetcode-cn.com/a5ff809a09bc095070f7bfd69e0a64667af6ecd186d39f770bd6bed14308e3e5-file_1587171759971" alt="img" style="zoom: 50%;" />

<img src="https://pic.leetcode-cn.com/80bc5db4d5126dacbef822a01e7625b3dc767297a7bf4a87de3c300f92191aec-file_1587171759977" alt="img" style="zoom:50%;" />

```java
public class Solution {
    public ListNode detectCycle(ListNode head) {
        
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if (fast == slow){
                fast = head;
                while (fast != slow){
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;
            }
        }
        return null;
    }
}
```

##### 哈希表

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None
        hashSet = set()
        while head != None:
            if head in hashSet:
                return head
            else:
                hashSet.add(head)
            		head = head.next
        return None
```

