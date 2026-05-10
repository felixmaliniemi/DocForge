/**
 * Detta är en klass som innehåller matematiska operationer
 */
class MathOperations {

    /** Returnerar summan av två tal */
    add(a: number, b: number): number {
        return a + b;
    }

    /** Returnerar skillnaden mellan två tal */
    subtract(a: number, b: number): number {
        return a - b;
    }

    /** Returnerar produkten av två tal */
    multiply(a: number, b: number): number {
        return a * b;
    }

    /** Returnerar kvoten av två tal, eller null om divisor är 0 */
    divide(a: number, b: number): number | null {
        return b !== 0 ? a / b : null;
    }
}
