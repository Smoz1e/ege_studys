i = 1789456123-1000000000
c = (i-i%16)//16*6+1+[0, 1+[0, 1+[0, 1+[0, 1][i%16>10]][i%16>9]][i%16>7]][i%16>2]
print(c, i%16)
