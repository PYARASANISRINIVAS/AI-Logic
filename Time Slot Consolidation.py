def remove_overlapping(intervals):
  ans= [intervals[0]]
  for start, end in intervals[1:]:
      if start <= ans[-1][1]:
        ans[-1][1] = max(ans[-1][1], end)  
      else:
          ans.append([start, end])             
  return ans

n=int(input("Enter the no of intervals:"))
arr=[[None]*2 for i in range(n)]
for i in range(n):
  arr[i][0]=int(input("Enter start number :"))
  arr[i][1]=int(input("Enter the end number : "))

arr=[[1, 3], [2, 6], [8, 10], [15, 18]]
print(remove_overlapping(arr))
