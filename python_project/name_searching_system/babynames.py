"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This file puts the original text document into the
data dictionary according to the year, name and rank data.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given y ear and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    # When the name already exists in the name_data
    if name in name_data:
        # If there has year data already, replace with a higher rank data.
        if year in name_data[name]:
            if int(name_data[name][year]) > int(rank):
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank
    # When the name doesn't exist in the name_data, create the new key and value.
    else:
        name_data[name] = {}
        name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r')as f:

        for line in f:
            names = line.split(',')     # list of rank, boy name, girl name
            # The first line of each file only has the year data, so save the number as name_data's year value.
            if len(names) == 1:
                year = line.strip()
            else:
                rank = names[0].strip()
                for i in range(1, 3):
                    add_data_for_name(name_data, year, rank, names[i].strip())


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)

    return name_data


def find_exact_match_name(name_data, target):
    """
    To find the exact match name of the input name in the name_data, and returns a list of the name that matches
    the target name.

    :param name_data: a dict containing baby name data organized by name
    :param target:  a string to look for in the name_data
    :return:  a list of a name from name_data that match the target string
    """
    name = []
    if target in name_data:
        name.append(target)
    return name


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    names = []
    for key in name_data:
        same_word = 0   # To count the number of the same words.
        j = 0   # The number to control the target string index.
        for i in range(0, len(key)):
            if key[i].lower() == target[j].lower():
                same_word += 1
                if j == len(target)-1:
                    names.append(key)
                else:
                    # Check the next letter of the target
                    j += 1
            # If key[i] != target[j]
            else:
                if same_word > 0:
                    # Means it must check the next letter of the key with the first letter of the target string.
                    j = 0
                    same_word = 0
    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
