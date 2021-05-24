from collections import deque

def count_down(n):
    while n>0:
        yield n
        n-= 1

c1 = count_down(10)
c2 = count_down(20)
print(next(c1))
print(next(c2))
print(next(c1))
print(next(c2))
print(next(c1))

print('=======================================')
#task schelduler
tasks = [count_down(10), count_down(5), count_down(20)]
while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        print(next(task))
        tasks.append(task)
    except StopIteration:
        print("task stopped")

print('=======================================')
task_queue = deque()
task_queue.appendleft(count_down(20))
task_queue.appendleft(count_down(5))
task_queue.appendleft(count_down(10))




while task_queue:
    task = task_queue.popleft()
    try:
        print(next(task))
        task_queue.append(task)
    except StopIteration:
        print("task finished")


print('This part is to yield from another iterator')

# to construct an interator using deque

friends = deque(("Tom","Tim","Jim","Sam"))

def get_friend():
    yield from friends

def greeting_friend(g):
    while True:
        try:
            friend = next(g)
            yield f"Hello {friend}"
        except StopIteration:
            raise ("friend list finish")

f_g = get_friend()
print(next(f_g))
print(next(greeting_friend(f_g)))
print(next(greeting_friend(f_g)))
print(next(greeting_friend(f_g)))
print(next(greeting_friend(f_g)))
print(next(greeting_friend(f_g)))























