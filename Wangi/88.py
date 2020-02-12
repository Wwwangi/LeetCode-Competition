#wrong
import numpy as np
class Solution(object):
    def merge(self,nums1, m, nums2, n):
        i=0
        j=0
        nums1 = filter(lambda x: x > 0, nums1)
        while(i<len(nums1)-1 and j<n):
            if(nums2[j]>=nums1[i] and nums2[j]<=nums1[i+1]):
                nums1=np.insert(nums1,i+1,nums2[j])
                i+=1
                j+=1
            else:
                i+=1
        while(j<n):
            nums1=np.append(nums1,nums2[j])
            j+=1

#correct
class Solution(object):
    def merge(self,nums1, m, nums2, n):
        while(m>0 and n>0):
            if(nums2[n-1]>nums1[m-1]):
                nums1[m+n-1]=nums2[n-1]
                n-=1
            else:
                nums1[m+n-1]=nums1[m-1]
                m-=1
        nums1[:n]=nums2[:n]
        return nums1