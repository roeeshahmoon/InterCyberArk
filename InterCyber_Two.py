def is_hill_or_valley(P, Q, A: []):
    if P == 0 or Q == len(A) - 1:
        return True
    if A[P - 1] < A[P] and A[Q] > A[Q+1]: # for hill  
        return True
    if A[P - 1] > A[P] and A[Q] < A[Q+1]: # for valley
        return True
    return False

def count_castles(A):
    n = len(A)
    if n <= 1:
        return n
    result = 0
    i = 0

    while i < n:
        start = i
        while i < n - 1 and A[i] == A[i + 1]:
            i += 1
        end = i

        if is_hill_or_valley(start, end, A):
            result += 1

        i += 1

    return result

# Test usage
A = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]
B = [-3,-3]

result_A = count_castles(A)
result_B = count_castles(B)
print("this is result A:", result_A)
print("this is result B:", result_B)

