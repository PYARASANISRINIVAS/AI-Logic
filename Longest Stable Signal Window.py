def solve_sample(n, signals, k):
    max_len = 0
    best_start = 1
    
    for i in range(n):
        current_min = signals[i]
        current_max = signals[i]
        
        for j in range(i, n):

            if signals[j] < current_min:
                current_min = signals[j]
            if signals[j] > current_max:
                current_max = signals[j]
            if current_max - current_min <= k:
                current_len = j - i + 1

                if current_len > max_len:
                    max_len = current_len
                    best_start = i + 1  
            else:
                break 

    print(max_len ,best_start)

n=int(input("Enter the number of signals :"))
signals=list(map(int,input().split()))
k=int(input("Enter the k value"))
solve_sample(n,signals,k)
