import csv

class Item:
    pay_rate = 0.8 # the pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validations to the received argument
        assert price >= 0, f'Price {price} is not greater than or equal zero'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal zero'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_form_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in  items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),              
            ) 
     
    @staticmethod        
    def is_integer(num):
        if isinstance(num, float):
           return num.is_integer() 
        elif isinstance(num, int):
            return True
        else:
            return False      
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"             
