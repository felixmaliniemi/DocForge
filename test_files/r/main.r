#' Detta är ett exempel på addition
add <- function(a, b) {
  return(a + b)
}
#' Detta är ett exempel på substraktion
subtract <- function(a, b) {
  return(a - b)
}
#' Detta är ett exempel på multiplikation
multiply <- function(a, b) {
  return(a * b)
}
#' Detta är ett exempel på division
divide <- function(a, b) {
  if(b != 0) return(a / b) else return(NA)
}

#' Main
print(paste("Addition:", add(3,2)))
print(paste("Subtraction:", subtract(5,3)))
print(paste("Multiplication:", multiply(4,2)))
print(paste("Division:", divide(10,2)))
