def solution(A):
    all_negative = all(x < 0 for x in A)

    if all_negative:
        return 1
    else:
        A = [x for x in A if x>0]
        
    if len(A)==0:
        return 1
    elif len(A)==1:
        if A[0]>1:
            return A[0]-1    
        else:
            return A[0]+1   
    
    max_value = max(A)
    min_value = min(A)
    numbers   = set(range(min_value,max_value+1))
    not_present = set(numbers).difference(A) 
    
    if not_present:
        return min(not_present)
    else:
        return max_value+1

# print(solution([1, 3, 6, 4, 1, 2]))
# print(solution([1, 2, 3]))
# print(solution([-1, -3]))
print(solution([2]))
