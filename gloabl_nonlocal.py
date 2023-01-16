# global_var = "전역 변수"

# def outer():
#     nonlocal_var = "비전역 변수"
#     print(global_var) # 가능
#     print(nonlocal_var) # 가능

#     def inner():
#         local_var = "지역 변수"
#         print(global_var) # 가능
#         print(nonlocal_var) # 가능
#         print(local_var) # 가능

    # print(local_var) # 불가능 (NameError: name 'local_var' is not defined)

# print(nonlocal_var) # 불가능 (NameError: name 'nonlocal_var' is not defined)
# print(local_var) # 불가능 (NameError: name 'local_var' is not defined)


# 선언된 3개의 var이 서로 다른변수이다.
# 이러한 현상을 variable shadowing이라고 부른다. 
# 외부에서 선언된 변수가 내부에서 같은 이름으로 선언된 변수에 가려지는 현상
var = "전역 변수"

def outer():
    var = "비지역 변수"
    print(var)
    
    def inner():
        var = "지역 변수"
        print(var)

    inner()
    print(var)

print(var)
outer()
print(var)


# # 동일한 이름의 변수를 바꿔주기 위해서는 global 키워드로 전역변수를 가져와야함
# num = 0

# def chnage_num():
#     global num
#     num = 100
#     print(num)

# chnage_num()

# print(num)


# # local 내에서는 nonlocal 키워드를 사용해서 값을 업데이트 할 수 있음
# def print_nums():
#     num = 0

#     def change_num():
#         nonlocal num
#         num = 100
#         print(num)

#     change_num()

#     print(num)

# print_nums()