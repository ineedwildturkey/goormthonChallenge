import java.util.*;

class Week2_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), k = sc.nextInt();

        String[][] plate = new String[n + 2][n + 2];
        for(int i = 0; i < n + 2; i++) {
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
        for (int h = 1; h < n + 1; h++){
            for (int w = 1; w < n + 1; w++) {
                int count = 0;
                if (plate[h][w].equals("0")) {
                    for (int sh = h - 1; sh < h + 2; sh++) {
                        for (int sw = w - 1; sw < w + 2; sw++) {
                            if (plate[sh][sw].equals("1")) count++;
                        }
                    }
                }
                if (count == k) result++;
            }
        }

        System.out.println(result);
    }
}
