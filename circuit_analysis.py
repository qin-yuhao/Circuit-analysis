import sympy


graph = {
    'U1':['R1'],
    'R3':['R4'],
    'R2':['U2'],
    'U2':['U1'],
    'R4':['U1'],
    'R1':['R2','R3']
}

class Node():
    def __init__(self,name,U = None,I = None,R = None,P = None) -> None:
        self.name = name
        self.U = U
        self.R = R
        self.I = I
        self.P = P
        if U and I:
            self.R = self.U / self.I
            self.P = self.U*self.I
        elif U and R:
            self.I = self.U/self.R
            self.P = self.U*self.I
        elif U and P:
            self.I = self.P /self. U
            self.R = self.U /self.I
        elif R and I:
            self.U = self.I * self.R
            self.P = self.U*self.I
        elif R and P:
            self.I = (self.P / self.R) ** 1/2
            self.U = self.I * self.R
        elif I and P:
            self.U = self.P/self.I

def findC(graph, s):
    stack = []
    stack.append(s)
    path = []
    res = []
    lay = [0]
    i = 1
    while (len(stack)>0):
        parent = stack.pop()
        nodes = graph[parent]
        if parent not in res:
            res.append(parent)
            lay.append(0)
            for node in nodes:
                stack.append(node)        
                lay[i] =lay[i] +1
            i += 1
        else:
            path.append(res.copy())
            res.pop()
            i -= 1 
            while(lay[i-1] == 1):
                res.pop() 
                i-=1   
                  
    
    queue = []
    queue.append(s)   
    lis = []
    i = 0
    vlis = []
    f = False
    res = []
    count = 0
    while(len(queue)>0 ):
        parent = queue.pop(0)
        nodes = graph[parent]
        if parent == s:
            count += 1
            if count == 2:
                break
        if f == False and len(nodes) > 1:
            f = True 
        for node in nodes:
            queue.append(node)
            if  f ==1 and len(nodes) > 1:
                lis.append([node])
            elif f == 1 and len(nodes) ==1:
                lis[i%len(lis)].append(node)
                i= i+1
        vlis = [i for item in lis for i in item]
        for e in vlis:
            if vlis.count(e) == len(lis):
                f = False
                for l in lis:
                    res = res + l[:l.index(e)].copy()
                    
                path.append(res.copy())
                break
    return path
                
pth = findC(graph, 'U1')
print(pth)
               
R1 = Node(name = 'R1',R=10,I=5)
print(R1.U)
print(R1.P)        
            
# def getFormula():

# def getValue():

# def solveFormula():

        
                 
          

                
    
                


                        
                     
            

           

