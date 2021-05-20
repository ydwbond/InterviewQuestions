from typing import Dict

ls = list(range(0, 10))


def add_a_number_to_list(lst: list, num: int = 1):
    for i in lst:
        lst[ i ] += num


print(ls)
print(id(ls))
add_a_number_to_list(ls, 10)
print(ls)
print(id(ls))

"""not do this"""
def func_with_default_mutable_value(orginal_list :list, lst: list = []):
    lst.append(1)
    orginal_list.append(lst)

func_with_default_mutable_value(ls)
print(ls)
func_with_default_mutable_value(ls, [1,2,3])
func_with_default_mutable_value(ls)

print(ls)
print(id(ls))


accounts: Dict[str, int] = {
    "checking": 0,
    "saving": 0
}

def add_transactions_to_account(amount:float,account_name:str = "checking" ):
    accounts[account_name] += amount
    for account in accounts:
        print(f"your {account} balance is {accounts.get(account)}")


trans = [
    (1000,'checking'),
    (1000,'saving'),
    (-189.1,'checking'),
    (-98.01,'checking'),
    (125.1,'checking'),
    (-99,'saving'),
    (-1000.0,'checking'),
    (98,'checking'),
]

for t in trans:
    add_transactions_to_account(t[0],t[1])

for t in trans:
    amount, acount = t
    print(amount)
    print(acount)
    add_transactions_to_account(*t)

for t in trans:
    add_transactions_to_account(*t)


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car make {self.make} and Model {self.model}>"


cars = [
    {"model": "Civic", "make": "Honda"},
    {"model": "Focus", "make": "Ford"},
    {"model": "Accord", "make": "Honda"},
]

car_objs = [Car(**car) for car in cars]
print(car_objs)









