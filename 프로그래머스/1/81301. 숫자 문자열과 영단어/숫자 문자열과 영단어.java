class Solution {
    public int solution(String s) {
        int answer = 0;
        char[] c = s.toCharArray();
        String[] numToAlpha = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        
        StringBuffer sb = new StringBuffer();

        for (int i = 0; i < c.length; i++) {
            char cha = c[i];
            
            if (Character.isDigit(cha)) {
                answer = answer * 10 + (int) (cha - '0');
            } else {
                sb.append(cha);

                for (int j = 0; j < 10; j++) {
                    if (numToAlpha[j].equals(sb.toString())) {
                        answer = answer * 10 + j;
                        sb.delete(0, sb.length());
                        break;
                    }
                }
            }
        }
        return answer;
    }
}