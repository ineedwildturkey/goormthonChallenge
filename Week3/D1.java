import java.util.*;

class Week3_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), a = sc.nextInt(), b = sc.nextInt(), count = -1;
        if (b > a) {
            int temp = a;
            a = b;
            b = temp;
        }

        int aCount = n / a;
        while (aCount != 0) {
            int temp = n - (a * aCount);
            if (temp % b == 0) {
                count = aCount + (temp / b);
                break;
            } else {
                aCount -= 1;
            }
        }

        if (aCount != 0 || n % b != 0) {
            System.out.println(count);
        } else {
            System.out.println(n / b);
        }
    }
}

/**
 * 코드 해설
 * 
 * 1. n, a, b 입력, b > a면 a, b 값 교환
 * 2. n ÷ a의 몫(이하 aCount)를 이용하여 while문 실행
 * 1) n - a × aCount(이하 temp) 가 b로 나눠질 경우 aCount + temp ÷ b 출력
 * 2) 그렇지 않다면 aCount - 1로 1)을 다시 실행
 * 3) aCount가 0이라면 b만으로 나눠지는지 확인, 참이면 n ÷ b 출력
 * 4) 3)이 거짓이면 -1 출력
 */