const getInput = require('./get-input');

async function getExpenses() {
    const input = await getInput(1);
    return input.trim().split(/\n/g).map(e => parseInt(e));
}
async function part1() {
    const expenses = getExpenses;

    const set = new Set();
    expenses.forEach(e => set.add(e));


    for (let num of set) {
        if (set.has(2020 - num)) {
            return console.log(num * (2020 - num));
        }
    }

    return console.log('not found');
}

async function part2() {
    const expense = await getExpenses();

    const map = new Map();
    
    for (let i = 0; i < expense.length; i++) {
        for (let j = i + 1; j < expense.length; j++) {
            map.set(expense[i] + expense[j], [i, j]);
        }
    }

    for (let i = 0; i < expense.length; i++) {
        let key = 2020 - expense[i];
        const combo = map.get(key);

        if (!!combo && !combo.includes(i)) {
            return console.log(expense[combo[0]] * expense[combo[1]] * expense[i]);
        }
    }

    return console.log('not found');
}

part2();