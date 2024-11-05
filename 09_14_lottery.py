import random  

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']


winning_ticket = random.sample(lottery_pool, 4)

print(f"The winning ticket numbers/letters are: {winning_ticket}")
print("Any ticket matching these 4 items wins a prize!")
