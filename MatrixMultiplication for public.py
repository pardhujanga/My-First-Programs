
def mm(x,y):
    """
    let x(the first input) be a matrix of dimensions i1*j1 and y(the second input) be of dimensions i2*j2.
    j1 must be equal to i2 for matrix multiplication to work as intended.
    """
    result={}
    i1=len(x)
    i2=j1=len(y)
    j2=len(y[0])
    try:
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

    except Exception:
        print('input error: please make sure the input follows the docstring guidelines.')
        print('the length of nested lists in x and y must all be equal(seperately)')
        print('the lenght of nested lists in first input must equal the no. of nested lists in second input.')
