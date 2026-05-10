/// Detta är ett exempel på addition
fn add(a: i32, b: i32) -> i32 { a + b }
/// Detta är ett exempel på substraktion
fn subtract(a: i32, b: i32) -> i32 { a - b }
/// Detta är ett exempel på multiplikation
fn multiply(a: i32, b: i32) -> i32 { a * b }
/// Detta är ett exempel på division
fn divide(a: f64, b: f64) -> f64 { if b != 0.0 { a / b } else { 0.0 } }

/** main */
fn main() {
    println!("Addition: {}", add(3,2));
    println!("Subtraction: {}", subtract(5,3));
    println!("Multiplication: {}", multiply(4,2));
    println!("Division: {}", divide(10.0,2.0));
}
