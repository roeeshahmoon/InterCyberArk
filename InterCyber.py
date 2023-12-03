def solution(S):
    ptr_start = 0
    ptr_final = len(S) - 1
    while ptr_start < ptr_final:
        if S[ptr_start] != S[ptr_final]:
            return -1
        ptr_start += 1
        ptr_final -= 1
    return ptr_start if ptr_start == ptr_final else -1

Str_A = "racecar"
Str_B = "x"
print("this is Str A:", solution(Str_A))
print("this is Str B:", solution(Str_B))