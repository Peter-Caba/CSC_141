import random  

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']


my_ticket = [3, 6, 'A', 9]

attempts = 0
winning_ticket = []


while winning_ticket != my_ticket:
  
    winning_ticket = random.sample(lottery_pool, 4)
    
  
    attempts += 1

print(f"It took {attempts} attempts to match the winning ticket: {my_ticket}")
