a=[1,2,5,6]
b=a
print(f"a的地址为{id(a)}   b的地址为{id(b)}")
b=a[:]
print(f"a的地址为{id(a)} b 的地址为{id(b)}")
print(f"{id(a[0])}  {id(b[0])}")

