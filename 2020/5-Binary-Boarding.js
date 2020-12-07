const getInput = require('./get-input');

async function getSeats() {
    return (await getInput(5)).trim().split(/\n/g);
}


function binarySearch(range, lowerSymbol, string) {
    let lower = 0;
    let upper = range - 1;

    for (let char of string) {
        const midPoint = Math.floor((upper - lower) / 2) + lower;

        if (char === lowerSymbol) {
            upper = midPoint;
        } else {
            lower = midPoint;
        }
    }

    return upper;
}

async function part1() {
    const seats = await getSeats();
    let maxId = 0;

    seats.forEach(s => {
        const row = binarySearch(128, 'F', s.substring(0, 7));
        const col = binarySearch(8, 'L', s.substring(7));
 
        maxId = Math.max(maxId, row * 8 + col);
        if (maxId === (row * 8 + col)) console.log(s, row, col);
    });
}

async function part2() {
    const seats = await getSeats();
    const seatIds = seats.map(s => {
        const row = binarySearch(128, 'F', s.substring(0, 7));
        const col = binarySearch(8, 'L', s.substring(7));

        return row * 8 + col
    }).sort();

    
    for (let i = 0; i < seatIds.length; i++) {
        if(seatIds[i]+2 === seatIds[i+1]) return console.log(seatIds[i]+1)
    }
    
}

part2();
