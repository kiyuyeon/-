# # %%
# katok = ["다현","정현","쯔위","사나","지효"]
# # %%
# print(katok)
# print(katok[0])
# print(katok[4])

# # %%
# katok.append(None)
# print(katok)

# #%%
# katok[5] = "모모"
# print(katok)

# # %%
# katok.append(None)
# print(katok)

# #%%
# katok[6] = katok[5]
# katok[5] = None
# print(katok)

# #%%
# katok[4] = None
# katok[4] = katok[3]
# katok[3] = None
# print(katok)

# #%%
# katok[3] = "미나"
# print(katok)

# #%%
# katok = ["다현","정현","쯔위","사나","지효"]


# def delete_data(position):
#     if position < 0 or position > len(katok):
#         print("데이터를 삭제할 범위를 벗어났습니다.")
#         return

# kLen = len(katok)
# katok[position] = None

# for i in range(position+1,kLen):
#     katok[i-1] = katok[i]
#     katok[i] = None

# del(katok[kLen-1])
# # %%
# katok2 = []
# katok2.append(None)
# 배열길이 = len(katok2)
# katok2[배열길이-1] = "다현"
# print(katok2)

# #%%

# katok3 = []

# def add_data(friend):
#     katok3.append(None)
#     kLen = len(katok3)
#     katok3[kLen-1] = friend

# add_data('다현')
# add_data('정연')
# add_data('쯔위')
# add_data('사나')
# add_data('지효')

# print(katok3)
# # %%

# katok4 = ["다현","정연","쯔위","사나","지효"]

# def insert_data(position,friend):
    
#     if position<0 or position >len(katok4):    
#         print("데이터를 삽입할 범위를 벗어났습니다.")
#         return

#     katok4.append(None)
#     kLen = len(katok4)
    
#     for i in range(kLen-1,position-1):
#         katok4[i]= katok4[i-1]
#         katok4[i-1] = None
        
#     katok4[position] = friend
    
# insert_data(2, '솔라')
# print(katok4)

# insert_data(6, '문별')
# print(katok4)
# # %%
#%%
katok4 = ["다현","정연","쯔위","사나","지효"]

def delete_data(position):
    
    if position < 0 or position > len(katok4):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return
        
    kLen = len(katok4)
    katok4[position] = None
        
    for i in range(position+1, kLen):
        katok4[i-1] = katok4[i]
        katok4[i] = None
            
    del(katok4[kLen-1])
        
delete_data(1)
print(katok4)
delete_data(3)
print(katok4)
# %%
