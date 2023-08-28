import java.util.*;

class Week2_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), k = sc.nextInt();

        String[][] land = new String[n][n];
        int[][] score = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                land[i][j] = sc.next();
                score[i][j] = 0;
            }
        }

        for (int i = 0; i < k; i++) {
            int y = sc.nextInt() - 1, x = sc.nextInt() - 1;
            for (int a = x - 1; a < x + 2; a++) {
                try {
                    String tile = land[y][a];
                    if (tile.equals("@"))
                        score[y][a] += 2;
                    else if (tile.equals("0"))
                        score[y][a]++;
                } catch (ArrayIndexOutOfBoundsException e) {
                    continue;
                }
            }
            for (int b = y - 1; b < y + 2; b += 2) {
                try {
                    String tile = land[b][x];
                    if (tile.equals("@"))
                        score[b][x] += 2;
                    else if (tile.equals("0"))
                        score[b][x]++;
                } catch (ArrayIndexOutOfBoundsException e) {
                    continue;
                }
            }
        }

        int result = 0;
        for (int[] a : score) {
            for (int b : a) {
                if (b > result)
                    result = b;
            }
        }

        System.out.println(result);
    }
}



/**
코드 해설

1. 한 변 길이(이하 n), 폭탄 떨어트릴 횟수(이하 k) 입력
2. n * n 크기의 2차원 String 배열(해당 칸 상태 저장용, 이하 land)와 int 배열(해당 칸 점수 저장용, 이하 score) 생성
3. 폭탄 떨어트리기
	1) 입력한 좌표에 해당하는 land 값과 상하좌우의 값을 확인
	2) 숫자면 입력한 좌표에 해당하는 score 값 + 1, @면 +2, #이면 아무것도 하지 않음
	3) 만약 인덱스 오류가 발생하면 try-catch로 패스
4. score 배열 순회, 최댓값 출력
 */