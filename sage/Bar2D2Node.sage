def Bar2D2Node_Stiffness(E,A,x1,y1,x2,y2,alpha):
    L = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    alpha = alpha*pi/180
    C=cos(alpha)
    S=sin(alpha)
    return E*A/L*matrix(4,4,(C*C,C*S,-C*C,-C*S,
                             C*S,S*S,-C*S,-S*S,
                             -C*C,-C*S,C*C,C*S,
                             -C*S,-S*S,C*S,S*S))

def Bar2D2Node_Assembly(KK,k,n1,n2):
    for i in range(2):
        for j in range(2):
            KK[2*n1+i,2*n1+j] += k[i,j]
            KK[2*n1+i,2*n2+j] += k[i,2+j]
            KK[2*n2+i,2*n1+j] += k[2+i,j]
            KK[2*n2+i,2*n2+j] += k[2+i,2+j]

def Bar2D2Node_Forces():
    pass

nodes = 4
E=2.95e11
A=0.0001
x1=0
y1=0
x2=0.4
y2=0
x3=0.4
y3=0.3
x4=0
y4=0.3
alpha1=0
alpha2=90
alpha3=atan(0.75)*180/pi
k1=Bar2D2Node_Stiffness(E,A,x1,y1,x2,y2,alpha1)
k2=Bar2D2Node_Stiffness(E,A,x2,y2,x3,y3,alpha2)
k3=Bar2D2Node_Stiffness(E,A,x1,y1,x3,y3,alpha3)
k4=Bar2D2Node_Stiffness(E,A,x4,y4,x3,y3,alpha1)

KK = matrix(RR,2*nodes,2*nodes)
Bar2D2Node_Assembly(KK,k1,0,1)
Bar2D2Node_Assembly(KK,k2,1,2)
Bar2D2Node_Assembly(KK,k3,0,2)
Bar2D2Node_Assembly(KK,k4,3,2)
var('u1,v1,u2,v2,u3,v3,u4,v4', domain=RR)
var('Rx1,Ry1,Rx2,Ry2,Rx3,Ry3,Rx4,Ry4', domain=RR)
Rx2=2e4
Rx3, Ry3 = 0.0, -2.5e4
u1 = v1 = v2 = u4 = v4 = 0.0
KKs = KK.matrix_from_rows_and_columns([2,4,5],[2,4,5])
Ps = vector([Rx2,Rx3,Ry3])
u2,u3,v3 = Ps/KKs
q = vector([u1,v1,u2,v2,u3,v3,u4,v4])
P = KK*q
