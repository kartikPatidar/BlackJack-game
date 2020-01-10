import random

class Balance:

	def __init__(self,balance = 100):
		self.balance = balance

	def plus_balance(self,value):
		self.balance = self.balance + value

	def sub_balance(self,value):
		self.balance = self.balance - value	





def deal_cards():
	
	dealer_card1 = random.randrange(1,14,1)
	dealer_card2 = random.randrange(1,14,1)
	player_card1 = random.randrange(1,14,1)
	player_card2 = random.randrange(1,14,1)

	if(dealer_card1 == 11 or dealer_card1 == 12 or dealer_card1 == 13):
		dealer_card1 = 10
	if(dealer_card2 == 11 or dealer_card2 == 12 or dealer_card2 == 13):
		dealer_card2 = 10
	if(player_card1 == 11 or player_card1 == 12 or player_card1 == 13):
		player_card1 = 10
	if(player_card2 == 11 or player_card2 == 12 or player_card2 == 13):
		player_card2 = 10		

	player_cards.append(player_card1)
	player_cards.append(player_card2)
	dealer_cards.append(dealer_card1)
	dealer_cards.append(dealer_card2)
	#print(dealer_cards)
	#print(player_cards)


def replay():
	return int(input("Do you want to play again(0[No] or 1[Yes]) : "))

def show_cards():
	print(f"Your cards : {player_cards}")
	print(f"Dealers cards : [ ?",end = ' ')
	for x in range(1, len(dealer_cards)) :
		print(f",{dealer_cards[x]}",end = '')
	print("]")	

def show_full():
	print(f"Your cards : {player_cards}")
	print(f"Dealer's cards : {dealer_cards}")
	

def deal_single_card(list_name):
	new_card = random.randrange(1,14,1)

	if(new_card == 11 or new_card == 12 or new_card == 13):
		new_card = 10
	if list_name == 'player':
		player_cards.append(new_card)
	else:
		dealer_cards.append(new_card)

play_again = 1
while  play_again == 1:
	bal = Balance()
	for x in range(1,11):
		if bal.balance == 0:
			print("You don't have any money left.")
			break
		print()
		print("Round -",x)
		print()
		print(f"Your Current Balance is : ${bal.balance}")
		while True:
			while True:
				try:
					player_bet = int(input("Your Bet :"))
				except ValueError:
					print("Please provide a number.")
					continue
				else:
					break

			if player_bet<=bal.balance:
				print("Best of luck ! \ndealing the cards...")
				break
			else:
				print("Bet amount can't exceed your balance")
				continue


		player_cards = []
		dealer_cards = []
		deal_cards()
		win = False
		show_cards()
		while not win:

			choice = int(input("Press '1' to HIT and '2' to STAND : " ))
			if choice == 1:
				print("Dealing card....")
				deal_single_card('player')
				show_cards()
				sump = sum(player_cards)
				if sump > 21:
					print("Player Bust!....Dealer won the round")
					show_full()
					win = True
					bal.sub_balance(player_bet)
					break
			if choice == 2:
				sumd = sum(dealer_cards)
				while sumd < 17:
					print("Dealing card...")
					deal_single_card('dealer')		
					show_cards()
					sumd = sumd + dealer_cards[-1]
				if sumd > 21:
					print("Dealer Bust!....You won the round")
					show_full()
					win = True
					bal.plus_balance(player_bet)
					break
				else:
					if sumd > sump:
						print("Dealer Won the round as his sum is higher!")
						show_full()
						win = True
						bal.sub_balance(player_bet)
						break
					elif sump > sumd:
						print("You Won the round as your sum is higher!")	
						show_full()
						win = True
						bal.plus_balance(player_bet)
						break
					else:
						print("PUSH....No one WON this round!")
						show_full()
						win = True
						break

	print("\n")
	play_again = replay()
	