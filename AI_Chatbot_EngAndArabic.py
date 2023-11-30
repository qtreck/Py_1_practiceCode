from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('SnapchatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

#Train the chatbot on Arabic language data
trainer.train('chatterbot.corpus.arabic')

# You can add more training data or customize the training process as needed

# Start the chatbot interaction
print("Hello! I'm your SnapchatBot. Ask me anything.")

while True:
    user_input = input("You: ")
    
    # Exit the loop if the user says 'bye'
    if user_input.lower() == 'bye':
        print("SnapchatBot: Goodbye! Have a great day.")
        break
    
    # Get the chatbot's response
    response = chatbot.get_response(user_input)
    
    print("SnapchatBot:", response)
