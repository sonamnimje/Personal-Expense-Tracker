class Expense:
     
     def __init__(self, name, category, amount) -> None:
         self.name = name
         self.category = category
         self.amount = amount
 
     def __repr__(self) -> str:
         return f"{self.name} (${self.amount:.2f})"
     def __repr__(self):
         return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"
