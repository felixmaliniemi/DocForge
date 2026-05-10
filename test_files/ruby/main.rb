=begin addition 
=end
def add(a, b) a + b end
=begin substraktion 
=end
def subtract(a, b) a - b end
=begin multiplikation 
=end
def multiply(a, b) a * b end
=begin division 
=end
def divide(a, b) b != 0 ? a / b : nil end

=begin 
main 
=end
def main
  puts "Addition: #{add(3,2)}"
  puts "Subtraction: #{subtract(5,3)}"
  puts "Multiplication: #{multiply(4,2)}"
  puts "Division: #{divide(10,2)}"
end