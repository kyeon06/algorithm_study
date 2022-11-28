N = int(input())
candy = list(map(int, input().split()))

player1 = 0
player2 = 0

for game in range(N):
    total = candy[game]
    if total % 2 == 0:
        player2 += 1
    else:
        player1 += 1

				
if player1 == player2:
    print("tie")
elif player1 > player2:
    print(player1)
else:
    print(player2)