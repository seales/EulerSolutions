import math

def foo(nums, request):
    if len(nums)  == 1:
        return str(nums.pop(0))
    else:
        list.sort(nums)
        possible_perms = math.factorial(len(nums))
        per_num = int(possible_perms/len(nums))
        position = int(request / per_num)

return str(nums.pop(position)) + foo(nums, request- (position*per_num))

assert foo([0,1,2,3,4,5,6,7,8,9], 0) == "0123456789"
assert foo([0,1,2,3,4,5,6,7,8,9], 1) == "0123456798"
assert foo([0,1,2,3,4,5,6,7,8,9], 2) == "0123456879"

assert foo([0,1,2], 0) == "012"
assert foo([0,1,2], 1) == "021"
assert foo([0,1,2], 2) == "102"
assert foo([0,1,2], 3) == "120"
assert foo([0,1,2], 4) == "201"
assert foo([0,1,2], 5) == "210"


print foo([0,1,2,3,4,5,6,7,8,9], 999999)
