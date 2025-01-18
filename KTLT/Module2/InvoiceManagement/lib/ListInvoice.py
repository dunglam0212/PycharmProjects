from Module2.InvoiceManagement.lib.Invoice import Invoice


class ListInvoice:
    def __init__(self):
        self.listinvoices = []
    def add_invoice(self):
        self.listinvoices.append(Invoice())
