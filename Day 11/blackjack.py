############### Blackjack Project #####################
import random as rd
from art import logo
import os

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
user=[]
dealer=[]

def deal_start():
  user.append(draw_card())
  dealer.append(draw_card())
  user.append(draw_card())
  dealer.append(draw_card())


def draw_card():
  return rd.choice(cards)
  

def black_jack():
  os.system('cls')
  user.clear()
  dealer.clear()
  print(logo)
  deal_start()
  user_score= user_turn(sum(user))
  dealer_score=sum(dealer)
  user_win=False
  draw=False
  if user_score>21: 
    user_win=False
  else:
    dealer_score= computer_turn(dealer_score, user_score)
    if dealer_score>21:
      user_win=True
    elif dealer_score==user_score and dealer_score!=21:
      draw=True
    elif user_score>dealer_score:
      user_win=True
      

  

  print(f"Your final hand, {user}, and your final_score= {user_score} ")
  print(f"Dealer's final hand, {dealer}, and dealer's final_score={dealer_score} ")

  if user_win:
    if dealer_score>21:
      print("Dealer is bursted")
    if user_score==21:
      print('BlackJack')        
    print('You win 😎')
  elif draw:
    print('Draw')
  else:
    if user_score>21:
      print("You are bursted")
    if dealer_score==21:
      print("Dealer has BlackJack")     
    print('You lost 😭')

  play_again=input('Do you wanna play another game of blackjack, y or n? ')

  if play_again.lower()=='y':
    black_jack()
  return


  

  
    
  


def computer_turn(sum, user_score):
  if sum>=21 or sum>user_score:
    return sum
  if sum>17:
    return sum

  drawn_card=draw_card()
  dealer.append(drawn_card)
  sum+=drawn_card

  if sum>21:
    if drawn_card==11:
      dealer[-1]=1
    else:
      for card in dealer:
        if card==11:
          card=1
          sum-=10
          break
  if(sum<17):
    return computer_turn(sum, user_score)

  return sum
      
    
  
  
  
  
    


  
def user_turn(sum):
  if sum>=21:
    return sum
  
  print(f" computer's current cards are [{dealer[0]}, X ]")
  print(""" your current cards are: {}, your current score={}  """.format(user,sum))

  choice=input('press "y" for hitting with another. ')
  if choice.lower()!='y':
    return sum
    
  drawn_card=draw_card()
  user.append(drawn_card)
  if drawn_card==11 and sum>10:
    drawn_card=1
      
  sum+=drawn_card
  if(sum>21):
    for card in user:
      if card==11:
        card=1
        sum-=10
        break
  return user_turn(sum)


black_jack()

 
 
        
  
    
  
