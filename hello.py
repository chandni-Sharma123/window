def rv(str1):
	v = ""
	for c in str1:
		if c in "aeiouAEIOU":
			v += c
	rs= ""
	for c in str1:
		if c in "aeiouAEIOU":
			rs += v[-1]
			v = v[:-1]
		else:
			rs += c
	return rs
print(rv("hello"))
