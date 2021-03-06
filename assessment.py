"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_list = phrase.split()
    word_dict = {}
    for word in word_list:
    #     if word not in word_list:
    #         word_dict[word] = 0
    #     else:
    #         word_dict[word] += 1
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_price_dict = {
        "Watermelon": 2.95,
        "Cantaloupe": 2.50,
        "Musk": 3.25,
        "Christmas": 14.25,
    }

    if melon_name in melon_price_dict.keys():
        return melon_price_dict.get(melon_name)
    else:
        return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    word_length_dict = {}
    for word in words:
        word_length = len(word)
        if word_length not in word_length_dict:
            word_length_dict[word_length] = [word]
        else:
            word_length_dict[word_length].append(word)
    word_length_list = []
    for word_length, words in word_length_dict.items():
        words = sorted(words)
        word_length_list.append((word_length, words))
    # for entry in word_length_list:
    #     print sorted(entry[1])
    return sorted(word_length_list)


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    pirate_to_english_dict = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "man": "matey",
        "professor": "foul blaggert",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": 'be',
    }

    english_word_list = phrase.split()
    pirate_word_list = []
    for english_word in english_word_list:
        if english_word in pirate_to_english_dict:
            pirate_word_list.append(pirate_to_english_dict[english_word])
        else:
            pirate_word_list.append(english_word)
    return " ".join(pirate_word_list)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    # placeholder_names_list = []
    # names_list.append(names[0])
    # del names[0]
    # return names

    # results[names[0]] = (list(names[0][-1]))
    # del names[0]

    # names_list_length = len(names)

    # if names_list_length % 2 == 0:
    #     n = 1
    # else:
    #     n = 2

    # return list(names[0])[-1]
    # results_list = [names[0]]
    # del names[0]
    # index = 0
    # # results_dict = {}
    # for result_name in results_list:
    #     # name_letters = list(name)
    #     index = 0
    #     for name in names:
    #         if result_name[-1] == name[0]:
    #             # results_dict[result_name] = name
    #             results_list.append(name)
    #             del name
    #             break
    #         else:
    #             index += 1
    #     index += 1
    # return results_list


    # index = 1
    # return results_dict.values()
    # return letters_list[-2]
#     for index in range(len(results_dict.values())-1):
#         if results_dict.values()[0][1] == results_dict.values()[index][0]:
#             # names_list = results_dict.keys()
#             results_list.append(results_dict.keys()[index])
#             del results_dict.keys()[index]
#         # return results_dict[index+1][0]
#         else:
#             index += 1
#     return results_list
# print kids_game(["bagon", "baltoy", "yamask", "starly", "nosepass", "kalob", "nicky", "booger"])
    

    # index = 0
    # results_list = []
    # results_tuples = results_dict.items()
    # for name, letters in results_tuples:
    #     results_list.append(name)
    #     del results_dict[name]
    #     last_letter = letters[1]
    #     first_letter_next_name = results_tuples[index+1][1][0]
    #     return results_tuples.values()[1]
        # while last_letter !=
        #     index += 1
        #     current_name = results_tuples[index][0]
        # first_letter = name
        # if last_letter ==
        # while :
        #     first_letter = name_letters[0]
        #     if last_letter = first


#####################################################################
# You can ignore everything below this.


def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
