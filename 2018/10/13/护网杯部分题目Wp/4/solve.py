import os
def xor(a,b):
    assert len(a)==len(b)
    c=""
    for i in range(len(a)):
        c+=chr(ord(a[i])^ord(b[i]))
    return c
def round(M,K):
    L=M[0:27]
    R=M[27:54]
    new_l=R
    new_r=xor(xor(R,L),K)
    return new_l+new_r
def ReRound(M,K):
    L=M[0:27]#new_l
    R=M[27:54]#new_r
    k=xor(xor(L,),R)
    return k
def fez(m,K):
    for i in K:
        m=round(m,i)
    return m
a = "c8b84d08e5a8e60a49578f387fff5a90e9e7c181734bf05be4f5403c9ea24a0b8741a329991637e11fa69019cd3b01d7c95b65f5abd5"
b = "5c3660c27cb9b3785a5ce06022e88bc831017e882d39475ea85d919ad9e5ac498f86c553216cab1f8f7468353d46ba8971efa9ca8c81"
c = "519ab6fc0e435da00516b844f8fe664bfe9445992f478dc650701739a11ffda5bbeb643159d7e8cd03a2104c798a1ca734b905ee6c76"
r = []
r.append("R1")
l = []
l.append("L1")
for i in range(1,8):
	r.append(r[i-1] + "^K" + str(i) + "^" + l[i-1])
	l.append(r[i-1])
for i in range(1,8):
	print("R:"+r[i],"L:"+l[i])
