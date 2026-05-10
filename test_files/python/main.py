from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

# Detta kör programmen
def main():
    """Kör alla matematiska operationer med exempelvärden"""
    x = 10
    y = 5

    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))

if __name__ == "__main__":
    main()
