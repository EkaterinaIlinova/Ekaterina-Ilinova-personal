# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 14:03:56 2022

@author: Ekaterina Ilinova
"""
#For  two strings s and t of lengths m and n respectively, find the minimum window 
#substring of s, such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string ""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t)>len(s):
            return ""
        minlen=len(s)
        map1={}
        map2={}
        #creating the map  for the string t
        for ch in t:
            if ch in map1:
                map1[ch]+=1
            else:
                map1[ch]=1
                map2[ch]=0
         
        summgoal=len(t)
        istart=-1 
        iend=-1
        #tentative start of substring
        istent=0
        i=0
        summ=0
        while (i<len(s))&(istent<=len(s)-len(t)): 
            ch=s[i]
            if ch in map2:
                map2[ch]+=1
                if map1[ch]>=map2[ch]:
                    summ=summ+1
                    
                    if summ==summgoal:
                        while istent<=i-len(t):
                            if (s[istent] in map2):
                                if map2[s[istent]]==map1[s[istent]]:
                                    break
                                map2[s[istent]]-=1
                            istent+=1
                        
                        if (i-istent+1<=minlen):
                            iend=i
                            istart=istent
                            minlen=i-istent
                        
                        
                        
                        
                        map2[s[istent]]-=1
                        summ-=1
                        istent+=1
                        
            i+=1
        
        
        answer=""
        if(istart>=0)&(iend>=istart):
            for j in range(istart,iend+1):
                answer=answer+s[j]
                
        return answer
    
    
    
            
        
        
        