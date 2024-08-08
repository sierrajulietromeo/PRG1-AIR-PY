# Flight Planning  

A new airline wants to start running commercial passenger flights. In order to assess the feasibility of proposed flights they
want a program that can help calculate the likely profitability of running a flight between a UK and an overseas airport. The UK airport
will be either Manchester (MAN) or London Gatwick (LGW).

They have asked you to create an MVP using some sample flight data. 

* A comma separated (CSV) file called ```airports.csv``` has been provided that contains the name and code for each overseas airport, 
the distance from MAN and the distance from LGW.

* A CSV file has also been provided with aeroplane information (```aeroplanes.csv```).

Two more CSV files are included: ```valid_flight_data.csv``` and ```invalid_flight_data.csv```.

## Task 1

* Each line in the ```valid_flight_data.csv``` file is a potential flight with some sample bookings and ticket prices. You program should read in ```airports.csv```, ```aeroplanes.csv``` and ```valid_flight_data.csv``` and output to the screen the details of the flight and the expected profit or loss for each flight. Additional credit will also be given if this output is also written to a .txt file.

## Task 2

* Each line in the ```invalid_flight_data.csv``` is also potential flights with sample bookings and ticket prices. However, each flight here has a data error (please view the file to see). Your program should be able to gracefully deal with each error and should not calculate impossible figures (for example, if more seats are sold on a plane than the plane actually has!)

## Guidance

  1. Your solution should read in the contents of the mentioned CSV files. This will ensure that your solution will continue to work in the future (e.g. for example if additional overseas airports are added).
  2. You are free to decide on the implementation details of this task. If you were to follow a procedural approach, one approach would be to have a number of functions that perform single tasks that work together to provide the desired output.
  3. Ensure appropriate rounding of floats is considered for calculated values.
 

Here is an example showing the calculation from the first flight data from ```valid_flight_data.csv```.

| UK airport   | Overseas airport   | Type of aircraft   |   Number of economy seats booked |   Number of business seats booked |   Number of first class seats booked |   Price of a economy class seat |   Price of a business class seat |   Price of a first class seat |
|:-------------|:-------------------|:-------------------|---------------------------------:|----------------------------------:|-------------------------------------:|--------------------------------:|---------------------------------:|------------------------------:|
| MAN          | JFK                | Large narrow body  |                              150 |                                12 |                                    2 |                             399 |                              999 |                          1899 |




## Sample Calculation: MAN to JFK (Large Narrow Body Aircraft)

**Flight Details:**

As above

**Data from CSV Files:**

| Source File   | Field                        | Value |
|---------------|-------------------------------|-------|
| airports.csv | Distance from MAN to JFK      | 5376 km |
| aircraft.csv | Running cost per seat per 100km | £7     |
| aircraft.csv | Maximum flight range          | 5600 km |
| aircraft.csv | Total seats                   | 204   |

**Calculations:**

**1. Income:**

| Class      | Seats Booked | Price per Seat | Total Income |
|------------|--------------|---------------|-------------|
| Economy    | 150          | £399          | £59,850     |
| Business   | 12           | £999          | £11,988     |
| First Class | 2           | £1899         | £3,798      |
| **Total**  |             |               | **£75,636** |

**2. Cost:**

| Description                            | Calculation                                               | Value         |
|-----------------------------------------|------------------------------------------------------------|--------------|
| Total seats taken                       | 150 (economy) + 12 (business) + 2 (first-class)              | 164         |
| Cost per seat for the entire flight | £7/seat/100km * (5376 km / 100 km)                           | £376.32/seat |
| Total cost                             | £376.32/seat * 164 seats                                  | £61,732.48   |

**3. Profit:**

£75,636 (income) - £61,732.48 (cost) = £13,903.52
The flight from Manchester (MAN) to JFK (John F. Kennedy International) using a Large narrow body aircraft, with the given seat bookings and prices, would result in a **profit of £13,903.52**.


## Looking for more marks?

* Ensure robust error handling. (Checks for invalid airport/aircraft codes, flight range limitations, and overbooking.)
* Code should be refactored with good coding standards.
* Write your own tests (like what you were provided with in tasks 1,2,3,4)
* Anything else you can think of. This is where you can impress!

