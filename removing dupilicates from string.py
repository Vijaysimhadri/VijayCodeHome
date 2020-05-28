
st=input("enetr a string")
st1=""
for i in st:
    if i not in st1:
        st1=st1+i


print(st1[::-1])


