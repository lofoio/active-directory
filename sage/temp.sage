# 用节点插值单元。
def Quad2D4Node_Stiffness(E,NU,thick,ID,ic,celdes,xyz):
    """弹性模量 E,泊松比 NU,厚度 h
     4 个节点 i、j、m、p 的坐标 xi,yi,xj,yj,xm,ym,xp,yp
    平面问题性质指示参数 ID(1 为平面应力,2 为平面应变)
    单元刚度矩阵 k(8X8)"""
    i,j,k,l = celdes[ic]
    xi,yi = xyz[i]
    xj,yj = xyz[j]
    xk,yk = xyz[k]
    xp,yp = xyz[l]
    ks = [1,-1,-1,1]
    yt = [1,1,-1,-1]
    a = 0.5*abs(xi-xj)
    b = 0.5*abs(yj-yk)
    noe = len(celdes[ic])
    ents = []
    for r in range(noe):
        for s in range(noe):
            krs = ks[r]*ks[s]
            yrs = yt[r]*yt[s]
            k1 = b*b*krs*(1+yrs/3.)+(1-NU)*0.5*a*a*yrs*(1+krs/3.)
            k2 = a*b*(NU*yt[r]*ks[s]+(1-NU)*0.5*ks[r]*yt[s])
            k3 = a*b*(NU*yt[s]*ks[r]+(1-NU)*0.5*ks[s]*yt[r])
            k4 = a*a*yrs*(1+krs/3.)+(1-NU)*0.5*b*b*krs*(1+yrs/3.)
            ents.append(matrix(RR,2,2,[k1,k2,k3,k4])*E*thick*0.25/((1-NU*NU)*a*b))
    return block_matrix(4,4,ents)

def Rect2D4Node_Stiffness(E,NU,thick,ID,ic,celdes,xyz):
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

with open("quad.txt", 'r') as infile:
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
k = Quad2D4Node_Stiffness(E,NU,thick,1,0,celdes,xyz)
# for i in range(cells):
#     k = Triangle2D3Node_Stiffness(E,NU,thick,1,i,celdes,xyz)
#     Assembly(dof,KK,k,celdes[i])

# sub_k,sub_p = bcsolver(dof,bcsf)
# KKs = KK.matrix_from_rows_and_columns(sub_k,sub_k)
# sub_u = vector(sub_p)/KKs
# U = [0.0]*nodes*dof
# for i in range(len(sub_k)):
#     U[sub_k[i]]=sub_u[i]
# P = KK*vector(U)
# ## no need to transpose vectors
# energy = 0.5*vector(U)*KK*vector(U)
# work = vector(U)*P
# poten = energy - work
