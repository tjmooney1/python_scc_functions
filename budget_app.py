class Category:
  def __init__(self, category):
      # initialize a new budget category with a given name
      self.category = category
      # initialize an empty ledger list to store transactions
      self.ledger = []

  def deposit(self, amount, description=""):
      # add a deposit to the ledger
      self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
      # withdraw funds and add the transaction to the ledger
      if self.check_funds(amount):
          self.ledger.append({"amount": -amount, "description": description})
          return True
      return False

  def get_balance(self):
      # calculate the current balance of the budget category
      return sum(item["amount"] for item in self.ledger)

  def transfer(self, amount, budget_category):
      # transfer funds between two budget categories
      if self.check_funds(amount):
          self.withdraw(amount, f"Transfer to {budget_category.category}")
          budget_category.deposit(amount, f"Transfer from {self.category}")
          return True
      return False

  def check_funds(self, amount):
      # check if there are enough funds for a withdrawal or transfer
      return amount <= self.get_balance()

  def __str__(self):
      # customize the string representation of the category for printing
      title = f"{self.category:*^30}\n"
      items = "".join(
          f"{item['description'][:23]:23}{item['amount']:>7.2f}\n" for item in self.ledger
      )
      total = f"Total: {self.get_balance():.2f}"
      return title + items + total


def create_spend_chart(categories):
  chart = "Percentage spent by category\n"
  # calculate total spent in each category
  spendings = [sum(item["amount"] for item in category.ledger if item["amount"] < 0) for category in categories]
  total_spent = sum(spendings)

  # build the chart row by row
  for i in range(100, -1, -10):
      chart += f"{i:3}| "
      for spending in spendings:
          chart += "o" if spending >= i * total_spent / 100 else " "
      chart += " \n"

  # add the horizontal line below the bars
  chart += "    -" + "---" * len(categories) + "\n"

  # add the category names below the chart
  max_name_length = max(len(category.category) for category in categories)
  for i in range(max_name_length):
      chart += "     "
      for category in categories:
          chart += category.category[i] if i < len(category.category) else " "
          chart += "  "
      chart += "\n"

  return chart.rstrip("\n")
