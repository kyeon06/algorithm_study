def solution(nums):
    getCnt = len(nums) // 2
    
    # 가져가야하는 폰켓몬 수가 폰켓몬 종류보다 적을 경우
    if len(set(nums)) >= getCnt:
        return getCnt
    # 가져가야하는 폰켓몬의 수가 폰켓몬 종류보다 클 경우
    else:
        return len(set(nums))