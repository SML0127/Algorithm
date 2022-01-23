import sys

sys.stdin = open("10507/input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    n, p = map(int, input().split())
    nums = list(map(int, input().split()))
    lp = 0
    rp = 1
    result = 1
    prev = 1
    while rp<len(nums):
        temp = prev
        diff = nums[rp] - nums[lp] - temp # 3
        print(lp, rp, diff)
        while diff<=p: # 일수 간의 차이 - temp
            rp += 1 # 1 5 6 10 11
            temp += 1 # num of used p
            if rp==len(nums):
                break
            diff = nums[rp] - nums[lp] - temp
        result = max(temp, result)
        prev = temp - 1
        lp += 1
 
    print("#%d %d" %(test_case, result+p))