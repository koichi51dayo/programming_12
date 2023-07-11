import copy
d0 = [ 8, 14, 13, 7, 15, 12, 16, 15, 12, 9 ]
d1 = [ 8, 14, 13, 7, 15 ]

searchlist=[]
dn=d1
l=len(dn)

class towdata:
    def __init__(self,num,val,next):
        self.num=num
        self.val=val
        self.next=next
        
def make_list(d):#循環リストの作成
    d=d[::-1]
    x=towdata(len(d),d[0],next=None)
    keepnum=d[0]
    del d[0]
    for idx,i in enumerate(d):
        newx=towdata(len(d)-idx,i,next=x)
        x=newx
    p=x #一番奥のノードと先頭ノードをつなげる
    while x.num!=l:
        x=x.next
    x.next=p  
    d.insert(0,keepnum)
    x=x.next
    return x
    
def make_searchlist(x:int,numlist:list,data=[]):
    global l
    if x==0:
        searchlist.append(copy.deepcopy(data))
        
    elif numlist==[]:
        pass
  
    else:  
        for idx,i in enumerate(numlist):
            if idx==0:
                z=[i]
            elif i==l:
                z=list(range(numlist[0],l+1))
            else:
                z=list(range(numlist[0],numlist[idx+1]))
                
            data.append(i)
            newlist=list(set(numlist)-set(z))
            newlist.sort()  #仕様かバグかわからないがソートしないと変な並び順になる
            make_searchlist(x-1,newlist,data)
            del data[-1] 
      
def defmin(x,y:list):
    count,start,end=0,0,0
    keepx=towdata(float('inf'),None,None)
    d=[]
    while True:
        if x.num==keepx.num and end==1:
            d.append(count)
            break
        
        if x.num in y:
            if count==0:
                keepx=copy.deepcopy(x)
                start=1
            else:
                d.append(count)
                count=0
                
        
        if start==1:
            count+=x.val
            end=1
        x=x.next
             
    mind=min(d)
    return mind
                
def main():
    keepmin=float('-inf')
    keeplist=[]
    x=make_list(dn)
    while True:
        a=int(input("見張りの数を入力してください(2以上{}以下で入力)".format(l)))
        if a<2 or a>l:
            print("数値が無効です")
        else:
            break
    numlist=list(range(1,l+1))
    make_searchlist(a,numlist)
    for i in searchlist:
        b=defmin(x,i)
        if b>keepmin:
            keepmin=b
            keeplist=i
            
    print("見張りを配置する塔は",end='')
    for i in keeplist:
        print(f"{i}番目",end=' ')
    print("\nその時の距離の最小値は{}".format(keepmin))
       
            
            
main()    
      
      
      


        
    
    
        