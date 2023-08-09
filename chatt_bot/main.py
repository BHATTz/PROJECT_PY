# import random

# # Dictionary of predefined prompts and their corresponding responses
# responses = {
#     "hi": "Hello there!",
#     "how are you": "I'm just a chatbot, but I'm here to help!",
#     "what's your name": "I'm ChatBot, nice to meet you!",
#     "bye": "Goodbye! Have a great day!"
# }

# def chatbot_response(user_input):
#     user_input = user_input.lower()  # Convert user input to lowercase
#     response = responses.get(user_input, "I'm not sure how to respond to that.")
#     return response

# # Main loop
# print("ChatBot: Hi, I'm ChatBot. Type 'bye' to exit.")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'bye':
#         print("ChatBot: Goodbye!")
#         break
#     else:
#         bot_response = chatbot_response(user_input)
#         print("ChatBot:", bot_response)

import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",  # You can choose other engines as well
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )
    return response.choices[0].text.strip()

def main():
    print("Chatbot: Hello! I'm your friendly chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        prompt = f"You: {user_input}\nChatbot:"
        response = generate_response(prompt)
        print(response)

if __name__ == "__main__":
    main()
