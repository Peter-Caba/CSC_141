language = [ 'spainsh','japaness', 'russian', 'german']
message = f"welcome to {language[0].title()}"
print(message)

message = f"welcome to {language[1].title()}"
print(message)

message = f"welcome to {language[2].title()}"
print(message)

message = f"welcome to {language[3].title()}"
print(message)

language = [ 'spainsh','japaness', 'russian', 'german']
language.remove('spainsh')
print(language)

language.insert(0, 'spainsh')
language.insert(2, 'german')
language.append('russian')


language = [ 'spainsh','japaness', 'russian', 'german']
popped_language = language.pop
print(popped_language)


language = [ 'spainsh','japaness', 'russian', 'german']
language.sort()
print(language)

language = [ 'spainsh','japaness', 'russian', 'german']
language.reverse()
print(language)

language = [ 'spainsh','japaness', 'russian', 'german']
number_language = len(language)
print(number_language)