#!/usr/bin/env python2

def recursive_folding(placement, i, j, str, best_so_far, best_contacts):
    # If the length of the string is 0, we have placed all the elements,
    # so we can calculate the number of contacts.  Otherwise, place the
    # the next element in an adjacent space and make another recursive
    # call.  The recursive call will be made placing the next element
    # in each of the (non-diagonal) adjacent spaces.
    if (len(str) == 0):
        num_contacts = 0
 
        # For each element in the current placement, we need to check 
        # how many contacts there are between the H elements.  Thus, we
        # can skip any P elements.
        for element in placement:
            if element[0] == 'P':
                continue
            x = element[1]
            y = element[2]

            adj_ij = [(x + 1, y), 
                      (x, y + 1), 
                      (x - 1, y), 
                      (x, y - 1)]

            # The number of contacts is equal to the number of H 
            # elements adjacent to the current H element.
            num_contacts += len([x for x in placement if x[0] == 'H' and 
                                 (x[1], x[2]) in adj_ij])

        # The above for loop will double count the number of contacts,
        # so the true number of contacts is half what we calculated.
        num_contacts = num_contacts / 2

        # Save the current placement and number of contacts if the
        # current number of contacts is greater than the best so far.
        if num_contacts > best_contacts:
            best_so_far = placement
            best_contacts = num_contacts
        return (best_so_far, best_contacts)
    else:
        # If placement contains elements, cur_ij is the currently
        # occupied spaces.  Then for each space (x,y) adjacent to the
        # (i,j) passed into the function, if (x,y) is not already 
        # occupied, append the next element in the string to the 
        # list placement.  Then make a recursive call with the appended
        # list, x, y, the tail of the string, and the passed-in
    # best_so_far and best_contacts.
        if placement:
            cur_ij = [(x[1], x[2]) for x in placement]
        else:
            cur_ij = []
        for x,y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:    
            if not (x, y) in cur_ij: 
                cur_placement = list(placement)
                cur_placement.append((str[0], x, y))
                (best_so_far, best_contacts) = recursive_folding(cur_placement, 
                                                                 x, y, str[1:],
                                                                 best_so_far, 
                                                                 best_contacts)
        return (best_so_far, best_contacts)


def print_placement(placement):
    output = ''
    min_i = min([x[1] for x in placement])
    max_i = max([x[1] for x in placement])
    min_j = min([x[2] for x in placement])
    max_j = max([x[2] for x in placement])
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            element = [x[0] for x in placement if x[1] == i and x[2] == j]
            if element:
                output += element[0]
            else:
                output += ' '
        output += '\n'
    print(output)


def main():
    string = 'HHPPHHHPHHPH'

    placement = []

    best_so_far = []
    best_contacts = 0

    i = j = 0

    (best_so_far, best_contacts) = recursive_folding(placement, 
                                                     i, j, string, 
                                                     best_so_far, 
                                                     best_contacts)

    print('Optimal number of contacts:')
    print(best_contacts)
    print('Optimal layout:')
    print_placement(best_so_far)


if __name__ == "__main__":
    main()