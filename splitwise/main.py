from user import User
from group import Group
from transaction import Transaction



if __name__ == "__main__":
    # no_of_users = int(input("Enter no of users: "))
    # users = []
    # for i in range(no_of_users ):
    #     user_name = input("Enter user name: ")
    #     users.append(User(user_name))
    # group_name = input("Enter group name ")
    # group = Group(group_name, users)
    # no_of_transactions = int(input("Enter no of transactions: "))
    # transactions = []
    # for i in range(no_of_transactions ):
    #     transaction_name = input("Enter transaction name ")
    #     amount_paid = int(input("Enter amount: "))
    #     amount_paid_by = input("Enter amount paid by: ")
    #     amount_paid_to = input("Enter amount paid to(comma seperated): ")
    #     transaction_type = input("Enter transaction type ")
    #     transactions.append((transaction_name, amount_paid, amount_paid_by, amount_paid_to, transaction_type))
    
    
    no_of_users = 3
    users = []
    
    users.extend([User("a"), User("b"), User("c")])
    group = Group("group_name", users)
    no_of_transactions = 3
    transactions = []
    
    transactions.append(("transaction_name", 10, "a", "b", "t"))
    transactions.append(("transaction_name", 20, "b", "a", "t"))
    transactions.append(("transaction_name", 10, "a", "c", "t"))
    
    
    
    
    
    group.add_group_transactions(transactions)
    group.print_transactions()
    group.print_amount_left_to_be_paid()
        