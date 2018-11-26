"""
This is a script that plays Hangman.

It plays Hangman using mostly 2 letter words.
Some of the two letter words are two letters long.
Some are not.
There are also some 20+ letter words sprinkled in, for variety.
A few single letter words, as well.
One of the single letter words is 20+ letters long.

Users can type y (or yes) to play, or n (or no) to exit.

During the course of the game, they can only guess letters.

They cannot exit a game until they have correctly guessed all the letters.
"""

import random
import re

def letter_revealer(string, letters):
    """
    Takes in a string and returns a string of the same length,
    containing dashes and letters. Any letter in both the
    original string and revealed_letters is also present in
    the return string. Any letter NOT in both the original
    string and revealed_letters is 'hidden' in the return string,
    with a dash.
    """
    return_string = ''

    if not letters:
        return_string = '-' * len(string)
    else:
        for letter in string:
            if letter in letters:
                return_string += letter
            else:
                return_string += '-'

    return return_string

GAME_WORDS = ['supercalifragilisticexpialidocious',
              'at',
              'an',
              'as',
              'ab',
              'deinstitutionalization',
              'ow',
              'ah',
              'it',
              'in',
              'counterrevolutionaries',
              'eh',
              'is',
              'oh',
              'ha',
              'no',
              'if',
              'we',
              'ye',
              'ya',
              'yo',
              'oy',
              'ka',
              'qi',
              'so',
              'up',
              'ut',
              'hi',
              'ok',
              'lo',
              'or',
              'os',
              'mi',
              'to',
              'ti',
              'ra',
              're',
              'a',
              'i',
              'o',
              'pi',
              'pa',
              'pe',
              'jo',
              'ax',
              'ox',
              'ab',
              'antidisestablishmentarianism',
              'bi',
              'be',
              'bo',
              'ho'
              'he',
              'ma',
              'me',
              'am',
              'um',
              'hm',
              'my',
              'by',
              'hmmmmmmmmm',
              'ummmmmmmmm',
              'grrrrrrrrr',
              'prrrrrrrrr',
              'ahhhhhhhhh',
              'ohhhhhhhhh',
              'aaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
              'electroencephalograph',
              'floccinaucinihilipilification',
              'qwertyuiopasdfghjklzxcvbnm',
              'abcdefghijklmnopqrstuvwxyz'
              'uncharacterically',
              'internationalization',
              'pneumonoultramicroscopicsilicovolcanoconiosis'
              ]

AFFIRMATIVE_RESPONSE = re.compile('^y$|^(yes)$', re.IGNORECASE)
NEGATIVE_RESPONSE = re.compile('^n$|^(no)$', re.IGNORECASE)
LETTER_IN_ALPHABET = re.compile('^[a-z]$', re.IGNORECASE)

print('Welcome to Hangman! Do you want to play a game?)\n')

while True:
    print('Y/n')

    RESPONSE = input()
    MATCHED = AFFIRMATIVE_RESPONSE.match(RESPONSE) or NEGATIVE_RESPONSE.match(RESPONSE)

    if not MATCHED:
        continue
    else:
        if NEGATIVE_RESPONSE.match(RESPONSE):
            print('Good-bye!')
            break

    RANDOM_INDEX = random.randint(0, len(GAME_WORDS) - 1)
    RANDOM_WORD = GAME_WORDS[RANDOM_INDEX]
    GUESSED_LETTERS = []
    DISPLAYED_LETTERS = letter_revealer(RANDOM_WORD, GUESSED_LETTERS)

    while DISPLAYED_LETTERS != RANDOM_WORD:
        print('\nWORD: ' + DISPLAYED_LETTERS + '\n')
        print('Guess a letter!\n')

        RESPONSE = input().lower()
        MATCHED = LETTER_IN_ALPHABET.match(RESPONSE)

        if not MATCHED:
            continue
        else:
            CASE_INSENSITIVE_RESPONSE = RESPONSE.lower()

            if CASE_INSENSITIVE_RESPONSE in GUESSED_LETTERS:
                print('You already guessed that letter!')
                continue
            else:
                GUESSED_LETTERS.append(CASE_INSENSITIVE_RESPONSE)

                if CASE_INSENSITIVE_RESPONSE not in RANDOM_WORD:
                    print('That letter is not in here...')
                    continue
                else:
                    print('Cool!')
                    DISPLAYED_LETTERS = letter_revealer(RANDOM_WORD, GUESSED_LETTERS)
                    continue

    print('\n' + DISPLAYED_LETTERS + '\n')
    print('You win! Another game?\n')

    continue
