from constants import *
def user_name() :
    user_n = input(names)
    if user_n == "0" :
       print(global_info)
    else :
        n = global_info.get("name")
        n.append(user_n)
        global_info.update(name = n)
        user_a = int(input(ages))
        a = global_info.get("age")
        a.append(user_a)
        global_info.update(age = a)
        user_s=input(sexes)
        s = global_info.get("sex")
        s.append(user_s)
        global_info.update(sex = s)
        print(global_info)
    return user_n
def del_it() :
    ind = int(input("Выбери индекс пользователя хочешь удалить из нашей базы, заметь что индексация начинается с 0"))
    l = global_info.get("name")
    l.pop(ind)
    u = global_info.get("age")
    u.pop(ind)
    f = global_info.get("sex")
    f.pop(ind)
    print(global_info )