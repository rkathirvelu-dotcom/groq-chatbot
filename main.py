import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    """Main function to run the Groq chatbot loop."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Error: GROQ_API_KEY not found. Please set it in your .env file.")
        return

    client = Groq(api_key=api_key)

    # Maintain conversation history for context
    conversation_history = []

    print("=" * 50)
    print("Welcome to the Groq Chatbot!")
    print("Ask me anything. Type 'quit' to exit.")
    print("=" * 50)

    while True:
        # Get user input
        user_input = input("\nYou: ").strip()

        # Check for quit condition
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # Skip empty input
        if not user_input:
            print("Please enter a question or message.")
            continue

        # Add user message to conversation history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        try:
            # Call the Groq API
            chat_completion = client.chat.completions.create(
                messages=conversation_history,
                model="llama3-8b-8192",  # Fast and capable Groq model
                temperature=0.7,
                max_tokens=1024,
            )

            # Extract the assistant's response
            assistant_message = chat_completion.choices[0].message.content

            # Add assistant response to conversation history
            conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })

            print(f"\nAssistant: {assistant_message}")

        except Exception as e:
            print(f"\nError calling Groq API: {e}")
            # Remove the last user message from history if API call failed
            conversation_history.pop()

if __name__ == "__main__":
    main()
