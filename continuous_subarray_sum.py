# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 14:13:05 2022

@author: Ekaterina Ilinova
"""


#For an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
#A good subarray is a subarray where: its length is at least two, and
#the sum of the elements of the subarray is a multiple of k.
#:A subarray is a contiguous part of the array.
#An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k




class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map={}
        
        summ=nums[0]%k
        i=1
        map[summ]=0
        while i<len(nums):
            summ=summ+nums[i]
            summ=summ%k
            if summ==0:
                return True
            elif summ in map:
                if i-map[summ]>1:
                    return True
            else:
                map[summ]=i
            i=i+1
        return False