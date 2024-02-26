import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] l = new int[N];
        for (int i = 0; i < N; i++) {
            l[i] = scanner.nextInt();
        }

        int[] d = new int[20];
        for (int i : l) {
            for (int j = 0; j < 20; j++) {
                d[j] += (i >> j) & 1;
            }
        }

        long result = 0;
        for (int i = 0; i < 20; i++) {
            result += (long) d[i] * (N - d[i]) * (1 << i);
        }

        System.out.println(result);
    }
}
