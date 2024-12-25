# Importing Required Libraries
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure genai API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define a function to load gemini-1.5-flash model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question):
    """Fetch a response from the Gemini API for a given question."""
    chat = model.start_chat(history=[])
    response = chat.send_message(question, stream=True)
    return response

def handle_stream_response(response):
    """Process and concatenate streamed response chunks."""
    response_text = ""
    for chunk in response:
        if hasattr(chunk, 'text'):
            response_text += chunk.text
    return response_text

def display_faq():
    """Display a list of Frequently Asked Questions (FAQs)."""
    faq_list = [
        "What is Gemini Pro API?",
        "How do I configure the API key?",
        "What are the usage limits for Gemini Pro?",
        "Can the chatbot handle multi-turn conversations?",
        "How do I exit the chatbot?",
    ]
    print("\nFrequently Asked Questions (FAQs):")
    for i, faq in enumerate(faq_list, 1):
        print(f"{i}. {faq}")

def main():
    """Main loop for the conversational chatbot."""
    print("\n🤖 Conversational Q&A Chatbot Using Gemini Pro API 🧠\n")

    # Initialize chat history
    chat_history = []

    print("Type 'faq' to see the Frequently Asked Questions (FAQs).")

    while True:
        # Accept user input
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chatbot. Goodbye!")
            break
        elif user_input.lower() == "faq":
            display_faq()
            continue

        # Fetch response from Gemini
        try:
            response = get_gemini_response(user_input)
            response_text = handle_stream_response(response)

            # Display and log response
            print(f"Bot: {response_text}\n")
            chat_history.append({"You": user_input, "Bot": response_text})
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    main()
