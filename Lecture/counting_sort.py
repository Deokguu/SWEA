'''
0 <= data[i] <= 4 조건
'''

#1. 개수 세기
data = [0, 1, 2, 3, 4, 4, 3, 3]
N = len(data)

counts = [0] * 5 # 곱할 숫자는 max(data) + 1, 크기에 주의!

for idx in range(N): #N 번의 연산
    counts[data[idx]] += 1

print(counts) #[1, 1, 1, 3, 2]

#2. 개수 누적
for idx in range(1, 5): # k번의 연산
    counts[idx] += counts[idx-1]

print(counts) # [1, 2, 3, 6, 8]

#3. 정렬 counts[i]를 감소시키고 temp에 i를 삽입 / 정렬 시 같은 값이 나타났을 때, 정렬이 끝났을 때 원래 순서를 유지하도록 하는!
temp = [0] * N #정렬 결과 저장

for idx in range(N-1, -1, -1): # N번의 연산
    counts[data[idx]] -= 1  #data[i]까지의 개수 1개 감소
    temp[counts[data[idx]]] = data[idx]  #data[i]까지 차지한 칸 수 중 가장 오른쪽에 data[i] 기록
print(temp)

#제약 사항, N이 비교적 작을 때만. k가 인덱스로 사용가능한 경우.