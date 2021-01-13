class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(data) {
        if (!this.root) {
            this.root = new Node(data);
            return;
        }

        this.insertWithNode(this.root, data);
    }

    insertWithNode(node, data) {
        if (data > node.data) {
            if (node.right) {
               this.insertWithNode(node.right, data);
            } else {
                node.right = new Node(data);
            }
        }

        if (data < node.data) {
            if (node.left) {
                this.insertWithNode(node.left, data);
            } else {
                node.left = new Node(data);
            }
        }
    }

    traverseInOrder(node) {
        if (node) {
            this.traverseInOrder(node.left);
            console.log(node.data);
            this.traverseInOrder(node.right);
        }
    }
}

const bst = new BinarySearchTree();
bst.insert(10);
bst.insert(8);
bst.insert(12);
bst.insert(9);
bst.insert(5);
bst.insert(3);
bst.insert(4);
bst.insert(15);
bst.traverseInOrder(bst.root);
