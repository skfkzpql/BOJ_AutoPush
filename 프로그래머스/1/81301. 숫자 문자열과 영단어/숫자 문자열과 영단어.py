def solution(s):
    answer = 0
    c = list(s)
    num_to_alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    sb = []

    for cha in c:
        if cha.isdigit():
            answer = answer * 10 + int(cha)
        else:
            sb.append(cha)

            for j in range(10):
                if num_to_alpha[j] == ''.join(sb):
                    answer = answer * 10 + j
                    sb.clear()
                    break

    return answer
