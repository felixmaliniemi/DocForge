/** Detta är ett exempel på addition */
function add(a, b) { return a + b; }

/** Detta är ett exempel på subtraktion */
function subtract(a, b) { return a - b; }

/** Detta är ett exempel på multiplikation */
function multiply(a, b) { return a * b; }

/** Detta är ett exempel på division */
function divide(a, b) { return b !== 0 ? a / b : null; }

/** Kör alla funktioner med exempelvärden */
function main() {
    console.log("Addition:", add(3,2));
    console.log("Subtraction:", subtract(5,3));
    console.log("Multiplication:", multiply(4,2));
    console.log("Division:", divide(10,2));
}

main();
