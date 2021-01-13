class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    insert(data) {
        if (!this.head) {
            this.head = new Node(data);
            return;
        }
        let node = this.head;
        while(node.next !== null) {
            node = node.next;
        }
        node.next = new Node(data);
    }

    traverse() {
        let node = this.head;
        while(node) {
            console.log(node.data);
            node = node.next;
        }
    }

    reverse() {
        let node = this.head;
        let current = node
        let previous = null;
        let next = null;
        while(current) {
            next = current.next;
            current.next = previous;
            previous = current
            current = next
        }
        this.head = previous
    }
}

const ll = new LinkedList();
ll.insert(10);
ll.insert(20);
ll.insert(30);
ll.insert(40);
ll.insert(50);

ll.traverse();
console.log("reversed");
ll.reverse();
ll.traverse();
