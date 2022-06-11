
from transaction import Transaction

class Group:
    
    def __init__(self, name, users):
      self.name = name
      self.users = users
      self.transactions = []
      self.group_amount_matrix = [[0 for __ in range(len(self.users))] for _ in range(len(self.users))]
      
            
    def get_user_by_id(self, id):
        if id < len(self.users):
            return self.users[id]
        
            
    def get_user_by_name(self, name):
        for u in self.users:
            if u.name == name:
                return u
    
    def add_group_transactions(self, transactions):
        for transaction in transactions:
            transaction_name, amount_paid, amount_paid_by, amount_paid_to, transaction_type = transaction[0], transaction[1], transaction[2], transaction[3], transaction[4]
            self.transactions.append(Transaction(transaction_name, amount_paid, self.get_user_by_name(amount_paid_by).id, [self.get_user_by_name(name).id for name in amount_paid_to.split(",")], transaction_type))
            for paid_to in self.transactions[-1].paid_to:
                payee_id = self.get_user_by_name(amount_paid_by).id
                # so that data is stored only in upper diagonal matrix
                if paid_to > payee_id:
                    self.group_amount_matrix[payee_id][paid_to] += amount_paid
                else:
                    self.group_amount_matrix[paid_to][payee_id] -= amount_paid
    
            
            
    def print_transactions(self):
        for t in self.transactions:
            # print(t.__dict__)
            for paid_to in t.paid_to:
                print(f"{t.amount} paid by {self.get_user_by_id(t.paid_by).name} to {self.get_user_by_id(paid_to).name}")
                
        print("-------------------------------")
            
    def print_amount_left_to_be_paid(self):
        for i in range(len(self.users)-1):
            for j in range(i+1, len(self.users)):
                if self.group_amount_matrix[i][j] == 0:
                    continue
                elif self.group_amount_matrix[i][j] < 0:
                    print(f"{-self.group_amount_matrix[i][j]} to be paid by {self.get_user_by_id(i).name} to {self.get_user_by_id(j).name}")
                else:
                    print(f"{self.group_amount_matrix[i][j]} to be paid by {self.get_user_by_id(j).name} to {self.get_user_by_id(i).name}")
            
            
