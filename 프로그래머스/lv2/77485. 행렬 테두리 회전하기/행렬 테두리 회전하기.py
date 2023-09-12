def solution(rows, columns, queries):
    result = []
    table = []

    for r in range(rows):
      table.append([j for j in range(r*columns+1, columns*(r+1)+1)])

    for query in queries:
      query = [x-1 for x in query]
      startNum = table[query[0]][query[1]]
      small = startNum

      #left
      for l in range(query[0]+1, query[2]+1):
        table[l-1][query[1]] = table[l][query[1]]
        small = min(small, table[l][query[1]])

      #bottom
      for b in range(query[1]+1, query[3]+1):
        table[query[2]][b-1] = table[query[2]][b]
        small = min(small, table[query[2]][b])

      #right
      for r in range(query[2]-1, query[0]-1, -1):
        table[r+1][query[3]] = table[r][query[3]]
        small = min(small, table[r][query[3]])

      #top
      for t in range(query[3]-1, query[1]-1, -1):
        table[query[0]][t+1] = table[query[0]][t]
        small = min(small, table[query[0]][t])

      table[query[0]][query[1]+1] = startNum
      result.append(small)

    return result