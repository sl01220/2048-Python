n=int(input())
for _ in range(n):
    data=list(map(int,input().split()))
    hc=[]
    for x in data:
        card=[]
        flower=(x-1)//13
        point=x%13
        card.append(flower)
        card.append(point)