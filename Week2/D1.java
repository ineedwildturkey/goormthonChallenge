import java.util.*;

class Week2_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String s = sc.next();

        ArrayList<String[]> strList = new ArrayList<>();
        Set<String> partStr = new HashSet<>();
        for (int i = 1; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                strList.add(new String[] { s.substring(0, i), s.substring(i, j), s.substring(j) });
                partStr.add(s.substring(0, i));
                partStr.add(s.substring(i, j));
                partStr.add(s.substring(j));
            }
        }

        ArrayList<String> strScore = new ArrayList<>(partStr);
        Collections.sort(strScore);

        int result = 0;
        for (int a = 0; a < strList.size(); a++) {
            String[] tempList = strList.get(a);
            int tempScore = 0;
            for (int b = 0; b < tempList.length; b++) {
                tempScore += strScore.indexOf(tempList[b]) + 1;
            }
            if (tempScore > result)
                result = tempScore;
        }

        System.out.println(result);
    }
}



/**
코드 해설

1. 문자열 길이(이하 n), 문자열(이하 s) 입력
2. substring을 이용하여 s를 3등분하여 ArrayList(이하 strList)에 배열 형태로 저장
3. 분할한 부분 문자열은 HashSet(이하 partStr)에 추가
4. 점수 계산을 위해 새로운 ArrayList(이하 strScore)에 partStr에 저장된 부분 문자열을 저장 후 정렬
5. strList에 저장된 3등분된 문자열에 각각 값을 매기고 최대값 구함
6. 결과 출력
*/