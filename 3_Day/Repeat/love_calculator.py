print('Welcome to the Love Calculator!')

your_name = str(input('What is your name?\n').lower())
her_name = str(input('What is their name?\n').lower())


true_count = sum(([your_name.count(letter) + her_name.count(letter) for letter in 'true']))
love_count = sum(([her_name.count(letter) + your_name.count(letter) for letter in 'love']))
# true_count, love_count = [sum(name.count(letter) for letter in word for name in [your_name, her_name]) for word in ['true', 'love']]


love_score = 8

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif 40 <= love_score >= 50:
    print(f'Your score is {love_score} you alright together.')
else:
    print(f'Your score is {love_score}')