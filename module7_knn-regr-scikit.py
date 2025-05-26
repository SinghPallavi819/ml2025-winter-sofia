import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    try:
        N = int(input("Enter the number of training points (N): "))
        if N <= 0:
            print("N must be a positive integer.")
            return

        k = int(input("Enter the value of k (for k-NN): "))
        if k <= 0:
            print("k must be a positive integer.")
            return

        print(f"Enter {N} data points:")
        x_values = np.empty((N, 1))
        y_values = np.empty((N,))

        for i in range(N):
            x = float(input(f"Enter x value for point {i+1}: "))
            y = float(input(f"Enter y value for point {i+1}: "))
            x_values[i] = x
            y_values[i] = y

        X_input = float(input("Enter the X value to predict Y using k-NN regression: "))

        if k > N:
            print("Error: k cannot be greater than N.")
            return

        model = KNeighborsRegressor(n_neighbors=k)
        model.fit(x_values, y_values)
        prediction = model.predict([[X_input]])

        print(f"\nPredicted Y value: {prediction[0]:.4f}")
        print(f"Variance of Y values in the dataset: {np.var(y_values):.4f}")

    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()