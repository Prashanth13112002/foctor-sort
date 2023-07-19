def factors(num):
    count=0
    i=1
    while i*i<=num:
        if num%i==0:
            if i==num//i:
                count+=1
            else:
                count+=2
        i+=1
    return count
def sort_factor(Array):
    return sorted(Array,key=lambda x:(factors(x),x))
arr=list(map(int,input().split()))
print(*sort_factor(arr))
