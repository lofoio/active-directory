def Triangle2D3Node_Stiffness(E,NU,thick,ID,ic,celdes,xyz):
    """
    弹性模量 E,泊松比 NU,厚度 thick
    三个节点 i、j、k 的坐标 xi,yi,xj,yj,xk,yk
    平面问题性质指示参数 ID(1 为平面应力,2 为平面应变)
    """
    i,j,k = celdes[ic]
    xi,yi = xyz[i]
    xj,yj = xyz[j]
    xk,yk = xyz[k]
    A = (xi*(yj-yk) + xj*(yk-yi) + xk*(yi-yj))/2.0
    betai = yj-yk
    betaj = yk-yi
    betam = yi-yj
    gammai = xk-xj
    gammaj = xi-xk
    gammak = xj-xi
    B = matrix(RR,3,6,[betai,0,betaj,0,betam,0,
                       0,gammai,0,gammaj,0,gammak,
                       gammai,betai,gammaj,betaj,gammak,betam])/(2*A)
    if ID == 1:
        D = (E/(1-NU*NU))*matrix(RR,3,3,[1,NU,0,
                                         NU,1,0,
                                         0,0,(1-NU)/2])
    elif ID == 2:
        D = (E/(1+NU)/(1-2*NU))*matrix(RR,3,3,[1-NU,NU,0,
                                               NU,1-NU,0,
                                               0,0,(1-2*NU)/2])
    return thick*A*B.transpose()*D*B

def Assembly(dof,KK,k,ns):
    noe = len(ns)
    for a in range(noe):
        for b in range(noe):
            l  = a*dof
            ll = ns[a]*dof
            r  = b*dof
            rr = ns[b]*dof
            for i in range(dof):
                for j in range(dof):
                    KK[ll+i,rr+j] += k[l+i,r+j]

def bcsolver(dof,bcsf):
    ns = []
    ps = []
    for t in bcsf:
        tt = (len(t)-1)/2
        for i in range(tt):
            if t[i*dof+1] == "x":
                n = int(t[0])*dof
                p = t[i*dof+2]
            elif t[i*dof+1] == "y":
                n = int(t[0])*dof+1
                p = t[i*dof+2]
            ns.append(n)
            ps.append(float(p))
    return ns, ps

with open("tri.txt", 'r') as infile:
    cells,nodes,bcs = [int(x) for x in infile.readline().split()]
    celdes = []
    xyz    = []
    bcsf   = []
    for i in range(cells):
        celdes += [[int(x)-1 for x in infile.readline().split()]]
    for i in range(nodes):
        xyz += [[float(x) for x in infile.readline().split()]]
    for i in range(bcs):
        bcsf += [infile.readline().split()]
    dof = int(infile.readline().split()[1])
    thick = float(infile.readline().split()[1])
    E = float(infile.readline().split()[1])
    NU = float(infile.readline().split()[1])

KK = matrix(RR,dof*nodes,dof*nodes)

for i in range(cells):
    k = Triangle2D3Node_Stiffness(E,NU,thick,1,i,celdes,xyz)
    Assembly(dof,KK,k,celdes[i])

sub_k,sub_p = bcsolver(dof,bcsf)
KKs = KK.matrix_from_rows_and_columns(sub_k,sub_k)
sub_u = vector(sub_p)/KKs
U = [0.0]*nodes*dof
for i in range(len(sub_k)):
    U[sub_k[i]]=sub_u[i]
P = KK*vector(U)
## no need to transpose vectors
energy = 0.5*vector(U)*KK*vector(U)
work = vector(U)*P
poten = energy - work
