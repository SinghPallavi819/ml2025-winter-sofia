import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.x_data = np.array([])
        self.y_data = np.array([])

    def add_data(self, x_list, y_list):
        self.x_data = np.array(x_list)
        self.y_data = np.array(y_list)

    def predict(self, X):
        if self.k > len(self.x_data):
            raise ValueError("k cannot be greater than the number of data points.")
        
        distances = np.abs(self.x_data - X)
        nearest_indices = np.argsort(distances)[:self.k]
        return np.mean(self.y_data[nearest_indices])

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive integer.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid real number.")

def main():
    N = get_positive_integer("Enter the number of data points (N): ")
    k = get_positive_integer("Enter the number of neighbors (k): ")

    x_vals = []
    y_vals = []

    print(f"\nEnter {N} data points:")
    for i in range(N):
        x = get_float(f"  x[{i+1}]: ")
        y = get_float(f"  y[{i+1}]: ")
        x_vals.append(x)
        y_vals.append(y)

    model = KNNRegressor(k)
    model.add_data(x_vals, y_vals)

    X_query = get_float("\nEnter the value of X for prediction: ")
    try:
        prediction = model.predict(X_query)
        print(f"\nPredicted Y using {k}-NN: {prediction:.4f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
