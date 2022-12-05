def solution(nums):
    monster_num = len(set(nums))
    get_monster = int(len(nums)/2)
    
    if get_monster < monster_num:
        result = get_monster
    else:
        result = monster_num
    return result