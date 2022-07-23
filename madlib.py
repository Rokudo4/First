# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____ "
# youtuber = "Kylie Ying" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")
name= input("name: ")
adj= input('adj: ')
things= input('things: ')
def madlib1():
    return('hello '+ name)

#print('hello {}'.format(name))
print(f'hello {name} you\'re very {adj}. hope you get {things}')