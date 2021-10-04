class Queue_structure:
   def __init__(self):
      self.in_val = Stack_structure()
      self.out_val = Stack_structure()

   def check_empty(self):
      return (self.in_val.check_empty() and self.out_val.check_empty())

   def enqueue_operation(self, data):
      self.in_val.push_operation(data)

   def dequeue_operation(self):
      if self.out_val.check_empty():
         while not self.in_val.check_empty():
            deleted_val = self.in_val.pop_operation()
            self.out_val.push_operation(deleted_val)
      return self.out_val.pop_operation()

class Stack_structure:
   def __init__(self):
      self.items = []

   def check_empty(self):
      return self.items == []

   def push_operation(self, data):
      self.items.append(data)

   def pop_operation(self):
      return self.items.pop()

my_instance = Queue_structure()

while True:
   print('enqueue <value>')
   print('dequeue')
   print('quit')
   my_input = input('What operation would you like to perform ?').split()

   operation = my_input[0].strip().lower()
   if operation == 'enqueue':
      my_instance.enqueue_operation(int(my_input[1]))
   elif operation == 'dequeue':
      if my_instance.check_empty():
         print('The queue is empty')
      else:
         deleted_elem = my_instance.dequeue_operation()
         print('The deleted element is : ', int(deleted_elem))
   elif operation == 'quit':
      break
