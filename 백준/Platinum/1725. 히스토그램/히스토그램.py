def largest_rectangle_area_histogram(heights):
    n = len(heights)
    
    # 스택을 활용한 가장 큰 직사각형의 넓이 계산 함수
    def calculate_largest_rectangle():
        stack = []
        max_area = 0
        
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area
    
    # 가장 큰 직사각형의 넓이 계산
    max_area = calculate_largest_rectangle()
    
    return max_area

# 입력 받기
N = int(input())
histogram = [int(input()) for _ in range(N)]

# 결과 출력
result = largest_rectangle_area_histogram(histogram)
print(result)
