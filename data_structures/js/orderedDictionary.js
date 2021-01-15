/*
 * OrderDictionary allows for quick retrieval of k/v pairs while retaining
 * the order of keys when inserting. The implementation uses a traditional
 * object to store k/v pairs allowing for lookup in O(1) and an array to store
 * keys which allows for O(1) insertion and O(n) insertion in the worse case
 * scenerio where n is the number of keys in the keys array.
 *
 * The key to understanding the implementation of OrderedDictionary is the word
 * property "ordered". In a traditonal dictionary, a hashing algorithm is used
 * in order to create a unique index for storing a key, also decreasing the chance
 * of collisions. We must use a linear data type such as an array to retain order
 * of keys and the ability to insert within a given position.
*/

class OrderedDictionary {
    constructor() {
        this.keys = [];
        this.values = {};
        this.size = 0;
    }

    add(key, value) {
        this.keys.push(key);
        this.size++;
        this.values[key] = value;
    }

    insertAt(index, key, value) {
        if (index >  this.size-1) {
            return;
        }
        this.keys.splice(index, 0, key);
        this.values[key] = value;
    }

    get(key) {
        return this.values[key];
    }

    getAt(index) {
        const key = this.keys[index];
        const value = this.values[key];
        return [key, value];
    }
}

const orderedDictionary = new OrderedDictionary();
orderedDictionary.add("John", "Doe");
orderedDictionary.insertAt(0, "apple", "pie");
console.log(orderedDictionary.get("John"));
console.log(orderedDictionary.getAt(0));
