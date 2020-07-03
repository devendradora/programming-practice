nums=[2,0,9,5,0,0,7]

p=0
for i in range(0,len(nums)):
	if nums[i] !=0:
		nums[i],nums[p]=nums[p],nums[i]
		p+=1

for i in range(0,len(nums)):
	print(nums[i])

