"""
File: anagram.py
Name:Tina Hung
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dictionary = {}               # The dictionary of dictionary.txt
check_words_lst = []          # To store the words that had been checked in list


def main():
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        word = input('Find anagrams for: ')
        start = time.time()
        # If input is not all English letters, ask user to enter again or -1 to quit.
        if not word.isalpha():
            if str(word) == EXIT:
                break
            else:
                print('Please enter English letters!')
        else:
            read_dictionary(len(word))
            find_anagrams(word)
            # Make the list empty
            check_words_lst.clear()
            end = time.time()
            print("total執行時間：%f 秒" % (end - start))


def read_dictionary(length):
    """
    This function is to construct the dict of dictionary.
    """
    # This function has asked TA.
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            if len(line.strip()) == length:
                dictionary[line.strip()] = line[0]


def find_anagrams(s):
    """
    This function is to rearrange the input word 's', and find the anagrams.
    :param s: The input word needed to find the anagrams
    """
    words_set = []      # Store all the anagrams
    num_lst = []        # Store the index of s
    helper(s, [], len(s), num_lst, words_set)
    print(f'{len(words_set)} anagrams: {words_set}')



def helper(s, new_word, s_len, num_lst, words_set):
    """
    This function is to help the find_anagrams.
    :param s: The input word needed to find the anagrams.
    :param new_word: Store the letters when rearranging the 'S'.
    :param s_len: length of s
    :param num_lst: To store the index of 's'.
    :param words_set: To store all the anagrams
    """
    if len(new_word) == s_len:
        # Reach base case when new-word's length = s_len
        rebuild_word = ''   # Anagram words
        # Turn list into text
        for ch in new_word:
            rebuild_word += ch
        # If the Anagram word already in words_set list, pass the word
        if rebuild_word in words_set:
            pass
        else:
            if rebuild_word in dictionary:
                words_set.append(rebuild_word)
                print('Found:', rebuild_word)
                print('Searching...')
    else:
        for i in range(len(s)):
            # To skip the same index of s
            if i in num_lst:
                pass
            else:
                # When the length of new_word> 1, check whether new_word exists in the dictionary
                if len(new_word) > 1:
                    if has_prefix(new_word) is False:
                        break
                # Choose
                new_word.append(s[i])
                num_lst.append(i)
                # Explore
                helper(s, new_word, s_len, num_lst,words_set)
                # Un-choose
                num_lst.pop()
                new_word.pop()


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s.
    """
    global check_words_lst

    if sub_s in check_words_lst:
        return True
    # Turn list into text
    check_word = ''
    for ch in sub_s:
        check_word += ch
    for key, value in dictionary.items():
        # If there is a word start with check_word, return true
        if key.startswith(check_word):
            check_words_lst.append(sub_s)
            return True
    print('false')
    return False


if __name__ == '__main__':
    main()
