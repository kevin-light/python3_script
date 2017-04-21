# str1 = """ABCaABCbABC1"""
# countA = 0
# countB = 0
# countC = 0
# length = len(str1)
# for i in range(length):
#     if str1[i] == '\n':
#         continue
# if str1[i].isupper():
#     if countB:
#         countC +=1
#     else:
#         countC=0
#         countA += 1
# if str1[i].islower():
#     if countA!=3:
#         countA = 0
#         countB = 0
#         countC = 0
#     else:
#         if countB:
#             countA = 0
#             countB = 0
#             countC = 0
#         else:
#             countB = 1
#             countC = 0
#             target = i
# if countA == 3 and countC == 3:
#     if i+1 != length and str1[i+1].isupper():
#         countA = 0
#         countB = 0
#         countC = 0
#     else:
#         print(str1[target],end='')
#         countA = 3
#         countB = 0
#         countC = 0


def comp():
    file1 = input('please enter first name:')
    file2 = input('please enter second name:')
    f1 = open(file1)
    f2 = open(file2)
    count = 0
    differ = []
    for line1 in f1:
        line2 = f2.readline()
        if line1 != line2:
            count += 1
            differ.append(count)
        if len(differ)==0:
            print('two files are same')
        else:
            print('there %d:places'% len(differ))
            for each in differ:
                print('at %d' % each)
print(comp())