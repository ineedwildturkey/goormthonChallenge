import java.util.*;

class Week2_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), k = sc.nextInt();

        String[][] plate = new String[n + 2][n + 2];
        for (int i = 0; i < n + 2; i++) {
            plate[0][i] = "0";
            plate[n + 1][i] = "0";
        }
        for (int i = 1; i < n + 1; i++) {
            plate[i][0] = "0";
            plate[i][n + 1] = "0";
            for (int j = 1; j < n + 1; j++) {
                plate[i][j] = sc.next();
            }
        }

        int result = 0;
        for (int h = 1; h < n + 1; h++) {
            for (int w = 1; w < n + 1; w++) {
                int count = 0;
                if (plate[h][w].equals("0")) {
                    for (int sh = h - 1; sh < h + 2; sh++) {
                        for (int sw = w - 1; sw < w + 2; sw++) {
                            if (plate[sh][sw].equals("1"))
                                count++;
                        }
                    }
                }
                if (count == k)
                    result++;
            }
        }

        System.out.println(result);
    }
}



/**
코드 해설

1. 한 변 길이(이하 n), 찾을 깃발 개수(이하 k) 입력
2. (n + 2) * (n + 2) 크기의 2차원 배열(이하 plate) 생성 후 1행(열) 또는 마지막행(열)은 제외하고 값 입력
3. 배열 탐색
	1) 배열에 값을 입력한 칸만 탐색
	2) 해당 칸의 값이 1인 경우 패스, 0이라면 그 칸을 중심으로 3×3 구간 탐색
	3) 1의 개수가 k와 같다면 결과 값에 추가
4. 결과 출력
 */