# Detta är ett exempel på addition
add() { echo $(($1 + $2)) }

# Detta är ett exempel på subtraktion
subtract() { echo $(($1 - $2)) }

# Detta är ett exempel på multiplikation
multiply() { echo $(($1 * $2)) }

# Detta är ett exempel på division
divide() { if [ $2 -ne 0 ]; then echo $(($1 / $2)); else echo 0; fi }

# Kör alla matematiska operationer med exempelvärden
main() 
{
  echo "Addition: $(add 3 2)"
  echo "Subtraction: $(subtract 5 3)"
  echo "Multiplication: $(multiply 4 2)"
  echo "Division: $(divide 10 2)"
}
