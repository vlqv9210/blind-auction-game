from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the auction program")
auction_list = {}
players_left = True

def new_player(name,price):
  auction_list["Name"] = name
  auction_list["Price"] = price
  print(auction_list)
  
def highest_guess():
  highest_price=0
  for people in auction_list:
    price = auction_list[people]
    if price > highest_price:
      highest_price = price
      winner = people
  print(f"The winner is {winner}")  

while players_left:
  name = input("What is your name? ")
  price = int(input("What is your bid? $"))
  auction_list[name] = price
  ask = input("Is there another player?")
  clear()
  if ask =="no":
    players_left = False
    highest_guess()
