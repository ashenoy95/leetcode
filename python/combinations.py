k = 2
n = 4
l = [i for i in range(1,n+1)]
final = []

def perm(prefix, l, ctr, final):
	if not ctr:
		final.append(prefix)
		print(final)
		return final
	for i in range(len(l)):
		perm(prefix+[l[i]], l[i+1:], ctr-1, final)

perm([], l, k, [])
