from app.helpers.logger import logger
from app.repositories.bill_repository import create, update, read, delete
from app.helpers.response import Response
from app.repositories.bill_repository import Bill

logger.announcement('Initializing Bill Service', 'info')
logger.announcement('Bill Service initialized', 'success')

class BillService:
    def __init__(self):
        pass

    # Create a new bill
    def create(self, bill: Bill):
        response = create(data=bill)
        return Response.success(response)

    # Update an existing bill
    def updateBill(self, billID: str, updatedBill: Bill):
        # Assumed that 'update' expects a dictionary of fields
        response = update(params={"id": billID}, data=updatedBill.__dict__)
        return response

    # Delete a bill by ID
    def deleteBill(self, billID: str):
        response = delete(params={"id": billID})
        return response

    # Schedule a bill reminder (set priority)
    def scheduleBillReminder(self, billID: str, highPriority: bool):
        # Placeholder for actual scheduling logic
        return Response.success('Bill reminder scheduled successfully')

    # Process a bill payment
    def processBillPayment(self, billID: str):
        # Placeholder for actual payment processing logic
        return Response.success('Bill payment processed successfully')

    # Retrieve all bills
    def findAll(self):
        return Response.success(read())
