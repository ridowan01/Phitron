var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

let uniq = [numbers[0]];
for (let i = 1; i < numbers.length; i++) {
    if (uniq[uniq.length-1]+1 == numbers[i]) {
        uniq.push(numbers[i]);
    }
}

console.log(uniq);