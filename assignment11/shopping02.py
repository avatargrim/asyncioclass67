import time
import asyncio
from asyncio import Queue
from random import randrange

# we first implement the Customer and Product classes, 
# representing customers and products that need to be checked out. 
# The Product class has a checkout_time attribute, 
# which represents the time required for checking out the product.
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_number: int):
    count=0
    Cashier_time=0
    while not queue.empty():
        customer: Customer = await queue.get()
        count+=1
        print(f"The Cashiert_{cashier_number} "
              f"will checkout Customer_{customer.customer_id}")
        await asyncio.sleep(0)
        for product in customer.products:
            Cashier_time+=product.checkout_time
            print(f"The Chasier_{cashier_number} "
                  f"will checkout Customer_{customer.customer_id}'s "
                  f"Product_{product.product_name} "
                  f"in {product.checkout_time} secs")
            await asyncio.sleep(product.checkout_time)
        print(f"The Chasier_{cashier_number} "
              f"finished checkout Customer_{customer.customer_id} ")
        queue.task_done()
    return (f"cashier{cashier_number} take {count}customers in {Cashier_time} sec")
# we implement the generate_customer method as a factory method for producing customers.
#
# We first define a product series and the required checkout time for each product. 
# Then, we place 0 to 4 products in each customer’s shopping cart.
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

# we implement the customer_generation method as a producer. 
# This method generates several customer instances regularly 
# and puts them in the queue. If the queue is full, the put method will wait.
async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count+customers)]
        for customer in customers:
            print("Waiting to put customer in line....")
            await queue.put(customer)
            print("Customer put in line...")
        customer_count = customer_count + len(customers)
        await asyncio.sleep(.001)
        return customer_count


# Finally, we use the main method to initialize the queue, 
# producer, and consumer, and start all concurrent tasks.
async def main():
    customers=10
    queue=3
    cashiers=5
    customer_queue = Queue(queue)
    customer_start_time = time.perf_counter()
    customer_producer = asyncio.create_task(customer_generation(customer_queue, customers))
    cashiers = [checkout_customer(customer_queue, i) for i in range(cashiers)]
    
    result= await asyncio.gather(customer_producer, *cashiers)
    first=result.pop(0)
    print("\n".join(map(str,result)))


    print(f"The supermarket process finished "
          f"{customer_producer.result()} customers "
              f"in {round(time.perf_counter() - customer_start_time ,ndigits=2)} secs")
if __name__ == "__main__":
    asyncio.run(main())