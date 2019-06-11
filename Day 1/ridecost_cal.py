#ride cost calculator

distance_travelled=int(input("Enter the distance travelled in kilometers: "))
cost_of_diesel=int(input("Enter the cost of diesel: "))
avg_of_car=int(input("Enter the average of car: "))

#calculate the fuel used in ride
fuel_used= distance_travelled/avg_of_car

#calculating cost
cost=fuel_used*cost_of_diesel
print("Cost of ride is: ",cost)
