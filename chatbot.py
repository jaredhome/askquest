# chatbot.py

import openai, tiktoken

# Function to count tokens in a text
def count_tokens(conversation_texts):
    total_tokens = 0 
    for conversation in conversation_texts:
        token_count = encoding.encode(conversation)
        total_tokens += len(token_count)
    return total_tokens

def main(user_input=None):
    # Conversation history is a list of conversation turns. It starts with a system message.
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    # Add user input to conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Generate response from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    # Get the response content
    answer = response.choices[0].message.content.strip()

    return answer

