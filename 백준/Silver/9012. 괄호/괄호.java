import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
   
        int T = Integer.parseInt(br.readLine());
        
        for(int i = 0; i < T; i++) {
            Stack<Character> stack = new Stack<>();
            String s = br.readLine();
            
            boolean check = true;
            
            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);
                if (c == '(') {
                    stack.push(c);
                } else if (stack.isEmpty()){
                    check = false;
                    break;
                } else {
                    stack.pop();
                }
            }
            System.out.println(check && stack.isEmpty() ? "YES" : "NO");
        }

        br.close();
    }
}