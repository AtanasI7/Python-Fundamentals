meerkat = list()

meerkat.append(input())
meerkat.append(input())
meerkat.append(input())

meerkat[0], meerkat[-1] = meerkat[-1], meerkat[0]
print(meerkat)