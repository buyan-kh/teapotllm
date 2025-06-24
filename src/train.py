import teapot as tp
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    # Dummy data - replace with actual data loading logic
    X = np.random.rand(1000, 10)
    y = np.random.randint(0, 2, 1000)
    return X, y

def train_model():
    X, y = load_data()
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = tp.Model()
    
    # Train and evaluate model
    model.fit(X_train, y_train)
    score = model.evaluate(X_test, y_test)
    print(f"Model accuracy: {score}")
    
    model.save("models/trained_model.tp")

if __name__ == "__main__":
    train_model() 