alien_0 = {'color':  'green', 'points': 5, 'health': 1, 'numbers': 10}
alien_1 = {'color':  'yellow', 'ponits': 10,'health': 2, 'numbers': 3}
alien_2 = {'color':  'red',    'ponits': 15, 'health': 3, 'numbers': 2}

aliens = [alien_0, alien_1, alien_2]

for ailen in aliens:
    print(f"There are {alien['numbers']} {alien['color']} aliens which provide" +
          f"({alien['points']} points and have a health of {alien['health']}.")