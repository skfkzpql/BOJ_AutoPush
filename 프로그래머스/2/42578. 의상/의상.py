from collections import defaultdict

def solution(clothes):
    # 각 의상 종류별로 개수를 세는 딕셔너리 생성
    clothes_dict = defaultdict(int)
    
    for _, category in clothes:
        clothes_dict[category] += 1
    
    # 각 의상 종류별로 선택하는 경우의 수 계산
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)  # 각 종류별로 선택하지 않는 경우를 포함하기 위해 +1
    
    # 모든 의상을 입지 않는 경우를 제외하기 위해 1을 빼줌
    answer -= 1
    
    return answer

