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
    
    def instantiate_form_csv(self):
        pass
    
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"             


Item.instantiate_form_csv()
