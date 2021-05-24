import functools
import time
import random

use_1 = {"id":"Tom","access_level":"admin"}
use_2 = {"id":"Jim","access_level":"user"}
use_3 = {"id":"Tim","access_level":"guest"}
use_4 = {"id":"Tim","access_level":None}
use_5 = {}


print("=============simple decorator=====================")
def caculate_fucntion_time(func):
    @functools.wraps(func)
    def wrapper_func():
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__} took {end-start} seconds")
    return wrapper_func

@caculate_fucntion_time
def login():
    time.sleep(random.random())
    print("log in successfully")


@caculate_fucntion_time
def load_data():
    time.sleep(random.random())
    print("load data successfully")

login()
load_data()

print("=============decorator with parameters =====================")
def check_user_in_role(access_level):
    def OuterReturn(func):
        @functools.wraps(func)
        def wrapper():
            print(f"check if user in {access_level}")
            func()
            print("done")
        return wrapper
    return OuterReturn


@check_user_in_role('admin')
def print_user_role():
    print(f"{use_1.get('id')}, role {use_1.get('access_level')}")


print_user_role()


def check_user_permission(user):
    def check_permission(func):
        @functools.wraps(func)
        def wrapper_func():
            if user.get("access_level") is not None:
                print(f"user {user.get('id')} has permission to the application")
                func()
            else:
                print(f"user {user.get('id')} does not have permission to the application")
        return wrapper_func
    return check_permission

@check_user_permission(user=use_4)
def view_data():
    print("Here is the data")

view_data()

print("""
for the above decorators with parameter does not really make sense to me,
but we will see if in the futures there are more good exmpales
""")


print("===========================functions with n numbers of parameters======================")


def print_function(*args, **kwargs):
    print(args,kwargs)

print_function()
print("1","2","3")
print(use_1)


def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} takes {end-start} seconds")
    return wrapper

@timer
def delete_data(id):
    time.sleep(random.random())
    print(f"{id} was deleted")

@timer
def displayUser(user):
    time.sleep(random.random())
    print(f"user {user.get('id')} access level {user.get('access_level')}")

delete_data(2)
displayUser(use_2)

@timer
def add_user(id, access_level):
    time.sleep(random.random())
    print(f"user {id} access level {access_level} was added")

add_user("JILL", "Admin")

#
#
#
# def user_has_permission(user):
#     def check_user_permission(func):
#         @functools.wraps(func)
#         def wrapper_func(user):
#             if user.get("access_level") is not None:
#                 func(user)
#             else:
#                 print(f"{user['id']} does not have access to the application")
#         return wrapper_func
#     return check_user_permission
#
# @user_has_permission(use_5)
# def do_some_admin_work(user):
#     print(f"user {user['id']} performed some action ")
#
# do_some_admin_work(use_2)