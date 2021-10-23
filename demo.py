from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
bot = ChatBot('Ron Obvious')

#trainer 1
trainer = ListTrainer(bot)

# Create a new trainer for the chatbot
trainer2 = ChatterBotCorpusTrainer(bot)

# Train the chatbot based on the english corpus
trainer2.train("chatterbot.corpus.english")

# Get a response to an input statement
print(bot.get_response("Hello, how are you today?"))

trainer.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])
######### form demo2
trainer.train([
    "I did not do much this week",
    "Did you run into the problems with programs or just did not have time?"
])
 
 
trainer.train([
    "I did a lot of progress",
    "Fantastic! Keep going on"
]) 
 
 
trainer.train([
    'Good morning!',
    'Good morning!',
    'How are you today?',
    'I am fine',
    'Do you like machine learning?',
    'Yes, I like machine learning'
])
  
  
trainer.train([
    'Good morning!',
    'Good morning!'
   
])
  
trainer.train([
    'Hello',
    'Hi there!'
   
])
  
  
trainer.train([
    'Let us talk about current activities',
    'What are you working on now?',
    'I am just browsing Internet for news',
    'What a waste of time! Dont you have any other things to do?',
    'I am working on python script to make new chatbot',
    'This is great. Keep working on this'
])
  
  
trainer.train(
    "chatterbot.corpus.english.greetings"
   
)
  
trainer.train(
   "chatterbot.corpus.english.conversations"
)
  
  
  
#from chatterbot.trainers import ListTrainer
  
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
  
#chatbot.set_trainer(ListTrainer)
trainer.train(conversation)
  
########################################
###  END of  TRAINING
########################################
  
  
  
print ("USER: How are you doing?")
  
response = bot.get_response("How are you doing?")
print("BOT:" + str(response))
print ("USER: Hello")

response = bot.get_response("Hello")
print("BOT:" + str(response))
print ("USER: Good morning!")
  
response = bot.get_response("Good morning!")
print("BOT:" + str(response))
  
  
  
print ("USER: Do you like machine learning?")
  
response = bot.get_response("Do you like machine learning?")
print ("BOT:" + str(response))
print ("USER: How do I make a neural network?")
  
response = bot.get_response('How do I make a neural network?')
print("BOT" + str(response))
print ("USER: Let us talk about current activities")
  
response = bot.get_response("Let us talk about current activities")
print("BOT:"+str(response))
  
print ("USER: I am just browsing Internet")
  
response = bot.get_response("I am just browsing Internet")
print("BOT:" + str(response))
  
print ("USER: I am working on python script to make new bot")
  
response = bot.get_response("I am working on python script to make new bot")
print("BOT:"+str(response))
  
  
print ("USER: Bye")
  
response = bot.get_response("Bye")
print("BOT:" + str(response))

#########




# Get a response for some unexpected input
response = bot.get_response('How do I make an omelette?')
print(response)