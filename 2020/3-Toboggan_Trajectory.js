const getInput = require('./get-input');

async function getMap() {
    const input = await getInput(3);
    return input.split(/\n/g).map(row => row.split(''));
}


function getTreeCount(map, slope) {
    let row = 0;
    let col = 0;
    let treeCount = 0;
    
    while (row < map.length) {
        if (col >= map[row].length) col = col % map[row].length;
        if (map[row][col] === '#') treeCount++;
        row += slope[1];
        col += slope[0];
    }

    return treeCount;
}

async function part1() {
    const map = await getMap();
    console.log(getTreeCount(map, [3, 1]));
}

async function part2() {
    const map = await getMap();
    const slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ];

    let treeProduct = 1;
    slopes.forEach(s => treeProduct *= getTreeCount(map, s));
    console.log(treeProduct);
}

part2();