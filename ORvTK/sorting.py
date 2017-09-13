# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 13:03:27 2015

@author: matevzk
"""
def quicksort(arr):
    """ Quicksort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if len(arr) <= 1:
        return arr
    else:
        return quicksort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + quicksort([x for x in arr[1:] if x>=arr[0]])
        
def insertionSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    return array
    

    
def bucketsort( A ):
  # get hash codes
  code = hashing( A )
  buckets = [list() for _ in range( code[1] )]
  # distribute data into buckets: O(n)
  for i in A:
    x = re_hashing( i, code )
    buck = buckets[x]
    buck.append( i )
 
  # Sort each bucket: O(n).
  # I mentioned above that the worst case for bucket sort is counting
  # sort. That's because in the worst case, bucket sort may end up
  # with one bucket per key. In such case, sorting each bucket would
  # take 1^2 = O(1). Even after allowing for some probabilistic
  # variance, to sort each bucket would still take 2-1/n, which is
  # still a constant. Hence, sorting all the buckets takes O(n).
 
  for bucket in buckets:
    bucket = insertionSort( bucket )
 
  ndx = 0
  # merge the buckets: O(n)
  for b in range( len( buckets ) ):
    for v in buckets[b]:
      A[ndx] = v
      ndx += 1
      
  return A
 
import math
 
def hashing( A ):
  m = A[0]
  for i in range( 1, len( A ) ):
    if ( m < A[i] ):
      m = A[i]
  result = [m, int( math.sqrt( len( A ) ) )]
  return result
 
 
def re_hashing( i, code ):
  return int( i / code[0] * ( code[1] - 1 ) )
   
    
