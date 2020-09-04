#### [删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

> 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
>
> 示例：
>
> 给定一个链表: 1->2->3->4->5, 和 n = 2.
>
> 当删除了倒数第二个节点后，链表变为 1->2->3->5.
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

为了方便，我们在原有链表前面设置一个**哑结点**，哑结点的好处在于，因为这里我们是要删除一个结点，所以我们可以定位到**被删除结点的前置结点**，然后将**前置结点的后续指针指向被删除结点的后续结点**，则可完成删除。

我们设置两个指针，两个指针初始状态都指向哑结点，**指针fast 先走n步**，然后指针fast和指针slow同步往前继续遍历链表，直至fast的后续结点为空，此时指针slow到达被删除结点的前置结点。

<img src="https://pic.leetcode-cn.com/4fbd5f3602bdbd44bd3a9ecc37ca8a029f6fd204fb28ac0627bc59fbccba6211-file_1587171760112" alt="img" style="zoom:50%;" />

<img src="https://pic.leetcode-cn.com/fdeb9e5c2ba212e82d333bcc50688c18679817ed0156f764c5f40fd8a6ada763-file_1587171760150" alt="img" style="zoom:50%;" />

<img src="https://pic.leetcode-cn.com/4168b225162a774750585a1c65c3748b6f3164cc6b12363702916690c4c28114-file_1587171760156" alt="img" style="zoom:50%;" />

<img src="https://pic.leetcode-cn.com/29ef677aeedfc72e2a4094c72b5f3e7cb6734d3c587ca127a10ea989b30799f8-file_1587171760168" alt="img" style="zoom:50%;" />

<img src="https://pic.leetcode-cn.com/9680476d590fd8138c5d6bd1d9b41baac280fbbcf16af5a39a15f103ddaf0bea-file_1587171760192" alt="img" style="zoom:50%;" />

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while n >= 0:
            fast = fast.next
            n -= 1
        while fast != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
```



```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode slow = dummy;
        ListNode fast = dummy;
        while (n >= 0){
            fast = fast.next;
            n--;
        }
        while (fast != null){
            slow = slow.next;
            fast = fast.next;
        }
        // if (slow.next == head){
        //     return head;
        // } else {
        //     slow.next = slow.next.next;
        // }
        slow.next = slow.next.next;
        return dummy.next;
    }
}
```

