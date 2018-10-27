from chatterbot.trainers import ListTrainer
import pandas as pd
from chatterbot import ChatBot
chatbot = ChatBot("Jarvis")
data = pd.read_csv('datafile.csv')

data["key"] = 'price'+ ' '+data["market"].map(str) +' '+ data["commodity"]
lis =  data["key"].tolist()
lis2 = data['modal_price'].tolist()
result = [None]*(len(lis)+len(lis2))
result[::2] = lis
result[1::2] = lis2


chatbot.set_trainer(ListTrainer)
chatbot.train(result)

str = "paddy(dhan) price in Nandikotkur  "
response = chatbot.get_response(str)
print(response)