s_id2=[(1,), (2,), (3,), (5,), (6,)]
out = [item for t in s_id2 for item in t]
# num = [1, 2, 3, 4, 5, 6]
print(out)
s_id = int(input("enter st_id to search:- "))
# print(s_id)
# s_id3=tuple(s_id)
check=s_id in out
print(check)

# tup = [(1, 2), (3, 4), (5, 6)]
#
# # result list initialization
# result = []
#
# for t in tup:
#     for x in t:
#         print(x)
#         result.append(x)
# # printing output
# print(result)


# dict = {"Ram": 23, "Suraj": 25, "Sakshi": 27, "Sonya": 30}
# for x in dict:
#     print(dict[x])
# list_1 = [x.upper () for x in dict if dict [x] > 25]
#
# print (list_1)