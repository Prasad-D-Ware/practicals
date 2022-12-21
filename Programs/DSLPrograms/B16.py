#GROUP B - 16. Write a python program to store first year percentage of students in array. 
#Write function for sorting array of floating point numbers in ascending order using quick 
#sort and display top five scores.

import array as arr


# Accept the % marks of the students

def accept_perc():
    a = arr.array('f', [])
    no_stud = int(input("Enter the number of Students : "))
    for i in range(0, no_stud):
        a.append(float(input("Enter the First Year % of Student[{0}] : ".format(i))))
    return a


# Print the % marks of the Students

def print_perc(a):
    for i in range(0, len(a)):
        print("\t {0:.2f}".format(a[i]), end=" ")
    print()


# Quick Sort Partition function

def partition(a, start, end):
    pivot = a[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            a[low], a[high] = a[high], a[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    a[start], a[high] = a[high], a[start]

    return high


# Quick Sort function

def quick_sort(a, start, end):
    if start >= end:
        return

    p = partition(a, start, end)
    quick_sort(a, start, p - 1)
    quick_sort(a, p + 1, end)
    return a


# Top 5 Score

def top_five(a):
    print("Top five score are : ")
    cnt = len(a)

    if cnt < 5:
        start, stop = cnt - 1, -1  # stop set to -1 as we want to print the 0th element
    else:
        start, stop = cnt - 1, cnt - 6

    for i in range(start, stop, -1):
        print("\t {0:.2f}".format(a[i]), end=" ")


# Driver program
if __name__ == "__main__":

    unsort_A = arr.array('f', [])
    quick_sort_A = arr.array('f', [])
    flag = 1

    while flag == 1:
        print("\n 1. Accept array elements \n 2. Display the Elements \n 3. Quick Sort  \n 4. exit")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            unsort_A = accept_perc()

        elif choice == 2:
            print_perc(unsort_A)

        elif choice == 3:
            print("Elements after sorting using Insertion Sort :")
            quick_sort_A = quick_sort(unsort_A, 0, len(unsort_A) - 1)
            print_perc(quick_sort_A)
            top_five(quick_sort_A)

        else:
            print("Wrong choice")
            flag = 0


