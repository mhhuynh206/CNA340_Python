service_choice = input('Enter desired auto service:\n')
print('You entered:', service_choice)
service_choice = service_choice.upper()
service_cost = 0
if service_choice == 'OIL CHANGE':
        service_cost = 35
if service_choice == 'TIRE ROTATION':
        service_cost = 19
if service_choice == 'CAR WASH':
        service_cost = 7
if service_cost == 0:
        print('Error: Requested service is not recognized')
else:
        print('Cost of', service_choice.lower() + ': $' + str(service_cost))