#!/usr/bin/python3
"""
finds peak in a list of unsorted ints
"""

def find_peak(list_of_integers):
    """
    finding peak
    """
    length_of_list = len(list_of_integers)
    if length_of_list == 0:
        return
    mid_of_list = length_of_list//2
    if (mid_of_list == length_of_list - 1 or list_of_integers[mid_of_list] >=
        list_of_integers[mid_of_list + 1]) and (mid_of_list == 0 or list_of_integers[mid_of_list] >=
                                         list_of_integers[mid_of_list - 1]):
        return (list_of_integers[mid_of_list])
    elif mid_of_list != length_of_list - 1 and list_of_integers[mid_of_list + 1] > list_of_integers[mid_of_list]:
        return (find_peak(list_of_integers[mid_of_list + 1:]))
    return (find_peak(list_of_integers[:mid_of_list]))
