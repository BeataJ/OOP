import csv

class Item:
    pay_rate = 0.8 # the pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validations to the received argument
        assert price >= 0, f'Price {price} is not greater than or equal zero'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal zero'

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # Action to execute
        Item.all.append(self)
        
    @property
    def price(self):
        return self.__price 
       
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value    

    @property
    # Property Decoretor = Read-Only Attribute
    def name(self): 
        return self.__name
    
    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise Exception("The name is to long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity
    
    
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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"             

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone
        We have {self.name} {self.quantity} times.
        Regards, JimShapedCoding
        """ 
        
    def __send(self):
        pass       

    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()