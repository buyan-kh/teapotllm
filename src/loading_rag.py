import pickle

# Pickle the TeapotAI model to a file with pre-computed embeddings
with open("teapot_ai.pkl", "wb") as f:
    pickle.dump(teapot_ai, f)


# Load the pickled model
with open("teapot_ai.pkl", "rb") as f:
    loaded_teapot_ai = pickle.load(f)

# You can now use the loaded instance as you would normally
print(len(loaded_teapot_ai.documents)) # => 10 Documents with precomputed embeddings

loaded_teapot_ai.query("What city is the Eiffel Tower in?") # => "The Eiffel Tower is located in Paris, France."
