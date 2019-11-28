class Queue:
    queue_limit = 3

    def __init__(self):
        self.__queue_list = []

    def enqueue(self, val):
        if len(self.__queue_list) < Queue.queue_limit:
            self.__queue_list.append(val)
            print(val, "inserted")
        else:
            print("Queue Overflow!")

    def dequeue(self):
        if len(self.__queue_list) > 0:
            val = self.__queue_list.pop(0)
            print(val, "deleted")
            return val
        else:
            print("Queue Empty!")

    def __call__(self):
        print(self.__queue_list)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(3)
q()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q()