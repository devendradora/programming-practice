/*
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
*/

import java.util.*;
import java.util.stream.Collectors;


class Solution {
    public String largestNumber(int[] nums) {
    	List<String> nums_str = new ArrayList<String>();
    	for(int i=0;i<nums.length;i++)
    		nums_str.add(String.valueOf(nums[i]));

    	Collections.sort(nums_str, new Comparator<String>(){
    		@Override
    		public int compare(String X, String Y){
    			//X=35 , Y=9 ; XY=359 ,YX=935
    			String XY = X+Y;
    			String YX = Y+X;
    			//return XY.compareTo(YX) > 0 ? -1 : 1;
    			return YX.compareTo(XY);

    		}

    	});

    	if(nums_str.get(0).equals("0"))
    		return "0";

    	return nums_str.stream().collect(Collectors.joining(""));  	        
    }

    public static void main(String[] args){
    	Solution sol = new Solution();
		int[] nums ={3, 30, 34, 5, 9};
		System.out.println(sol.largestNumber(nums));
    }
}




