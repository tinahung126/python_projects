"""
File: boggle.py
Name: Tina Hung
----------------------------------------
This program recursively finds all the possible word in the input 16 letters
and terminates when the function runs through entire 16 letters.
"""
import time
# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary = {} 			# The dict to store the dictionary's data
check_words_lst = {}		# The dict to store the words that have been check and exist in the dictionary
not_exist_lst = {}			# The dict to store the words that have been check and does not exist in the dictionary


def main():
	"""
	This function requires the user to enter 16 letters and process these letters into list data,
	and then start looking for possible combinations of words.
	"""
	read_dictionary()
	all_row = []
	# Build the 4 rows letters
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		row_lst = row.lower().split()
		if len(''.join(row_lst)) != 4:
			print("illegal: Only allow 4 letters!")
			break
		else:
			if not ''.join(row_lst).isalpha():
				print("Illegal: Can't enter any digit!")
				break
			else:
				all_row.append(row_lst)
	start = time.time()
	if len(all_row) == 4:
		words_set = [] 	# To store the words that match successfully
		for x in range(4):
			for y in range(4):
				# Go through all letters(4*4)
				word = []
				place = []
				# Start checking for words starting with each letter
				word.append(all_row[x][y])
				place.append((x, y))
				find_next_words(x, y, word, all_row, place, words_set)
		end = time.time()
		print(f'There are {len(words_set)} words in total')
		print("total執行時間：%f 秒" % (end - start))


def find_next_words(x, y, word_list, all_row, place_list, words_set):
	"""
	This function connects the words around all_row [x] [y] and tries to find
	the complete word that matches the dictionary until it traverses the entire 16 letters.
	:param x: the index of all_row
	:param y: the index of all_row[x]
	:param word_list: the list to store letters
	:param all_row: the list of input 16 letters
	:param place_list: the list to store the index of x,y that have been checked
	:param words_set: the words found in the dictionary
	"""
	# To check the 9 place around that letter
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			# To avoid the range over the index
			if 0 <= x + i <= 3:
				if 0 <= y + j <= 3:
					# Not to count itself
					if not (i == 0 and j == 0):
						# Make sure not to choose the same word
						if ((x + i), (y + j)) not in place_list:
							# When the length of word_list> 1, check whether word_list exists in the dictionary
							if len(word_list) >= 2:
								if has_prefix(word_list) is False:
									break
							# Choose
							place_list.append(((x + i), (y + j)))
							word_list.append(all_row[x + i][y + j])
							# When the length of word > 4, check the dictionary, and continue to run
							if len(word_list) >= 4:
								if ''.join(word_list) in words_set:
									pass
								else:
									if ''.join(word_list) in dictionary:
										words_set.append(''.join(word_list))
										print(''.join(word_list))
							# Explore
							find_next_words(x + i, y + j, word_list, all_row, place_list, words_set)
							# Un-choose
							word_list.pop()
							place_list.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for line in f:
			if 4 <= len(line.strip()) <= 16:
				dictionary[line.strip()] = line[0]


def has_prefix(sub_s):
	"""
	This function checks whether sub_s is in check_words_lst or not_exist_lst,
	and if it does not exist in both lists, it looks up the word in the dictionary.

	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global check_words_lst
	global not_exist_lst
	# Turn list into string
	check_word = ''.join(sub_s)
	if check_word in check_words_lst:
		return True
	if check_word in not_exist_lst:
		return False
	for key, value in dictionary.items():
		# If there is a word start with check_word, return true
		if key.startswith(check_word):
			check_words_lst[check_word] = sub_s[0]
			return True
	not_exist_lst[check_word] = sub_s[0]
	return False


if __name__ == '__main__':
	main()
