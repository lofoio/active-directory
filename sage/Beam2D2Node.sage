def Beam2D2Node_Stiffness(E,I,A,L,alpha):
    a = E*A/L
    b = E*I/(L*L*L)
    b12 = 12*b
    b6 = 6*b*L
    b2 = 2*b*L*L
    b4 = 2*b2
    alpha = alpha*pi/180
    C=cos(alpha)
    S=sin(alpha)
    Te = matrix(RR,6,6,(C,S,0,0,0,0,
                        -S,C,0,0,0,0,
                        0,0,1,0,0,0,
                        0,0,0,C,S,0,
                        0,0,0,-S,C,0,
                        0,0,0,0,0,1))
    Ke = matrix(RR,6,6,(a,0,0,-a,0,0,
                        0,b12,b6,0,-b12,b6,
                        0,b6,b4,0,-b6,b2,
                        -a,0,0,a,0,0,
                        0,-b12,-b6,0,b12,-b6,
                        0,b6,b2,0,-b6,b4))
    return Te.transpose()*Ke*Te

def Beam2D2Node_Assembly(KK,k,n1,n2):
    for i in range(3):
        for j in range(3):
            KK[3*n1+i,3*n1+j] += k[i,j]
            KK[3*n1+i,3*n2+j] += k[i,3+j]
            KK[3*n2+i,3*n1+j] += k[3+i,j]
            KK[3*n2+i,3*n2+j] += k[3+i,3+j]

nodes = 4
dof = 3
E=3.0e11
I=6.5e-7
A=6.8e-4
alpha1=0.0
alpha2=90.0
alpha3=90.0
L1=1.44
L2=0.96
k1=Beam2D2Node_Stiffness(E,I,A,L1,alpha1)
k2=Beam2D2Node_Stiffness(E,I,A,L2,alpha2)

KK = matrix(RR,dof*nodes,dof*nodes)
Beam2D2Node_Assembly(KK,k1,0,1)
Beam2D2Node_Assembly(KK,k2,2,0)
Beam2D2Node_Assembly(KK,k2,3,1)
KKs = KK.submatrix(0,0,6,6)

var('u1,v1,st1,u2,v2,st2,u3,v3,st3,u4,v4,st4', domain=RR)
var('Rx1,Ry1,M1,Rx2,Ry2,M2,Rx3,Ry3,M3,Rx4,Ry4,M4', domain=RR)
Rx1,Ry1,M1,Rx2,Ry2,M2 = 3.e3,-3.e3,-720,0,-3.e3,720
Ps = vector([Rx1,Ry1,M1,Rx2,Ry2,M2])
u1,v1,st1,u2,v2,st2 = Ps/KKs
