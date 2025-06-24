from teapotai import TeapotAI

# Sample documents for RAG system
documents = [
    "The Eiffel Tower is located in Paris, France. It was built in 1889 and stands 330 meters tall.",
    "The Great Wall of China is a historic fortification that stretches over 13,000 miles.",
    "The Amazon Rainforest is the largest tropical rainforest in the world, covering over 5.5 million square kilometers.",
    "The Grand Canyon is a natural landmark located in Arizona, USA, carved by the Colorado River.",
    "Mount Everest is the tallest mountain on Earth, located in the Himalayas along the border between Nepal and China.",
    "The Colosseum in Rome, Italy, is an ancient amphitheater known for its gladiator battles.",
    "The Sahara Desert is the largest hot desert in the world, located in North Africa.",
    "The Nile River is the longest river in the world, flowing through northeastern Africa.",
    "The Empire State Building is an iconic skyscraper in New York City that was completed in 1931 and stands at 1454 feet tall."
]

# Initialize TeapotAI with documents for RAG
teapot_ai = TeapotAI(documents=documents)

# Get the answer using RAG
answer = teapot_ai.chat([
    {
        "role":"system",
        "content": "You are an agent designed to answer facts about famous landmarks."
    },
    {
        "role":"user",
        "content": "What landmark was constructed in the 1800s?"
    }
])
print(answer) # => The Eiffel Tower was constructed in the 1800s.
