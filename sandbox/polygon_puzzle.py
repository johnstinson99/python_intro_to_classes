
import random
my_list = ['a', 'b', 'c']
choice = random.choice(my_list)
print(choice)
random.shuffle(my_list)
print(my_list)

mandatory_letter = 'm'
optional_letters = 'irsoemfr'

# method one, find all permutations.
# method two - check each word
new_word = 'amam'.replace('m', '', 1)
print(new_word)

print(all([True, True, True]))
print(any([True, False, False]))

sentence = 'the quick brown fox jumped over the lazy dog'
word_list = sentence.split(' ')
print(word_list)
word_list.sort()
print(word_list)
print(' '.join(word_list))

sentence = 'the quick brown fox jumped over the lazy dog'
word_list = sentence.split(' ')
new_list = list(enumerate(word_list))
print(new_list)

word_pairs = [word_list[i: i+2] for i in range(0, len(word_list) - 2 + 1)]
print(word_pairs)


def get_the_answer(is_numeric=False):
    """returns the answer to the ultimate question of life, the universe and everything
    :param is_numeric: returns number if True, string if False
    """
    if(is_numeric):
        return 42
    else:
        return "Forty-two"

print(get_the_answer(is_numeric=True))
help(get_the_answer)

list_letters = ['a', 'b', 'c']
list_numbers = [1, 2, 3]
zipped_list = list(zip(list_numbers, list_letters))
print(zipped_list)

zipped_list = [(1, 'a'), (2, 'b'), (3, 'c')]
lista, listb = zip(*zipped_list)
print(lista, listb)


phone_no_dict = {'bill': '1234',
                 'fred': '9876',
                 'jane': '9912',
                 'alice': '6583'}
print(phone_no_dict['fred'])
phone_no_dict['fred'] = '1111'
print(phone_no_dict['fred'])
phone_no_dict['emergency'] = '999'
print(phone_no_dict)