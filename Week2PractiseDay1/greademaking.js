const number = prompt("Enter your number: ");

if (number >= 80 && number <= 100) {
    console.log("A+");
}
else if (number >= 70 && number < 80) {
    console.log("A");
}
else if (number >= 60 && number < 70) {
    console.log("A-");
}
else if (number >= 50 && number < 60) {
    console.log("B");
}
else if (number >= 40 && number < 50) {
    console.log("C");
}
else if (number >= 33 && number < 40) {
    console.log("D");
}
else if (number >= 0 && number < 33) {
    console.log("F");
}
else {
    console.log("Invalid Number");
}