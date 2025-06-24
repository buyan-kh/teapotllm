#!/usr/bin/env python3
"""
Simple RAG demo without requiring the TeapotAI model
Shows the concept of retrieval-augmented generation
"""

import re
from typing import List, Dict

class SimpleRAG:
    def __init__(self, documents: List[str]):
        self.documents = documents
    
    def retrieve(self, query: str, top_k: int = 3) -> List[str]:
        """Simple keyword-based retrieval"""
        query_words = set(query.lower().split())
        doc_scores = []
        
        for doc in self.documents:
            doc_words = set(re.findall(r'\w+', doc.lower()))
            score = len(query_words.intersection(doc_words))
            doc_scores.append((score, doc))
        
        # Sort by score and return top_k
        doc_scores.sort(reverse=True, key=lambda x: x[0])
        return [doc for _, doc in doc_scores[:top_k] if _ > 0]
    
    def answer_question(self, question: str) -> str:
        """Generate answer based on retrieved documents"""
        relevant_docs = self.retrieve(question)
        
        if not relevant_docs:
            return "I don't have information to answer that question."
        
        # Simple rule-based answering for demo
        context = " ".join(relevant_docs)
        
        # Extract key facts based on question type
        if "height" in question.lower() or "tall" in question.lower():
            height_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:meters?|feet|ft)', context, re.IGNORECASE)
            if height_match:
                return f"Based on the documents, the height is {height_match.group(1)} {height_match.group(0).split()[-1]}."
        
        if "when" in question.lower() or "built" in question.lower() or "constructed" in question.lower():
            year_match = re.search(r'\b(1[6-9]\d{2}|20\d{2})\b', context)
            if year_match:
                return f"According to the documents, it was built/constructed in {year_match.group(1)}."
        
        if "where" in question.lower() or "located" in question.lower():
            location_match = re.search(r'(?:located in|in)\s+([A-Z][^.,]+)', context)
            if location_match:
                return f"It is located in {location_match.group(1).strip()}."
        
        # Fallback: return first relevant sentence
        sentences = re.split(r'[.!?]', context)
        if sentences:
            return sentences[0].strip() + "."
        
        return "Based on the available documents: " + relevant_docs[0][:100] + "..."

# Demo documents about landmarks
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

def demo_interactive():
    """Interactive demo version"""
    rag = SimpleRAG(documents)
    
    print("🫖 TeapotAI Interactive RAG Demo")
    print("=" * 40)
    print("Ask questions about landmarks! (or 'demo' for auto-demo)")
    
    while True:
        try:
            question = input("\nQuestion: ").strip()
            if question.lower() in ['quit', 'exit', 'q']:
                break
            elif question.lower() == 'demo':
                demo_automatic()
                continue
            elif question:
                answer = rag.answer_question(question)
                relevant_docs = rag.retrieve(question)
                print(f"Answer: {answer}")
                print(f"Used {len(relevant_docs)} documents")
        except (EOFError, KeyboardInterrupt):
            break

def demo_automatic():
    """Automatic demo showing RAG capabilities"""
    rag = SimpleRAG(documents)
    
    print("\n🫖 TeapotAI RAG Demo")
    print("=" * 40)
    print("Demonstrating retrieval-augmented generation\n")
    
    sample_questions = [
        "What landmark was constructed in the 1800s?",
        "How tall is the Eiffel Tower?", 
        "Where is Mount Everest located?",
        "What is the longest river in the world?",
        "Which desert is in North Africa?",
        "What building was completed in 1931?"
    ]
    
    for question in sample_questions:
        print(f"Q: {question}")
        answer = rag.answer_question(question)
        relevant_docs = rag.retrieve(question)
        print(f"A: {answer}")
        if relevant_docs:
            print(f"📄 Retrieved: {relevant_docs[0][:80]}...")
        print("-" * 50)

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        demo_interactive()
    else:
        demo_automatic()

if __name__ == "__main__":
    main()