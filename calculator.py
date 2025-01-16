def get_number(prompt):
    """Get a number from the user or exit."""
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'e':
            return 'exit'
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operand():
    """Get a valid arithmetic operation from the user."""
    while True:
        operand = input("Enter an operation (+, -, *, /, %) (or type 'e' to exit): ").strip()
        if operand.lower() == 'e':
            return 'exit'
        if operand in ["+", "-", "*", "/", "%"]:
            return operand
        print("Invalid operation. Please enter one of +, -, *, /, %.")

def perform_operation(result, operand, next_number):
    """Perform the arithmetic operation and return the updated result."""
    if operand == "+":
        return result + next_number
    elif operand == "-":
        return result - next_number
    elif operand == "*":
        return result * next_number
    elif operand == "/":
        if next_number == 0:
            print("Error: Division by zero is not allowed.")
            return result
        quotient = result / next_number
        remainder = result % next_number
        print(f"Quotient: {quotient}, Remainder: {remainder}")
        return quotient
    elif operand == "%":
        if next_number == 0:
            print("Error: Division by zero is not allowed.")
            return result
        return (next_number/result)*100

def main():
    print("Welcome to the Advanced Calculator! Type 'e' at any prompt to exit.")
    result = 0
    history = []  # To track the operations history

    while True:
        # Get the first number
        first_number = get_number("Enter the first number (or type 'e' to exit): ")
        if first_number == 'exit':
            print("Program exited.")
            break
        result = first_number
        history = [f"Start: {result}"]  # Reset history for a new start

        while True:
            # Get the operand
            operand = get_operand()
            if operand == 'exit':
                print(f"Final result: {result}")
                print("Operation history:")
                print("\n".join(history))
                return

            # Get the next number
            next_number = get_number("Enter the next number (or type 'e' to exit): ")
            if next_number == 'exit':
                print(f"Final result: {result}")
                print("Operation history:")
                print("\n".join(history))
                return

            # Perform the operation
            new_result = perform_operation(result, operand, next_number)
            if new_result != result:
                history.append(f"{result} {operand} {next_number} = {new_result}")
                result = new_result

            print(f"Current result: {result}")

            # Ask for next action
            next_action = input("Do you want to continue (c), start over (s), or exit (e)? ").lower()
            if next_action == "e":
                print(f"Final result: {result}")
                print("Operation history:")
                print("\n".join(history))
                return
            elif next_action == "s":
                print("Starting over...")
                break
            elif next_action != "c":
                print("Invalid input. Continuing with the current operation.")

# Run the main function
if __name__ == "__main__":
    main()
