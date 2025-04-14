calculator/
├── calculator.py         # Main calculator logic
├── main.py               # Entry point
└── README.md             # Project documentation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
from calculator import add, subtract, multiply, divide

def main():
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation: ").lower()

    try:
        if op == 'add':
            result = add(a, b)
        elif op == 'subtract':
            result = subtract(a, b)
        elif op == 'multiply':
            result = multiply(a, b)
        elif op == 'divide':
            result = divide(a, b)
        else:
            raise ValueError("Invalid operation.")

        print(f"Result: {result}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
# 🔢 Simple Python Calculator

A basic calculator implemented in Python with support for:

- Addition
- Subtraction
- Multiplication
- Division

## 🚀 How to Run

```bash
python main.py

---

### 🟩 Upload to GitHub

1. Create a new repository (e.g., `python-calculator`)
2. Push your files:

```bash
git init
git add .
git commit -m "Initial commit: simple calculator"
git remote add origin https://github.com/yourusername/python-calculator.git
git push -u origin main
