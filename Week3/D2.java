import java.util.*;

class Week3_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[][] city = new int[n][n], visited = new int[n][n];

        for(int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                city[i][j] = sc.nextInt();
                visited[i][j] = 0;
            }
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] != 1 && city[i][j] == 1) {
                    Stack<int[]> adjoin = new Stack<>();
                    adjoin.add(new int[]{i, j});
                    while (!adjoin.isEmpty()) {
                        int[] current = adjoin.pop();
                        int x = current[0], y = current[1];
                        for (int[] dirc : new int[][] {{x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1}}){
                            int dx = dirc[0], dy = dirc[1];
                            if (dx < 0 || dx >= n || dy < 0 || dy >= n) continue;
                            else if (visited[dx][dy] != 1 && city[dx][dy] == 1) {
                                adjoin.add(new int[]{dx, dy});
                                visited[dx][dy] = 1;
                            }
                        }
                    }
                    result += 1;
                }
            }
        }

        System.out.println(result);
    }
}