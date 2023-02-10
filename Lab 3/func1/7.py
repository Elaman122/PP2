def has_33(nums):
    cnt = 0
    for i in range(0, len(nums)):
        if(nums[i] == 3):
            cnt += 1

        else:
            cnt = 0

        if(cnt >= 2):
            return True


    return False
        

print(has_33([1, 3, 3]))    
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3])) 