from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
chatbot = ChatBot("Jarvis")


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

str = "Hi baby"
response = chatbot.get_response(str)
print(response)
