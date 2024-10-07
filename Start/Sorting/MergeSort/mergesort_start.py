# Example file for Programming Foundations: Algorithms by Joe Marini
# Implement a merge sort with recursion

'''
Merge Sort
* divide-and-conquer algorithm
* breaks a dataset into individual pieces and merges them
* uses recursion to operate on datasets
* performs well on large data sets
* O(n log n) time complexity 
* how it works
    - break down an unsorted list into segments until you 
        are down to each value being in its own array (this is inherently sorted since there is only one element)
    - then merge these arrays back up into each other until we've rebuilt the original orray in sorted form
'''


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # TODO: recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # TODO: if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # TODO: if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


# test the merge sort with data
print(items)
mergesort(items)
print(items)
