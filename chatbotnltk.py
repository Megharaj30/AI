import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot pairs (patterns and responses)
pairs = [
    [
        r"gm|good morning",  # Match product inquiry
        ["Good Morning ! How can I help you ?",],
    ],
    [
        r"hi|hey|hello",  # Match common greetings
        ["Hello! How can I assist you today?", "Hey there! How can I help you today?", "Hi, welcome! How can I assist you today?"],
    ],
    [
        r"what products do you have",  # Match product inquiry
        ["We have a wide range of products including electronics, fashion, books, and home appliances. What are you interested in?",],
    ],
    [
        r"i am looking for (.*)",  # Match product search
        ["I have found some options in our %1 category. Would you like to know more about them?",],
    ],
    [
        r"order status (.*)",  # Match order status inquiry
        ["I can help you with that. Please provide your order ID, and I'll check the status for you.",],
    ],
    [
        r"i want to return my (.*)",  # Match return request
        ["I'm sorry to hear that. Please provide your order number and the reason for the return, and I will assist you.",],
    ],
    [
        r"how can i contact customer service",  # Match customer service inquiry
        ["You can contact our customer service at support@store.com or call us at 123-456-7890. How else can I assist you?",],
    ],
    [
        r"thanks|thank you",  # Match gratitude
        ["You're welcome! Let me know if you need anything else.", "Happy to help! If you need further assistance, feel free to ask."],
    ],
    [
        r"quit",  # Match quit request
        ["Thank you for visiting! Have a great day! :) Bye!", "It was nice talking to you. Take care and see you soon! :)"],
    ],
    [
        r"(.*)",  # Default response for any other input
        ["I'm sorry, I didn't quite catch that. Could you please ask something else?",],
    ],
]

# Define the chatbot function
def chatbot():
    print("Welcome to the E-commerce Store! How can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

# Main entry point
if __name__ == "__main__":
    chatbot()
