import java.util.*;

class Week2_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), k = sc.nextInt();

        String[][] land = new String[n][n];
        int[][] score = new int[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++) {
                land[i][j] = sc.next();
                score[i][j] = 0;
            }
        }

        for (int i = 0; i < k; i++) {
            int y = sc.nextInt() - 1, x = sc.nextInt() - 1;
            for(int a = x - 1; a < x + 2; a++) {
                try {
                    String tile = land[y][a];
                    if (tile.equals("@")) score[y][a] += 2;
                    else if (tile.equals("0")) score[y][a]++;
                } catch (ArrayIndexOutOfBoundsException e) {
                    continue;
                }
            }
            for(int b = y - 1; b < y + 2; b += 2) {
                try {
                    String tile = land[b][x];
                    if (tile.equals("@")) score[b][x] += 2;
                    else if (tile.equals("0")) score[b][x]++;
                } catch (ArrayIndexOutOfBoundsException e) {
                    continue;
                }
            }
        }

        int result = 0;
        for(int[] a : score) {
            for(int b : a) {
                if(b > result) result = b;
            }
        }

        System.out.println(result);
    }
}
