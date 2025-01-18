class Invoice:
    def __init__(self, id=None, tax_number = None, vendor_address=None, vendor_phone=None, date = None,customer_name = None, customer_address=None, payment_method=None):
        self.id = id
        self.tax_number = tax_number
        self.vendor_address = vendor_address
        self.vendor_phone = vendor_phone
        self.date = date
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.payment_method = payment_method

