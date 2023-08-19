import java.util.*;

class Day2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int t = sc.nextInt(), m = sc.nextInt();

        for (int i = 0; i < n; i++) {
            m += sc.nextInt();
            while (m >= 60) {
                t = t < 23 ? ++t : 0;
                m -= 60;
            }
        }

        System.out.println(t + " " + m);
    }
}



/**
코드 해설
 
1. N, T, M 순서에 맞게 입력
2. 개발 시간 입력하여 M에 추가 (N번 반복)
3. M이 60 이상일 경우 M이 60 미만이 될 때까지 m -= 60 반복하며 T값 변경 (람다식)
	- T가 23 미만이라면 ++T(T++은 갑이 변경되지 않으니 주의)
	- T가 23(이상)이라면 T = 0
4. 결과값 출력
*/