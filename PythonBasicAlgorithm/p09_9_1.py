# -*- coding: utf-8 -*-
# 일반적인 삽입 정렬 알고리즘으로 리스트를 정렬하는 과정을 적으시오
# 1. 삽입 정렬 함수를 정의내린다.
# 2. 값을 출력할 빈 리스트를 하나 만든다.
# 3. while 문을 사용해 입력받은 리스트가 빈 리스트가 될 때까지 값을 하나씩 빼오도록 한다.
# 4. 빼오는 것은 무작위로 빼오지만 (맨 앞의 값만 빼오는 것 처럼) 이를 새 리스트에 입력할 때 적절하게 입력한다.
# 5. 적절하게 입력하기 위해서, 리스트를 읽어온 다음, 빼온 값 보다 작은 값보다는 뒤에,
# 큰 값보다는 앞의 위치를 알아내는 함수를 만든다.
# 6. 그 위치란 결국 큰 값 바로 앞의 위치이므로, insert의 특성에 따라 빼온 값보다 가장 가깝게 큰 값의 위치가 된다.
# 7. 위치에 맞게 값을 빼온 후, 삽입한다. 정렬된 리스트를 출력한다.


def find_ins_idx(r, v):
    # 이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인하여
    for i in range(0, len(r)):
        # v 값보다 i번 위치에 있는 자료값이 크면
        # v가 그 값 바로 앞에 놓여야 정렬 순서가 유지된다.
        if v < r[i]:
            return i
    # 적절한 위치를 못 찾았을 때는
    # v가 r의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입한다.
    return len(r)

def ins_sort(a):
    result = [] # 새 리스트로 정렬값을 저장
    while a : # 기존 리스트에 값이 남아 있는 동안 반복
        value = a.pop(0) # 기존 리스트에서 한 개를 꺼낸다.
        ins_idx = find_ins_idx(result, value) # 꺼낸 값이 들어갈 적당한 위치를 찾는다.
        result.insert(ins_idx, value) # 찾은 위치에 값 삽입
    return result

d = [2, 4, 5, 1, 3]
print(ins_sort(d))
