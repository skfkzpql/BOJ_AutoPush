from itertools import combinations

def calculate_ability(team, S):
    ability = 0
    for i, j in combinations(team, 2):
        ability += S[i][j] + S[j][i]
    return ability


N = int(input())  # 팀원의 수
S = [list(map(int, input().split())) for _ in range(N)]  # 능력치 행렬

min_diff = float('inf')  # 최소 능력치 차이를 저장할 변수

# 가능한 모든 팀 조합 생성
for team1 in combinations(range(N), N // 2):
    team2 = tuple(i for i in range(N) if i not in team1)
    
    # 스타트 팀과 링크 팀의 능력치 계산
    ability_team1 = calculate_ability(team1, S)
    ability_team2 = calculate_ability(team2, S)
    
    # 두 팀의 능력치 차이 계산
    diff = abs(ability_team1 - ability_team2)
    
    # 최소 능력치 차이 갱신
    min_diff = min(min_diff, diff)

print(min_diff)

