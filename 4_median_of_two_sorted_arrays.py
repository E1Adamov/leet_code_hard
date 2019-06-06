class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # combine and sort arrays
        full_arr = sorted(nums1 + nums2)

        # if the array length is odd
        if len(full_arr) % 2 != 0:
            # return the middle element
            return float(full_arr[int((int(len(full_arr)-1)/2))])

        else:
            # return the mean of two middle elements
            return (full_arr[int(len(full_arr)/2)] + full_arr[int(len(full_arr)/2)-1]) / 2
