<?php
/** Detta är ett exempel på addition */
function add($a, $b) {
    return $a + $b;
}

/** Returnerar skillnaden mellan två tal */
function subtract($a, $b) {
    return $a - $b;
}

/** Returnerar produkten av två tal */
function multiply($a, $b) {
    return $a * $b;
}

/** Returnerar kvoten av två tal, eller null om divisor är 0 */
function divide($a, $b) {
    return $b != 0 ? $a / $b : null;
}

/** Startpunkt för programmet */
function main() {
    echo "Addition: " . add(3, 2) . "\n";
    echo "Subtraction: " . subtract(5, 3) . "\n";
    echo "Multiplication: " . multiply(4, 2) . "\n";
    echo "Division: " . divide(10, 2) . "\n";
}

main();
?>
