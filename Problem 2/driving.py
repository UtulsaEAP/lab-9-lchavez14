def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   req_gallons = miles_driven / miles_per_gallon 
   cost = req_gallons * dollars_per_gallon
   return cost

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
   
    #print your costs here like example below
    #print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
    miles_driven = float(input())
    
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
    
   
   