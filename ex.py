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


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
        # Call to super function to have to all attributes / method
        super().__init__(
            name, price, quantity
        )
        
        # Run validations to the received argument
        assert broken_phones >= 0, f'Broken Phones {broken_phones} is not greater than or equal zero'


        # Assign to self object
        self.broken_phones = broken_phones
        
        
        def __repr__(self) -> str:
            return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.broken_phones})" 

phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)

# Item.instantiate_form_csv()
print(Item.all)


