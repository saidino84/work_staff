class Tranferencia:
    
    def __init__(self, 
                number,
                date,
                subtotal,
                parcents,
                total,
                destin,
                user,
                description,
                state=0
                ):
        self.number=number
        self.date=date
        self.subtotal=subtotal
        self.parcents=parcents
        self.total=total
        self.destin=destin
        self.user=user
        self.description=description
        self.state=state

    def __repr__(self)->str:
        return f"N:{self.number},"
def get_tranference_as_list(self):
    return list(self)
