import java.util.*;

public class Week2_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] items = {14, 7, 1};

        int count = 0;
        for (int i = 0; i < items.length; i++) {
            int temp = n / items[i];
            count += temp;
            n -= items[i] * temp;
        }

        System.out.println(count);
    }
}
