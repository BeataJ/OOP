from item import Item

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