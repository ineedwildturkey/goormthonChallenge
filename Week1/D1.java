import java.util.*;

class Day1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double w = sc.nextDouble(), r = sc.nextDouble();

        System.out.println((int) (w * (1 + r / 30)));
    }
}



/**
코드 해설
 
1. W, R을 공백으로 구분하여 실수 자료형으로 입력받음(정수 자료형일 시 올바르게 계산되지 않음, 입력할 값의 자료형은 상관없음)
2. 소수점 이하 값 버리므로 출력 전 계산 값을 정수로 변환
*/