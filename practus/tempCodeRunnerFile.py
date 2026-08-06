nums=[13,45,6,4,15,7]
n=len(nums)
t=10
for i in range (0,n):
    for j in range (i,n) :
        if nums[i]+nums[j]==t :
            print(i,j)