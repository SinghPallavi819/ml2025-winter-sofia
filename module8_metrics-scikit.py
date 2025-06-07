import numpy as np
from sklearn.metrics import precision_score, recall_score

def get_binary(prompt):
    """Accepts only binary (0 or 1) input from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1):
                return value
            else:
                print("Please enter only 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter 0 or 1.")

def main():
    try:
        N = int(input("Enter the number of data points (N): "))
        if N <= 0:
            print("N must be a positive integer.")
            return

        x_values = np.empty(N, dtype=int)  # Ground truth (actual labels)
        y_values = np.empty(N, dtype=int)  # Predicted labels

        print("\nEnter N binary points (X = ground truth, Y = predicted):")
        for i in range(N):
            print(f"\nPoint {i+1}:")
            x = get_binary("  Enter X value (0 or 1): ")
            y = get_binary("  Enter Y value (0 or 1): ")
            x_values[i] = x
            y_values[i] = y

        precision = precision_score(x_values, y_values, zero_division=0)
        recall = recall_score(x_values, y_values, zero_division=0)

        print("\n--- Evaluation Metrics ---")
        print(f"Precision: {precision:.2f}")
        print(f"Recall:    {recall:.2f}")

    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
