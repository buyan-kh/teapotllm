import pickle

# Save TeapotAI model with pre-computed embeddings
with open("teapot_ai.pkl", "wb") as f:
    pickle.dump(teapot_ai, f)

# Load the saved model
with open("teapot_ai.pkl", "rb") as f:
    loaded_teapot_ai = pickle.load(f)

print(len(loaded_teapot_ai.documents))

loaded_teapot_ai.query("What city is the Eiffel Tower in?")
