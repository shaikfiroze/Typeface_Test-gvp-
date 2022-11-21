
def Base3Number(N):
	

	if (N == 0):
		return

	x = N % 3
	N //= 3
	if (x < 0):
		N += 1


	Base3Number(N);

	if (x < 0):
		print(x + (3 * -1), end = "")
	else:
		print(x, end = "")


def convert(D):
	
	print("Base 3 number of ", D,
		" is: ", end = "");


	if (D != 0):
		Base3Number(D);
	else:
		print("0", end = "")
t=int(input())
convert(t)
