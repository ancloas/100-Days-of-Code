from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print('Welcome to the secret auction program')

answer = 'yes'

bids = {}
while answer.lower() == 'yes':
    name = input('What is your name?: ')
    bid = int(input('please make your bid. $'))
    bids[name] = bid
    answer = input('Are there any other bidders? Type "yes" or "no".')
    clear()

selected_name = ''
selected_name = 'name'
for name in bids:
    if selected_name not in bids:
        selected_name = name
    elif bids[name] > bids[selected_name]:
        selected_name = name

print(selected_name + ' has the highest bidding with a bid of $' +
      bids[selected_name])
