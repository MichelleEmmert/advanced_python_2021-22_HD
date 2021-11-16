#
# The first version of our function!
# Write doc strings 
#
def find_peaks(list_of_intensities):
    """Find peaks

    Find local maxima for a given list of intensities or tuples
    Intensities are defined as local maxima if the
    intensities of the elements in the list before and after
    are smaller than the peak we want to determine.

    For example given a list:
        1 5 [6] 4 1 2 [3] 2

    We expect 6 and 3 to be returned.
    

    Args:
        list_of_intensities (list of floats, ints or tuple of ints): a list of
            numeric values

    Returns:
        list of floats or tuples: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)

    """

    list_of_intensities_updated = []
    for element in list_of_intensities:
        list_of_intensities_updated.append(sum(element))

    maximum_list = []

    for pos,value in enumerate(list_of_intensities_updated):

        if pos == 0:
            post_value = list_of_intensities_updated[pos+1]
            if value > post_value:
                maximum_list.append(value)
        
        if pos == len(list_of_intensities_updated) - 1:
            pre_value = list_of_intensities_updated[pos-1]
            if pre_value < value:
                maximum_list.append(value)

        if not pos == 0 and not pos == len(list_of_intensities_updated) -1:
            post_value = list_of_intensities_updated[pos+1]
            pre_value = list_of_intensities_updated[pos-1]
            if pre_value < value > post_value:
                maximum_list.append(value)

    return maximum_list
