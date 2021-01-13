class Stack {
    constructor() {
        this.data = [];
    }

    push(data) {
        this.data.push(data);
    }

    pop() {
        if (this.data.length === 0) {
            return;
        }

        const length = this.data.length;
        const lastValue = this.data[length-1];
        const newData = [];
        for (let i = 0; i < length-1; ++i) {
            newData.push(this.data[i]);
        }
        this.data = newData;
        return lastValue;
    }
}

const stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
stack.push(4);

console.log(stack.data)

const lastValue = stack.pop();
console.log(lastValue);
console.log(stack.data);
