from transformers import pipeline

pipe = pipeline("text2text-generation", model="teapotai/teapotllm")

from teapotai import TeapotAI

# Sample context
context = """
The Eiffel Tower is a wrought iron lattice tower in Paris, France. It was designed by Gustave Eiffel and completed in 1889.
It stands at a height of 330 meters and is one of the most recognizable structures in the world.
"""

teapot_ai = TeapotAI()

answer = teapot_ai.query(
    query="What is the height of the Eiffel Tower?", 
    context=context
)
print(answer) # => "The Eiffel Tower stands at a height of 330 meters. "
