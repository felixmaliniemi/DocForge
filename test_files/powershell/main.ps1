<# Detta är ett exempel på addition #>
function Add($a, $b) { return $a + $b }
<# Detta är ett exempel på subtraction #>
function Subtract($a, $b) { return $a - $b }
<# Detta är ett exempel på multiplication #>
function Multiply($a, $b) { return $a * $b }
<# Detta är ett exempel på division #>
function Divide($a, $b) { if ($b -ne 0) { return $a / $b } else { return 0 } }

<# Main #>
Write-Output "Addition: $(Add 3 2)"
Write-Output "Subtraction: $(Subtract 5 3)"
Write-Output "Multiplication: $(Multiply 4 2)"
Write-Output "Division: $(Divide 10 2)"
