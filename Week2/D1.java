import java.util.*;

public class Week2_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String s = sc.next();

        ArrayList<String[]> strList = new ArrayList<>();
        Set<String> partStr = new HashSet<>();
        for(int i = 1; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                strList.add(new String[]{s.substring(0, i), s.substring(i, j), s.substring(j)});
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
            if (tempScore > result) result = tempScore;
        }

        System.out.println(result);
    }
}
