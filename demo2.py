from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
  
chatbot = ChatBot("mybot",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'prev_day_disk',
            'output_text': 'How much did you do toward your goal on previous day?'
        },
        # {
        #     "import_path": "chatterbot.logic.BestMatch",
        #     "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
        #     "response_selection_method": "chatterbot.response_selection.get_first_response"
        # },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ])
    # ,
    # trainer='chatterbot.trainers.ListTrainer')
trainer = ListTrainer(chatbot)  
  
########################################
###   TRAINING - run this just one time
########################################
  
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
  
response = chatbot.generate_response("How are you doing?")
print("BOT:" + (response))
print ("USER: Hello")
  
response = chatbot.get_response("Hello")
print("BOT:" + str(response))
print ("USER: Good morning!")
  
response = chatbot.get_response("Good morning!")
print("BOT:" + str(response))
  
  
  
print ("USER: Do you like machine learning?")
  
response = chatbot.get_response("Do you like machine learning?")
print ("BOT:" + str(response))
print ("USER: How do I make a neural network?")
  
response = chatbot.get_response('How do I make a neural network?')
print("BOT" + str(response))
print ("USER: Let us talk about current activities")
  
response = chatbot.get_response("Let us talk about current activities")
print("BOT:"+str(response))
  
print ("USER: I am just browsing Internet for news")
  
response = chatbot.get_response("BOT: I am just browsing Internet for news")
print("BOT:" + str(response))
  
print ("USER: I am working on python script to make new chatbot")
  
response = chatbot.get_response("I am working on python script to make new chatbot")
print("BOT:"+str(response))
  
  
print ("USER: Bye")
  
response = chatbot.get_response("Bye")
print("BOT:" + str(response))