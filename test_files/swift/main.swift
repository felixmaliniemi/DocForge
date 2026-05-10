/**
  Detta är en klass som innehåller matematiska operationer
*/
class MathOperations {

    /** Returnerar summan av två tal */
    func add(a: Int, b: Int) -> Int { a + b }

    /** Returnerar skillnaden mellan två tal */
    func subtract(a: Int, b: Int) -> Int { a - b }

    /** Returnerar produkten av två tal */
    func multiply(a: Int, b: Int) -> Int { a * b }

    /** Returnerar kvoten av två tal, eller nil om divisor är 0 */
    func divide(a: Int, b: Int) -> Int? { b != 0 ? a / b : nil }
}
