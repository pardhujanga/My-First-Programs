
def mm(x,y):
    """
    let x be a matrix of dimensions i1*j1 and y be of dimensions i2*j2 and j1=i2
    """
    result={}
    i1=len(x)
    i2=j1=len(y)
    j2=len(y[0])
    for a in range(i1):
        result[a]={}
    for i in range(i1):
        for j in range(j2):
            a=0
            for k in range(i2):
                a+=(x[i][k]*y[k][j])
                result[i][j]=a
            print(result[i][j])
    ans=[]
    for i in result:
        ans.append(list(result[i].values()))
    return ans
