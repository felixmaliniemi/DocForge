# Detta är ett exempel på addition
sub add {
    my ($a, $b) = @_;
    return $a + $b;
}
# Detta är ett exempel på subtraction
sub subtract {
    my ($a, $b) = @_;
    return $a - $b;
}
# Detta är ett exempel på multiplikation
sub multiply {
    my ($a, $b) = @_;
    return $a * $b;
}
# Detta är ett exempel på division
sub divide {
    my ($a, $b) = @_;
    return $b != 0 ? $a / $b : undef;
}

# Main
print "Addition: " . add(3,2) . "\n";
print "Subtraction: " . subtract(5,3) . "\n";
print "Multiplication: " . multiply(4,2) . "\n";
print "Division: " . divide(10,2) . "\n";
