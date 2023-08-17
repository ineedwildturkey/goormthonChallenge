import java.util.*;

class Day4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] hbg = new int[sc.nextInt()];
        for (int i = 0; i < hbg.length; i++) {
            hbg[i] = sc.nextInt();
        }

        System.out.println(isComplete(hbg));
    }

    static int isComplete(int[] arr) {
        int max = 0, maxIdx = 0, result = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
                maxIdx = i;
            }
        }

        for (int j = maxIdx; j < arr.length - 1; j++) {
            if (arr[j] < arr[j + 1])
                return result;
        }
        for (int k = maxIdx; k > 1; k--) {
            if (arr[k] < arr[k - 1])
                return result;
        }

        for (int l : arr)
            result += l;
        return result;
    }
}



/**
코드 해설

1. new int[] 배열 생성, 길이는 Scanner로 입력받음
2. 배열에 값 Scanner로 입력받음
3. isComplete 메소드 실행
	- 배열을 순회하며 최대값이 위치한 인덱스를 구함
	- 최대값을 기준으로 배열 왼쪽과 오른쪽으로 배열 순차 탐색하면서 현재 값과 다음 값을 비교하여 값이 같거나 감소하는지를 확인, 조건을 만족하면 배열의 합 반환, 그렇지 않는 경우 0 반환
4. 결과 출력
 */