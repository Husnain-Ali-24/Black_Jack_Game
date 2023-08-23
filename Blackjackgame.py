import random
Input=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
condition=True
while condition==True:
 if Input=="y":
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  your_current_score=0
  computer_current_score=0
  your_final_score=0
  final_score=0
  your_card=[]
  computer_card=[]
  for i in range(2):
   a=random.choice(cards)
   b=random.choice(cards)
   your_card.append(a)
   computer_card.append(b)
  print(f"Your Cards: {your_card}")
  print(f"Computer's first Card: {computer_card[0]}")
  if your_current_score==21:
    print("You Win!")
    a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if a=="y":
       condition=True
    else:
       condition=False
  else:
       Input_1=input("Type 'y' to get another card, type 'n' to pass: ")
       if Input_1=="n":
        print(f"Your Final Hand: {your_card}")
        print(f"Computer's Final Hand: {computer_card}")
        a=sum(your_card)
        add_computer_card=computer_card.copy()
        add_computer_card.append(random.choice(cards))
        b=sum(add_computer_card)
        if b<17:
         sum=0
         for i in add_computer_card:
          sum+=i
         if sum>17 and sum<21:
          pass
         elif sum<17:
          add_computer_card_1=add_computer_card.copy()
          add_computer_card_1.append(random.choice(cards))
          sum1=0
          for j in add_computer_card_1:
           sum1+=j
          if sum1>21:
           print("You win")
           a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
           if a=="y":
            condition=True
           else:
            condition=False
         elif sum>21:
          print("You win!")
          a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
          if a=="y":
            condition=True
          else:
            condition=False
         elif sum<sum(your_card):
          print("You Win")
          a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
          if a=="y":
            condition=True
          else:
            condition=False
        else:
         if a>b:
          print("You Win!")
         elif a>21:
          print("You Loss!")
         elif a==b:
          print("Both Are Equal So,Fall!")
         else:
          print("You Loss!")
         a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
         if a=="y":
          condition=True
         else:
          condition=False
       elif Input=="y":
        d=random.choice(cards)
        for i in your_card:
         your_current_score+=i
        for j in computer_card:
         computer_current_score+=j
        e=your_card.copy()
        e.append(d)
        print(f"Your Cards: {your_card}, current score: {your_current_score}")
        print(f"Computer's first card:{computer_card[0]}")
        for i in e:
         your_final_score+=i
        print(f"Your Final hand: {e}, final score:{your_final_score}")
        print(f"Computer Final hand: {computer_card}, final score:{computer_current_score}")
        if your_final_score>21:
         print("You Loss!")
         a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
         if a=="y":
             condition=True
         else:
             condition=False
        else:
         x=sum(e)
         y=sum(computer_card)
         if x>y:
          print("You win!")
          a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
          if a=="y":
             condition=True
          else:
             condition=False
         elif x>21:
          print("You Loss")
          a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
          if a=="y":
             condition=True
          else:
             condition=False
         elif y>21:
          print("You Win!")
          a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
          if a=="y":
             condition=True
          else:
             condition=False
         elif x==y:
          print("Draw!")
          a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
          if a=="y":
             condition=True
          else:
             condition=False
         elif x<y:
          print("You Loss")
          a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
          if a=="y":
             condition=True
          else:
             condition=False
 else:
  print("Ok! Good Byeee!")
  condition=False