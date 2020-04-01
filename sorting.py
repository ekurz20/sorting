#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input which controls how the elements of the list should be compared against each other.
If cmp(a,b) returns -1, then a<b;
if cmp(a,b) returns  1, then a>b;
if cmp(a,b) returns  0, then a==b.
'''

import random

def cmp_standard(a,b):
    '''
    used for sorting from lowest to highest
    '''
    if a<b:
        return -1
    if b<a:
        return 1
    return 0


def cmp_reverse(a,b):
    '''
    used for sorting from highest to lowest
    '''
    if a<b:
        return 1
    if b<a:
        return -1
    return 0


def cmp_last_digit(a,b):
    '''
    used for sorting based on the last digit only
    '''
    return cmp_standard(a%10,b%10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    '''
    if len(xs)>0 and len(ys)>0:
        z = []
        x = 0
        y = 0
        while x<=len(xs)-1 and y<=len(ys)-1:
            if cmp(xs[x],ys[y])==0:
                z.append(xs[x])
                z.append(ys[y])
                x+=1
                y+=1
            elif cmp(xs[x],ys[y])==1:
                z.append(ys[y])
                y+=1
            elif cmp(xs[x]ys[y])==-1:
                z.append(xs[x])
                x+=1
        if x > y:
            z.append(ys[y])
        if x < y:
            z.append(xs[x])
        if len(xs) > len(ys):
            z.append(xs[len(xs)-1])
        if len(ys) > len(xs):
            z.append(ys[len(ys)-1])
        return z
    return xs+ys

def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs
    '''
    if len(xs)==1 or len(xs)==0:
        return xs
    else:
        z=1
        while z<=len(xs):
            left = xs[0:int(len(xs)/2)]
            right = xs[int(len(xs)/2):len(xs)]
            x=1
            while x<=len(left):
                for index in range(len(left)-1):
                    a=left[index]
                    b=left[index+1]
                    if cmp(a,b)==1:
                        left[index]=b
                        left[index+1]=a
                x+=1
            a = left[len(left)-1]
            b = right[0]
            if cmp(a,b)==1:
                left[len(left)-1]=b
                right[0]=a
            y=1
            while y<=len(right):
                for index in range(len(right)-1):
                    a = right[index]
                    b = right[index+1]
                    if cmp(a,b)==1:
                        right[index]=b
                        right[index+1]=a
                y+=1
            z+=1
        return left+right

def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected, 
    and the list is split into a "less than" sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)

    You should return a sorted version of the input list xs
    '''


def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented in-place,
    i.e. with O(1) memory requirement.
    Merge sort, on the other hand, has an O(n) memory requirement.

    Follow the pseudocode of the Lomuto partition scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    You should directly modify the input xs variable instead of returning a copy of the list.
    '''
