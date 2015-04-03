def wascally(n,k):
	F = [0]*(n+1)
	F[0] = 0
	F[1] = 1
	for x in range(2,n+1): F[x] = (k*F[x-2]) + F[x-1] 
	return F[n]

print wascally(33,4)
