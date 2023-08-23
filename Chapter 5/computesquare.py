def main():
    """The main function for this script"""
    number = float(input("Enter a number: "))
    results = square(number)
    print("The square of", number, "is", results)
def square(x):
    """Return the square of x."""
    return x*x

# The entry point for program execution. A call for main must be included.
# in the script.
if __name__ == "__main__":
    main()
