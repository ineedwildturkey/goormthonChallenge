def game(board, y, x, n) :
    userLoc = y * n + x
    visited = [0 for _ in range(n ** 2)]
    visited[userLoc] = 1
    
    keep = True
    while keep :
        cnt, cmd = int(board[userLoc][:-1]), board[userLoc][-1]
        lCheck, rCheck = (userLoc // n) * n, (userLoc // n + 1) * n - 1
        for _ in range(cnt) :
            userLoc += dirc[cmd]
            if cmd == "U" and userLoc < 0 : userLoc += n ** 2
            elif cmd == "D" and userLoc > n ** 2 - 1 : userLoc -= n ** 2
            elif cmd == "L" and userLoc < lCheck : userLoc += n
            elif cmd == "R" and userLoc > rCheck : userLoc -= n
            
            if visited[userLoc] :
                keep = False
                break
            visited[userLoc] = 1
    
    return sum(visited)

n = int(input())

gy, gx = map(int, input().split())
py, px = map(int, input().split())
gy -= 1
gx -= 1
py -= 1
px -= 1

board = ["" for _ in range(n ** 2)]
for i in range(n) :
    for idx, cmd in enumerate(list(map(str, input().split()))) :
        board[n * i + idx] = cmd
dirc = {"U" : -n, "D" : n, "L" : -1, "R" : 1}

scoreG, scoreP = game(board, gy, gx, n), game(board, py, px, n)

print(f'goorm {scoreG}' if scoreG > scoreP else f'player {scoreP}')

"""
코드 해설

1. 한 변의 길이(이하 n), goorm과 player의 좌표(gy, gx, py, px) 입력
2. n^2 길이의 배열(이하 board) 생성 후 각 좌표의 커맨드 입력
3. 커맨드 값에 따른 이동량 값을 저장한 사전(이하 dirc) 생성
4. 게임(game 함수) 실행
    1) 유저가 위치 값(이하 userLoc) 지정
    2) 유저가 지나간 곳을 저장하는 배열(이하 visited) 생성, 유저가 있던 위치에 +1
    3) board[userLoc]의 커맨드 확인, 커맨드의 횟수만큼 dirc[해당 커맨드] 값 이동
    4) 게임판 상하좌우 경계를 벗어나면 반대쪽으로 들어오도록 userLoc 값 조정
    5) 이미 지나갔던 곳이라면 게임 중단 후 유저가 visited의 합 반환
5. 결과 출력
"""