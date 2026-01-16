def sq_cube():
  arr1=[]
  arr2=[]
  while i<=10:
    square=i*i
    cube=i*i*i
    square.append(arr1)
    cube.append(arr2)
    i=i+1
  return arr1,arr2
if "__name__"=="__main__":
  print("square:",sq_cube())
  print("cube:",sq_cube())
  
