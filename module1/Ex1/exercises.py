import random
import time

start_time = time.perf_counter()

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or max < min or quantity <1 or quantity > 1000 or quantity > max-min+1:
        print(f"Out of range")
        return list()
    # else:
    #     ticket_list = range(min, max+1)
    #     the_main_list = sorted(random.sample(ticket_list, quantity))
    #     #final_list = sorted(the_main_list)   
    # return the_main_list
    # Nice one option :)
    #return sorted(random.sample(range(min, max+1), quantity))
    

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
        
end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")
    
#0.0001981999957934022 секунд > Час виконання: 0.00016469997353851795 секунд