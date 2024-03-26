
def buscar_u_elemento(list, data):
    try:
        list.reverse()
        return len(list) - list.index(data) - 1
    except ValueError:
        return -1


print(buscar_u_elemento([1,2,3,2,3,4],1))
print(buscar_u_elemento([1,2,3,2,3,4],2))
print(buscar_u_elemento([1,2,3,2,3,4],3))
print(buscar_u_elemento([1,2,3,2,3,4],5))
