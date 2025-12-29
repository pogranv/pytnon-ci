import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(f"Running in CLI mode. 2 + 2 = {add(2, 2)}")
    else:
        print("Hello from Python Calculator!")
