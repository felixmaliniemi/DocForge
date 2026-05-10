/** MathOps innehåller grundläggande matematiska operationer */
public class MathOps {

    /** Returnerar summan av a och b */
    public static int add(int a, int b) {
        return a + b;
    }

    /** Returnerar skillnaden mellan a och b */
    public static int subtract(int a, int b) {
        return a - b;
    }

    /** Returnerar produkten av a och b */
    public static double multiply(double a, double b) {
        return a * b;
    }

    /** Returnerar kvoten av a och b. Returnerar 0 om b är 0 */
    public static double divide(double a, double b) {
        if (b == 0) return 0;
        return a / b;
    }

    /** Kör alla matematiska operationer med exempelvärden och skriver ut resultatet */
    public static void main(String[] args) {
        System.out.println("Addition: " + add(3, 2));
        System.out.println("Subtraction: " + subtract(5, 3));
        System.out.println("Multiplication: " + multiply(4, 2));
        System.out.println("Division: " + divide(10, 2));
    }
}
