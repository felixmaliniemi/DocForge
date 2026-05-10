/** 
  * Detta är ett exempel på addition
  * Objekt som innehåller grundläggande matematiska operationer
  */
object MathOperations {

  /** Returnerar summan av två tal */
  def add(a: Int, b: Int): Int = a + b

  /** Returnerar skillnaden mellan två tal */
  def subtract(a: Int, b: Int): Int = a - b

  /** Returnerar produkten av två tal */
  def multiply(a: Int, b: Int): Int = a * b

  /** Returnerar kvoten av två tal, eller None om divisor är 0 */
  def divide(a: Int, b: Int): Option[Double] = if (b != 0) Some(a.toDouble / b) else None

  /** Startpunkt för programmet */
  def main(args: Array[String]): Unit = {
    println(s"Addition: ${add(3,2)}")
    println(s"Subtraction: ${subtract(5,3)}")
    println(s"Multiplication: ${multiply(4,2)}")
    println(s"Division: ${divide(10,2).getOrElse("null")}")
  }
}
