# rlist = ["","","",5,"","",48,"",16]
# print(rlist)

# unsortedrlist = rlist
# for i in range(1,unsortedrlist.count("")+1):
#     unsortedrlist.remove("")


# sortedrlist = unsortedrlist
# sortedrlist.sort()
# print(unsortedrlist)
# print(sortedrlist)

# print(sortedrlist==unsortedrlist)
# print(rlist)

# rlist = ["","","",5,"","",48,"",16]
# print(rlist)

# unsortedrlist = rlist
# for i in range(1,unsortedrlist.count("")+1):
#     unsortedrlist.remove("")

# print(f'unsortedrlist (before .sort()): {unsortedrlist}')

# sortedrlist = unsortedrlist
# sortedrlist.sort()

# print(f'sortedrlist: {sortedrlist}')
# print(f'unsortedrlist (after .sort()): {unsortedrlist}')


# print(sortedrlist==unsortedrlist)

# Scenario 1
# rlist = ["","","",5,"","",48,"",16]

# Scenario 2
# rlist = ["","","",5,"","",16,"",48]

# print(f"rlist at the start: {rlist}")

# unsortedrlist = rlist.copy()

# print(f"unsortedrlist & rlist point to same list: {hex(id(unsortedrlist)) == hex(id(rlist))}")
# print(f"unsortedrlist & rlist have same positional content: {unsortedrlist == rlist}")
# for i in range(1,unsortedrlist.count("")+1):
#     unsortedrlist.remove("")

# print(f"unsortedrlist (before .sort()): {unsortedrlist}")

# # returns a new list no matter what
# sortedrlist = sorted(unsortedrlist)

# print(f"sortedrlist: {sortedrlist}")
# print(f"unsortedrlist (after .sort()): {unsortedrlist}")

# print(f"sortedrlist & unsortedrlist point to same list: {hex(id(unsortedrlist)) == hex(id(sortedrlist))}")
# print(f"sortedrlist & unsortedrlist have same content: {sortedrlist==unsortedrlist}")
# print(f"rlist at the end: {rlist}")

import random

logn=[501]
c=0 #conditional to start while loop
while c<21:
    generated_number = random.randint(1,1000)
    logn.append(generated_number)
    logn_sorted=logn.copy()
    logn_sorted.sort()
    c=c+1
    print("unsorted: "+str(logn))
    print("sorted: "+str(logn_sorted))
    print("Same order: "+str(logn==logn_sorted))
    c += 1