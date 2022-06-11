
class Transaction:
  
  def __init__(self, transaction_name, amount, paid_by, paid_to, type):
    self.transaction_name = transaction_name
    self.amount = amount
    self.paid_by = paid_by
    self.paid_to = paid_to
    self.type = type