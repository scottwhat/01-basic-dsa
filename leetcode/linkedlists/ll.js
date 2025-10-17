// Node class for linked list
class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

// Linked List class
class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }

    // Add element to the beginning of the list
    prepend(val) {
        const newNode = new ListNode(val);
        newNode.next = this.head;
        this.head = newNode;
        this.size++;
        return this;
    }

    // Add element to the end of the list
    append(val) {
        const newNode = new ListNode(val);
        
        if (!this.head) {
            this.head = newNode;
        } else {
            let current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = newNode;
        }
        this.size++;
        return this;
    }

    // Insert element at specific index
    insertAt(index, val) {
        if (index < 0 || index > this.size) {
            throw new Error('Index out of bounds');
        }

        if (index === 0) {
            return this.prepend(val);
        }

        const newNode = new ListNode(val);
        let current = this.head;
        
        for (let i = 0; i < index - 1; i++) {
            current = current.next;
        }
        
        newNode.next = current.next;
        current.next = newNode;
        this.size++;
        return this;
    }

    // Remove element from the beginning
    removeFirst() {
        if (!this.head) return null;
        
        const removedVal = this.head.val;
        this.head = this.head.next;
        this.size--;
        return removedVal;
    }

    // Remove element from the end
    removeLast() {
        if (!this.head) return null;
        
        if (!this.head.next) {
            const removedVal = this.head.val;
            this.head = null;
            this.size--;
            return removedVal;
        }

        let current = this.head;
        while (current.next.next) {
            current = current.next;
        }
        
        const removedVal = current.next.val;
        current.next = null;
        this.size--;
        return removedVal;
    }

    // Remove element at specific index
    removeAt(index) {
        if (index < 0 || index >= this.size) {
            throw new Error('Index out of bounds');
        }

        if (index === 0) {
            return this.removeFirst();
        }

        let current = this.head;
        for (let i = 0; i < index - 1; i++) {
            current = current.next;
        }

        const removedVal = current.next.val;
        current.next = current.next.next;
        this.size--;
        return removedVal;
    }

    // Remove first occurrence of a value
    remove(val) {
        if (!this.head) return false;

        if (this.head.val === val) {
            this.head = this.head.next;
            this.size--;
            return true;
        }

        let current = this.head;
        while (current.next && current.next.val !== val) {
            current = current.next;
        }

        if (current.next) {
            current.next = current.next.next;
            this.size--;
            return true;
        }

        return false;
    }

    // Find element and return its index
    indexOf(val) {
        let current = this.head;
        let index = 0;

        while (current) {
            if (current.val === val) {
                return index;
            }
            current = current.next;
            index++;
        }

        return -1;
    }

    // Check if list contains a value
    contains(val) {
        return this.indexOf(val) !== -1;
    }

    // Get element at specific index
    get(index) {
        if (index < 0 || index >= this.size) {
            throw new Error('Index out of bounds');
        }

        let current = this.head;
        for (let i = 0; i < index; i++) {
            current = current.next;
        }

        return current.val;
    }

    // Get the size of the list
    getSize() {
        return this.size;
    }

    // Check if list is empty
    isEmpty() {
        return this.size === 0;
    }

    // Clear the list
    clear() {
        this.head = null;
        this.size = 0;
    }

    // Reverse the linked list
    reverse() {
        let prev = null;
        let current = this.head;
        
        while (current) {
            let next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        
        this.head = prev;
        return this;
    }

    // Convert to array
    toArray() {
        const result = [];
        let current = this.head;
        
        while (current) {
            result.push(current.val);
            current = current.next;
        }
        
        return result;
    }

    // Convert to string
    toString() {
        if (!this.head) return 'null';
        
        const values = [];
        let current = this.head;
        
        while (current) {
            values.push(current.val);
            current = current.next;
        }
        
        return values.join(' -> ') + ' -> null';
    }

    // Print the list
    print() {
        console.log(this.toString());
    }

    // Get middle element (useful for algorithms)
    getMiddle() {
        if (!this.head) return null;
        
        let slow = this.head;
        let fast = this.head;
        
        while (fast.next && fast.next.next) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return slow.val;
    }

    // Detect cycle in the list
    hasCycle() {
        if (!this.head || !this.head.next) return false;
        
        let slow = this.head;
        let fast = this.head;
        
        while (fast && fast.next) {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow === fast) {
                return true;
            }
        }
        
        return false;
    }
}

// Example usage and testing
console.log('=== Linked List Example ===');

const list = new LinkedList();

// Add elements
list.append(1).append(2).append(3);
list.prepend(0);
console.log('After adding elements:', list.toString());

// Insert at specific position
list.insertAt(2, 1.5);
console.log('After inserting 1.5 at index 2:', list.toString());

// Remove elements
console.log('Removed first:', list.removeFirst());
console.log('After removing first:', list.toString());

console.log('Removed last:', list.removeLast());
console.log('After removing last:', list.toString());

// Search operations
console.log('Index of 2:', list.indexOf(2));
console.log('Contains 1.5:', list.contains(1.5));
console.log('Element at index 1:', list.get(1));

// List info
console.log('Size:', list.getSize());
console.log('Is empty:', list.isEmpty());

// Reverse the list
list.reverse();
console.log('After reversing:', list.toString());

// Convert to array
console.log('As array:', list.toArray());

// Get middle element
console.log('Middle element:', list.getMiddle());

// Export for use in other files
module.exports = { ListNode, LinkedList };
