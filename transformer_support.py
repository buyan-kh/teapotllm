from transformers import pipeline

# Load the model
teapot_ai = pipeline("text2text-generation", "teapotai/teapotllm")

context = """
The Eiffel Tower is a wrought iron lattice tower in Paris, France. It was designed by Gustave Eiffel and completed in 1889.
It stands at a height of 330 meters and is one of the most recognizable structures in the world.
"""

question = "What is the height of the Eiffel Tower?"

answer = teapot_ai(context+"\n"+question)

print(answer[0].get('generated_text')) # => The Eiffel Tower stands at a height of 330 meters.
