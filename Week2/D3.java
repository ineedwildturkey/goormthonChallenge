import java.util.*;

class Week2_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] items = { 14, 7, 1 };

        int count = 0;
        for (int i = 0; i < items.length; i++) {
            int temp = n / items[i];
            count += temp;
            n -= items[i] * temp;
        }

        System.out.println(count);
    }
}



/**
코드 해설

1. n 입력
2. 통증 감소 수치를 내림차순으로 배열(이하 items)에 저장
3. n ÷ (items에 저장된 값)을 순서대로 몫이 최대가 될 때까지 계산 후 그 몫을 결과 값에 추가, n은 나눈 후의 나머지 값으로 갱신
4. 결과 출력
 */