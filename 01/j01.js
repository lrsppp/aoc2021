const path = require('path');
const fs = require('fs');

const input = fs
            .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
            .toString()
            .trim()
            .split('\n')
            .map((num) => parseInt(num, 10));


// Solution 1
function one(input) {
    var count = 0;
    for (var i = 0; i < input.length - 1; i++) {
        if (input[i+1] > input[i]) {
            count += 1;
        }
    }
    return count;
}


// Solution 2
function two(input, window = 3) {
    var sums = [];
    for (var i = 0; i < input.length - window + 1; i++) {
        var sum = 0;
        for (k = 0; k < window; k++) {
            sum += input[i+k];
        }
        sums.push(sum);
    }

    return one(sums);
}

console.log(one(input));
console.log(two(input));


