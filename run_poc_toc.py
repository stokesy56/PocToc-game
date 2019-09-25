# we will need to import our functions
from poc_toc_functions import *
# play the game and while loop here
user_input = int(input('Give me a number').strip())
if div3(user_input) and div5(user_input):
    print('PocToc')
elif div3(user_input):
    print('Poc')
elif div5(user_input):
    print('Toc')
else:
    print(user_input)

