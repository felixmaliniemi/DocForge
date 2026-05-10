package main
import "fmt"

/** Detta är ett exempel på addition */
func add(a, b int) int { return a + b }
/** Detta är ett exempel på subtraktion */
func subtract(a, b int) int { return a - b }
/** Detta är ett exempel på multiplikation */
func multiply(a, b int) int { return a * b }
/** Detta är ett exempel på division */
func divide(a, b float64) float64 {
    if b != 0 { return a / b }
    return 0
}

/** Kör alla matematiska operationer med exempelvärden */
func main() {
    fmt.Println("Addition:", add(3,2))
    fmt.Println("Subtraction:", subtract(5,3))
    fmt.Println("Multiplication:", multiply(4,2))
    fmt.Println("Division:", divide(10,2))
}
