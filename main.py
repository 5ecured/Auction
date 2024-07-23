import os

print('Welcome to the secret auction program.')

dict = {}

keep_going = True

while keep_going:
    user_name = input('What is your name?:\n')
    user_bid = int(input('What is your bid?:\n$'))

    dict[user_name] = user_bid

    should_continue = input('Are there any other bidders? Type "yes" or "no":\n')
    os.system('clear')

    if should_continue == 'no':
        keep_going = False

highest_bid = 0
winner = ''

for bidder in dict:
    if dict[bidder] > highest_bid:
        highest_bid = dict[bidder]
        winner = bidder

os.system('clear')
print(dict)
print(f'The winner is {winner} with bid of {highest_bid}')