class QueuUsingStack:
    def __init__(self):
        self.stack_enqueue=[]
        self.stack_dequeue=[]
    def enqueue(self, element):
        self.stack_enqueue.append(element)
    def dequeue(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        if self.stack_dequeue:
            return self.stack_dequeue.pop()
        else:
            return None
    def print_font(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
            if self.stack_dequeue:
                font_element = self.stack_dequeue[-1]
                print(font_element)
            else:
                print()
input_queries= input().split(',')
queue= QueuUsingStack()
for query in input_queries:
    query_type, *args = query.split()
    if query_type =='1':
        queue.enqueue(int(args[0]))
    elif query_type=='2':
        queue.dequeue()
    elif query_type == '3':
        queue.print_font()