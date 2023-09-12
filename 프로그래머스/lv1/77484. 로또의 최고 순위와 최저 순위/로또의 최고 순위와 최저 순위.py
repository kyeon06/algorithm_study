def solution(lottos, win_nums):
  result = []
  win = { 6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6 }

  if sum(lottos) == 0:
    result.append(1)
    result.append(6)
    return result

  notnum = lottos.count(0)
  cnt = 0

  for i in lottos:
    if i in win_nums:
      cnt += 1
  
  result.append(win[cnt+notnum])
  result.append(win[cnt])
  return result