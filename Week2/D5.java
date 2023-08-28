import java.util.*;

class Week2_5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int gy = sc.nextInt() - 1, gx = sc.nextInt() - 1, py = sc.nextInt() - 1, px = sc.nextInt() - 1;

        String[] board = new String[(int) Math.pow(n, 2)];
        for (int i = 0; i < board.length; i++) {
            board[i] = sc.next();
        }

        int scoreG = game(board, gy, gx, n), scoreP = game(board, py, px, n);
        String result = (scoreG > scoreP) ? "goorm " + scoreG : "player " + scoreP;
        System.out.println(result);
    }

    public static int game(String[] board, int y, int x, int n) {
        int userLoc = y * n + x, len = board.length;
        int[] visited = new int[(int) Math.pow(n, 2)];
        visited[userLoc] = 1;

        boolean keep = true;
        while (keep) {
            int strLen = board[userLoc].length(), lCheck = (userLoc / n) * n, rCheck = (userLoc / n + 1) * n - 1;
            int cnt = Integer.parseInt(board[userLoc].substring(0, strLen - 1));
            String cmd = board[userLoc].substring(strLen - 1, strLen);
            for (int i = 0; i < cnt; i++) {
                switch (cmd) {
                    case "U":
                        userLoc -= n;
                        if (userLoc < 0)
                            userLoc += len;
                        break;
                    case "D":
                        userLoc += n;
                        if (userLoc > len - 1)
                            userLoc -= len;
                        break;
                    case "L":
                        userLoc--;
                        if (userLoc < lCheck)
                            userLoc += n;
                        break;
                    case "R":
                        userLoc++;
                        if (userLoc > rCheck)
                            userLoc -= n;
                        break;
                    default:
                        break;
                }

                if (visited[userLoc] == 1) {
                    keep = false;
                    break;
                } else {
                    visited[userLoc] = 1;
                }
            }
        }

        int total = 0;
        for (int j : visited)
            total += j;

        return total;
    }
}

/**
코드 해설

1. 한 변의 길이(이하 n), goorm과 player의 좌표(gy, gx, py, px) 입력
2. n^2 길이의 배열(이하 board) 생성 후 각 좌표의 커맨드 입력
3. 게임(game 메서드) 실행
	1) 유저의 위치 값 지정(이하 userLoc)
	2) 유저가 지나간 위치를 저장하는 배열(이하 score) 생성 후 해당 위치에 +1
	3) 유저 위치(인덱스)의 board에 저장된 커맨드를 슬라이싱 하여 지정된 횟수만큼 커맨드 실행
	4) 상하좌우 경계를 벗어난 경우 반대쪽으로 이동하도록 인덱스 값 조정
	5) 이미 지나간 곳이라면 게임 중단 후 score 배열의 총합 반환
4. 결과 출력
 */