    class ListNode {
    int val;
    ListNode next;

    public ListNode(int val) {
        this.val = val;
    }
}

public class RecursiveReverseLinkedList {

    public static ListNode reverseList(ListNode head) {
        // Base case: If the list is empty or has only one node, return the current head
        if (head == null || head.next == null) {
            return head;
        }

        // Recursive case: Reverse the rest of the list
        ListNode reversedList = reverseList(head.next);

        // Make the current node the new tail and update its next pointer
        head.next.next = head;
        head.next = null;

        return reversedList;
    }

    public static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        System.out.println("Original linked list:");
        printList(head);

        // Reversing the linked list recursively
        head = reverseList(head);

        System.out.println("Reversed linked list:");
        printList(head);
    }
}
