arr= [[1, 0, 0, 0, 1],
      [1, 0, 1, 0, 0],
      [0, 1, 1, 1, 0],
      [0, 0, 1, 1, 0],
      [1, 0, 0, 0, 0]]
marker=[[0,0,0,0,0]for x in range(5)]
def search_m(arr,marker,x,y):
    if ( x<0 or x>=5 )or (y<0 or y>=5):
        return 0
    elif arr[x][y]==1 and marker [x][y]==0:
        marker[x][y]=1
        search_m(arr,marker, x - 1, y)
        search_m(arr, marker, x + 1, y)
        search_m(arr,marker, x , y+1)
        search_m(arr, marker, x , y-1)


search_m(arr,marker,2,2)
c=0
for i in range(5):
    for j in range(5):
        if marker[i][j]==1:
            c+=1
print(c)
