import nltk
from nltk.chat.util import Chat, reflections 

pairs = [
    [
        r"my name is  (.*)",
        ["Hello %1, how can i help you?",]
    ],
    [
        r"hi|hey|wsp",
        ["hello!", "hey there!",]
    ],
    [
        r"what is your name freind?",
        ["I am your freindly chatbot.",]
    ],
    [
        r"how are you?",
        ["Im just a bunch of code, but thanks for asking!"]
    ],
    [
        r"Quit",
        ["Goodbye have a good day"]
    ],
]

chatbot = Chat(pairs, reflections)

# Function to interact with the chatbot
def chat():
    print("Hello, i am your chatbot. How can i assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye! Have a nice day!")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print("Chatbot: ", response)
            else:
                print("Chatbot: Im not sure how to respond to that.")
chat()