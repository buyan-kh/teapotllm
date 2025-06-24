import teapot as tp
import numpy as np

def load_model():
    model = tp.Model.load("models/trained_model.tp")
    return model

def predict(model, input_data):
    prediction = model.predict(input_data)
    return prediction

if __name__ == "__main__":
    model = load_model()
    
    # Sample input data
    sample_input = np.random.rand(1, 10)
    
    prediction = predict(model, sample_input)
    print(f"Prediction: {prediction}") 