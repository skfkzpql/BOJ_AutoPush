import java.util.Scanner;

public class Main {
    public static long mypow(long base, long exp, long mod) {
        long result = 1;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp /= 2;
        }
        return result;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println(mypow(sc.nextLong(), sc.nextLong(), sc.nextLong())); //
    }
}