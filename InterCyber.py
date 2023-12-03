def solution(S):
    ptr_start = 0
    ptr_final = len(S) - 1
    while ptr_start < ptr_final:
        if S[ptr_start] != S[ptr_final]:
            return -1
        ptr_start += 1
        ptr_final -= 1
    return ptr_start if ptr_start == ptr_final else -1

Str = "racecar"
Str = "x"
print(solution(Str))