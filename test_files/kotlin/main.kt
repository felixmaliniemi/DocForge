/** En enkel klass för matte */
class MathOps {
    /** Returnerar summan av två tal */
    fun add(a: Int, b: Int): Int {
        return a + b
    }

    fun subtract(a: Int, b: Int): Int {
        return a - b
    }
}

/** Startpunkt för programmet */
fun main() {
    val m = MathOps()
    println("Addition: ${m.add(2, 3)}")
}
