
import uuid


class User:
    class_counter = 0
    def __init__(self, name):
      self.name = name
      self.id = User.class_counter
      User.class_counter += 1
      
      
    
    