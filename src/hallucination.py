from teapotai import TeapotAI

# Context without height information to test hallucination prevention
context = """
The Eiffel Tower is a wrought iron lattice tower in Paris, France. It was designed by Gustave Eiffel and completed in 1889.
"""

teapot_ai = TeapotAI()

answer = teapot_ai.query(
    query="What is the height of the Eiffel Tower?", 
    context=context
)
print(answer)
