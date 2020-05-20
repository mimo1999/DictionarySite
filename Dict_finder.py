# Import the modules required 
import json 
from difflib import get_close_matches 
  
# Loading data from json file 
# in python dictionary 
data = json.load(open("C:/Users/KIIT/Desktop/dictionary.json")) 
  
def translate(w): 
    # converts to lower case 
    w = w.lower() 
  
    if w in data: 
        return data[w] 
    # for getting close matches of word 
    elif len(get_close_matches(w, data.keys())) > 0:              
        yn = yn.lower()  
        return data[get_close_matches(w, data.keys())[0]] 
    else: 
        return "The word doesn't exist. Please double check it."
  
# Driver code 
word = input("Enter word: ") 
output = translate(word) 

print(output)
#if type(output) == list: 
#    for item in output: 
#        print(item) 
#else: 
#    print(output) 
input('Press ENTER to exit')  