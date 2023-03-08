import random

names = ['Any', 'Alex', 'Ivan', 'Peter', 'Steve', 'Jane']
places = ['Sofia', 'Plovdiv', 'Varna', 'Burgas']
verbs = ['eats', 'holds', 'sees', 'plays with', 'brings']
nouns = ['stones', 'cake', 'apple', 'laptop', 'bikes']
adverbs = ['slowly', 'diligently', 'warmly', 'sadly', 'rapidly']
details = ['near the river', 'at home', 'in the park']


def get_random_word(words):
    return random.choice(words)


print('Hello, this is your first random sentence:')

while True:
    random_name = get_random_word(names)
    random_places = get_random_word(places)
    random_verbs = get_random_word(verbs)
    random_nouns = get_random_word(nouns)
    random_adverbs = get_random_word(adverbs)
    random_details = get_random_word(details)

    print(f'{random_name} from {random_places} {random_adverbs} {random_verbs} {random_nouns}')
    input('Click [Enter] to generate a new one.')



