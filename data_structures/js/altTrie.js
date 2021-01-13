class Node {
    constructor() {
        this.data = {};
        this.isWord = false;
    }

    hasKey(k) {
        return this.data[k] !== undefined;
    }

    insert(k) {
        this.data[k] = new Node();
    }
}

class Trie {
    constructor() {
        this.root = new Node();
    }

    insert(word) {
        let node = this.root;
        [...word].forEach(char => {
            if (!node.hasKey(char)) {
                node.insert(char);
            }
            node = node.data[char];
        });
        node.isWord = true;
    }

    contains(word) {
        let chars = [...word];
        let node = this.root;
        for (let i = 0; i < chars.length; ++i) {
            let char = chars[i];
            if (!node.hasKey(char)) {
                return false;
            }
            node = node.data[char];
        }
        return node.isWord;
    }
}

const trie = new Trie();
const validWords = ["Hello", "JavaScript", "l33t"];
const invalidWords = ["Python", "g00dby3!"];

validWords.forEach(word => {
    trie.insert(word);
});

const wordsToSearch = [...validWords, ...invalidWords];

wordsToSearch.forEach(word => {
    let found = trie.contains(word);
    if (found) {
        console.log(`${word} was found in the Trie`);
    } else {
        console.log(`${word} was not found in the Trie`);
    }
});
