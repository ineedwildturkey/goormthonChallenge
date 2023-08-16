import java.util.*;

class Day3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int result = 0;

        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            String str_n = sc.next(), s = sc.next(), str_m = sc.next();
            int n = Integer.parseInt(str_n), m = Integer.parseInt(str_m);
            switch (s) {
                case "+":
                    result += n + m;
                    break;
                case "-":
                    result += n - m;
                    break;
                case "*":
                    result += n * m;
                    break;
                case "/":
                    result += n / m;
                    break;
                default:
            }
        }
        System.out.println(result);
    }
}



/**
코드 해설

1. 결과값 초기화 T값 입력
2. for문 내에서 피연산자, 연산 기호, 연산자를 문자열 자료형으로 입력받은 후 피연산자, 연산자는 정수로 변환
3. switch-case문으로 연산 기호에 따라 계산, 정수 나눗셈은 알아서 나머지가 버려지므로 '/'' 연산 그대로 사용
4. 결과 출력
*/