import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load knowledge base
DATASET = "datasets/maasai/qa_dataset.csv"

df = pd.read_csv(DATASET)

# Remove incomplete records
df = df.dropna(subset=["Question", "Answer"])

# Prepare questions
questions = df["Question"].astype(str).tolist()

# Convert questions into numerical vectors
vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(questions)


def answer_question(user_question):

    # Convert user question into a vector
    user_vector = vectorizer.transform([user_question])

    # Compare with stored questions
    similarities = cosine_similarity(
        user_vector,
        question_vectors
    )[0]

    # Find most similar question
    best_index = similarities.argmax()

    score = similarities[best_index]

    # Minimum confidence threshold
    if score < 0.15:
        return "I don't have enough information to answer that."

    result = df.iloc[best_index]

    return {
        "answer": result["Answer"],
        "matched_question": result["Question"],
        "confidence": round(float(score), 3),
        "source": result["Source"]
    }


# Interactive terminal
print("\n=== MAA AI QUESTION ANSWERING ===")
print("Type 'exit' to quit.")

while True:

    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        break

    if not user_input:
        continue

    response = answer_question(user_input)

    if isinstance(response, dict):

        print("\nMaa AI:", response["answer"])
        print("Matched question:", response["matched_question"])
        print("Confidence:", response["confidence"])
        print("Source:", response["source"])

    else:
        print("\nMaa AI:", response)
