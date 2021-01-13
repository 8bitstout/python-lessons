class Node {
    constructor() {
        this.data = new Array(26);
        this.isWord = false;
    }

    hasDataAtIndex(i) {
        return this.data[i] !== undefined;
    }

    insert(i) {
        this.data[i] = new Node();
    }
}

class Trie {
    constructor() {
        this.root = new Node();
    }

    insert(word) {
        let node = this.root;
        [...word].forEach(letter => {
            let i = this.getIndex(letter);
            if (!node.hasDataAtIndex(i)) {
                node.insert(i);
            }
            node = node.data[i];
        });
        node.isWord = true;
    }

    contains(word) {
        let node = this.root;
        let letters = [...word];
        for (let i = 0; i < letters.length; ++i) {
            let letter = letters[i];
            let index = this.getIndex(letter);
            if (!node.hasDataAtIndex(index)) {
                return false;
            }
            node = node.data[index];
        }
        return node.isWord;
    }

    getIndex(char) {
        return char.charCodeAt() -  "a".charCodeAt();
    }
}

const trie = new Trie();
const validWords = ["hello", "world", "javascript"];

validWords.forEach(word => {
    trie.insert(word);
    console.log(`Insert "${word}" into Trie`);
});

const invalidWords = ["python", "goodbye"];

const wordsToSearch = [...validWords, ...invalidWords];

wordsToSearch.forEach(word => {
    const foundWord = trie.contains(word);
    if (foundWord) {
        console.log(`"${word}" exists in the Trie`);
    } else {
        console.log(`"${word}" does not exist in the Trie`);
    }
});
