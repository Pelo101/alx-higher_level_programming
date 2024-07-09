#!/usr/bin/python3
"""function that finds peak of unsorted integers"""

def find_peak(list_of_integers)

   def peak(arr, low, high):
    
       mid = (low + high) //2

       if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
	   return arr[mid]

       elif mid > 0 and  arr[mid - 1] > arr[mid]:
	   return peak(arr, low, mid - 1)

       else:
	   return peak(arr, mid + 1, high)


   if not list_of_integers:
       return None

   return peak(list_of_integers, 0, len(list_of_integers) - 1)
