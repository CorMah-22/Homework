# SECTION 07 HW 

## Section 7.1
> **Note:** SavvyCoders_SQL_chargeDB.db database was set up  for this section for the first part of the HW.

<br>

### 7.1 HW Answers

#### Question 1
1. Using EVregistry, Write a query to select the `ModelYear`, `Make`, and `Model` off all of the vehicles in the registry.

```SQL

SELECT ModelYear, Make, Model
FROM EVRegistry;

```
#### Question 2 
2. Using the EVRegistry table, Write a query that lists all of the unique types of EV's. your reult set should have one column, `ElectricVehicleType`. 

```SQL

SELECT DISTINCT "ElectricVehicleType" FROM "EVRegistry";

```
#### Question 3
3. Using the EVRegistry, Write a query that shows all of the information on Battery Electric Vehicles (BEV) that are in the registry. 

```SQL

SELECT * 
FROM "EVRegistry"
WHERE ElectricVehicleType= "Battery Electric Vehicle (BEV)";

```
#### Question 4
4. Using the EVRegistry, wirte a query that returns the `Make` and `Model` of all of the EV's that have a BaseMSRP between 20000 and 35000?  

```SQL

SELECT * 
FROM "EVRegistry"
WHERE BaseMSRP < 20000 AND BaseMSRP < 35000;

```

## Section 7.2

### 7.2 HW Answers

> **Note:** SavvyCoders_SQL_chargeDB.db database was set up  for this section for the first part of the HW.

#### Question 1 

1. Using EVRegistry, write a query to find a record  where the `City` attribute is NULL. Return all of the available columns. 
```SQL

SELECT * 
FROM "EVRegistry"
WHERE City IS NULL;
```
## Question 2
2. Write a query to find the `make`, `model`, and `ElectricVehicleType` where the VIN number has  that ends in '3E1EA1J'.
```SQL

SELECT  Make, Model, ModelYear, VIN
FROM EVRegistry
WHERE VIN LIKE "%3E1EA1J";
```

#### Question 3

3. Select the `ModelYear`, `make`, `model`, `ElectricVehicleType`, and `range` of the Tesla vehicles or cheverolet vehicles in the registry. Order the result set by Make and Model year in from newest to oldest. 

```SQL

SELECT  Make, Model, ModelYear, ElectricVehicleType, ElectricRange
FROM EVRegistry
WHERE Make = "TESLA" OR Make = "CHEVROLET"
ORDER BY Make, ModelYear ASC;

```

#### Question 4

4. Using EVCharging, Write a query to find out how many many times those stations were used. Order them by the most used to the least used and limit the output to 5 records. 

```SQL

SELECT stationId, COUNT(DISTINCT sessionId) AS Usage
FROM "EVCharging"
GROUP BY stationId
ORDER BY Usage DESC
LIMIT 5;

```
#### Question 5

5.  Using EVCharging, For the folks who charged longer than 0.5 hours, show the min and max of the charging time for each user. Your output columns should be `userid`, `minTime`, and `maxTime`. Order this result set by the last two columns respectively. 

```SQL

SELECT userid, MAX(chargeTimeHrs) AS maxHrs, MIN(chargeTimeHrs) AS minHrs
FROM "EVCharging"
WHERE chargeTimeHrs > 0.5
GROUP BY userid
ORDER BY maxHrs, minHrs;

```
## Section 7.3

### 7.3 HW Answers

> **Note:** SavvyCoders_SQL_chargeDB.db database was set up  for this section

#### Question 1

1. Using EVCharging, Which day of the week has the highest average charging time? Round the answer to 2 decimal points.

```SQL

SELECT ROUND(AVG(chargeTimeHrs),2) as 'avgChargeTime'
FROM EVCharging

-- Tue

```
#### Question 2

2. Using, EV charging, Find the total power consumed from charging EV's by each User. Return the `userId` and name the calculated column, `totalPower`. Round the answer to 2 deciaml points and list the out put in highest to lowest order. Limit the order to the top 15 users. 

```SQL

SELECT userId, ROUND(SUM(kwhTotal),2) AS totalPower
FROM EVCharging
GROUP BY userId
ORDER BY  totalPower DESC
LIMIT 15

```
#### Question 3

3. Using dimfacility and factCharge, write a query to find out which type of facility (GROUP BY) has the most amount of charging stations. Return `type Facility` and name the calculated column `numStation`. Order the result set from highest to lowest number of charging stations.
```SQL

SELECT b.typeFacility AS facilityType, COUNT(DISTINCT a.stationID) AS numStation
FROM factCharge AS a
INNER JOIN dimfacility AS b ON a.facilityID = b.FacilityKey
GROUP BY b.typeFacility
ORDER BY  2 DESC

```
#### Question 4

4. In your own words, Briefly explain Primary Keys and Foreign Keys. 

**Primary key** is unique indetifier for each row in a table, it only appears once in table.

**Foreign Key** is primary key tat used in diffrent table from the orginla table and can be repeated in the new table. 

#### Question 5

5. Using EV Charging, For the folks who charged longer than one hour, show the min and max of the charging time for each user. Your output columns should be `userid`, `minTime`, and `maxTime`. Order this result set by the last two columns respectively. HINT: USE `HAVING`

```SQL

SELECT userid, MIN(chargeTimeHrs) AS minTime, MAX(chargeTimeHrs) AS maxTime
FROM EVCharging
GROUP BY userid
HAVING  chargeTimeHrs > 1
ORDER BY 2, 3

```

