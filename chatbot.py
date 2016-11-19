#Chatbot 
from random import randint,choice 
import time

def replies(user_input):
	questions = ["how are you?","What are you doing","ssup","supp"]
	greetings = ["hello","hey","hi","heyaa"]
	jokes = ["tell me some jokes","make me laugh","tell me a joke"]
	print("User: " + user_input)
	
	asked = user_input.lower()
	response = "I didn't get it"
	if asked in questions:
		response = [" I 'm fine , Thank you "," Nothing much "," Doing good ",
					" poking around" , "what about you"]
	if asked in greetings:
		response = [" hello"," hey"," hi"," heyaa"]
	if asked in jokes:
		response = [" Ques:    Why shouldn ' t you interupt a talking judge ??" + "\n" + 
		 			 "Answer:    KyuKi uske judge-baat hurt ho jate hai XD XD "]

	time.sleep(1)
	print("Comp: " + choice(response) + "\n")
	time.sleep(1)


while True:
	tests = ["how are you?","What are you doing","ssup","supp","hello","hey","hi","heyaa" 
				"tell me some jokes","make me laugh","tell me a joke"]
	replies(tests[randint(0 , len(tests) - 1)] )
	