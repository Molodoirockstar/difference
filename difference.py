def get_users(file):
  f=open(file,'r')
  data=f.read().replace('\n','')
  data=data.split('user: ')
  file_names=[]
  data.pop(0)
  for text in data:
    head, sep, tail = text.partition(',')
    file_names.append(head)
  return file_names        
    
def del_duplicates(arr):
    n=len(arr)
    if(n==0 or n == 1):
        return arr

    pivot=0
    for last_o in range(0, n-1):
        if(arr[last_o]!=arr[last_o+1]):
            arr[pivot]=arr[last_o]
            pivot=pivot+1
    arr[pivot]=arr[n-1]
    return arr[0:pivot+1]
    
def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return array

arr=list(del_duplicates(sort(get_users('file'))))
arr1=list(del_duplicates(sort(get_users('file1'))))

for e in arr1:
    for e1 in arr:
        if e == e1:
            arr.remove(e1)
            
            break
        else:
            continue
        
print(arr)        
