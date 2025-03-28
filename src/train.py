import teapot as tp
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    # Replace this with your actual data loading logic
    # This is just a dummy example
    X = np.random.rand(1000, 10)
    y = np.random.randint(0, 2, 1000)
    return X, y

def train_model():
    # Load data
    X, y = load_data()
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Initialize model
    model = tp.Model()
    
    # Train model
    model.fit(X_train, y_train)
    
    # Evaluate model
    score = model.evaluate(X_test, y_test)
    print(f"Model accuracy: {score}")
    
    # Save model
    model.save("models/trained_model.tp")

if __name__ == "__main__":
    train_model() 