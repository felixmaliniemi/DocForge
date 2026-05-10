using System;

/** MathOperations innehåller grundläggande matematiska funktioner */
class MathOperations
{
    /** Detta är ett exempel på addition */
    public static int Add(int a, int b) { return a + b; }

    /** Detta är ett exempel på subtraktion */
    public static int Subtract(int a, int b) { return a - b; }

    /** Detta är ett exempel på multiplikation */
    public static int Multiply(int a, int b) { return a * b; }

    /** Detta är ett exempel på division */
    public static double Divide(double a, double b) { return b != 0 ? (double)a / b : 0; }

    /** Kör alla matematiska operationer med exempelvärden */
    public static void Main()
    {
        Console.WriteLine("Addition: " + Add(3, 2));
        Console.WriteLine("Subtraction: " + Subtract(5, 3));
        Console.WriteLine("Multiplication: " + Multiply(4, 2));
        Console.WriteLine("Division: " + Divide(10, 2));
    }
}
