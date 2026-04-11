
-- SQL CASE AND WHEN

--  Problem 2: Bonus Calculation Based on Department and Performance Scenario: Bonus is calculated based on the department and performance rating:

SELECT *,
  CASE
    -- Finance Department
    WHEN department = 'Finance' 
         AND performance_rating = 'A' 
      THEN salary * 0.20
    
   WHEN department = 'Finance' 
         AND performance_rating = 'B' 
      THEN salary * 0.15
  
   WHEN department = 'Finance' 
         AND performance_rating = 'C' 
      THEN salary * 0.5
    
  WHEN department = 'Engineering' 
         AND performance_rating = 'A' 
      THEN salary * 0.18
    
  WHEN department = 'Engineering' 
         AND performance_rating = 'B' 
      THEN salary * 0.12
  
  WHEN department = 'Engineering' 
         AND performance_rating = 'C' 
      THEN salary * 0.3

    -- Other Departments
    ELSE salary * 0.08
  END AS bonus
FROM Employee;



-------------------------------------------------------------------
-- Problem 3: Categorizing Employees by Salary Range and Performance
-------------------------------------------------------------------

select *,
  case
    when salary > 80000 and performance_rating = 'A'then 'High Performer'
    when salary between 50000 and 80000 and performance_rating = 'B' then 'Mid Performer'
    when salary < 50000 and performance_rating = 'C' then 'Low Performer'
    end performer
    from employee;

----------------------------------------------------------------
-- Problem 4: Risk Assessment Based on Experience and Department
----------------------------------------------------------------
SELECT *,
  CASE 
    -- Performance A
    WHEN performance_rating = 'A' THEN 
      CASE 
        WHEN salary > 80000 AND experience > 5 THEN '25% Hike'
        WHEN salary > 80000 THEN '20% Hike'
        WHEN salary BETWEEN 50000 AND 80000 THEN '15% Hike'
        ELSE 'No Hike'
      END

    -- Performance B
    WHEN performance_rating = 'B' THEN 
      CASE 
        WHEN experience > 5 THEN '12% Hike'
        ELSE '10% Hike'
      END

    -- Performance C
    WHEN performance_rating = 'C' THEN 'No Hike'

    ELSE 'No Hike'
  END AS hike
FROM Employee;

-------------------
--Nested Cases
------------------
-----------------------------------------------------------------------------------
-- Problem 1: Nested CASE for Performance and Salary Hike Based on Multiple Criteria
------------------------------------------------------------------------------------
select *,
     CASE 
      WHEN performance_rating = 'A' THEN 
        CASE 
          WHEN salary > 80000 AND experience > 5 THEN '25% Hike'
          WHEN salary BETWEEN 50000 AND 80000 THEN '15% Hike'
          ELSE 'No Hike'
        END
      WHEN performance_rating = 'B' THEN 
        CASE 
          WHEN experience > 5 THEN '12% Hike'
          ELSE '10% Hike'
        END
      WHEN performance_rating = 'C' THEN 'No Hike'
      ELSE 'No Hike'
    END AS hike
FROM Employee

-------------------------------------
-- problem 2.Department and Performance
--------------------------------------
SELECT *,
  CASE 
    -- Finance
    WHEN department = 'Finance' THEN 
      CASE 
        WHEN performance_rating = 'A' AND experience > 10 THEN salary * 0.25
        ELSE salary * 0.20
      END

    -- HR
    WHEN department = 'HR' THEN 
      CASE
        WHEN performance_rating = 'B' OR experience > 5 THEN salary * 0.15
        ELSE salary * 0.10
      END

    -- Other departments
    ELSE salary * 0.08
  END AS bonus

FROM Employee;

--------------------------------------
-- Problem 3: Nested CASE for Employee Categorization Based on Salary, Performance, and ExperienceScenario
---------------------------------------
SELECT *,
  CASE 
    -- Salary > 70000
    WHEN salary > 70000 THEN 
      CASE 
        WHEN performance_rating = 'A' AND experience > 8 THEN 'Top performer'
        WHEN experience <= 8 THEN 'Mid performer'
        ELSE 'Mid performer'
      END

    -- Salary between 50k and 70k
    WHEN salary BETWEEN 50000 AND 70000 THEN 
      CASE
        WHEN performance_rating = 'A' THEN 'Rising Star'
        ELSE 'Average performer'
      END

    -- Salary < 50k
    WHEN salary < 50000 THEN 'Low Performer'

  END AS category
FROM Employee;      

-------------------------------------------
-- 4.Nested CASE for Tax Bracket Based on Salary and Experience
--------------------------------------------
SELECT *,
  CASE 
    -- Salary > 90000
    WHEN salary > 90000 THEN 
      CASE 
        WHEN experience > 10 THEN '35% tax bracket'
        ELSE '30% tax bracket'
      END 

    -- Salary 60000 to 90000
    WHEN salary BETWEEN 60000 AND 90000 THEN
      CASE 
        WHEN experience > 5 THEN '25% tax bracket'
        ELSE '20% tax bracket'
      END

    -- Salary < 60000
    WHEN salary < 60000 THEN '15% tax bracket'

    ELSE 'No Tax Info'
  END AS tax_bracket

FROM Employee;

---------------------------------------------
-- Problem 5: Nested CASE for Promotion Eligibility Based on Performance, Salary, and Experience
----------------------------------------------
select *,
  CASE 
    when performance_rating = 'A'then 
    CASE 
      when salary > 75000 and experience > 7 then 'Eligible for senior role'
      else 'Eligible for junior role'
    end 
    when performance_rating = 'B' then
    CASE 
      when experience > 5 then 'Eligible for Consideration'
      else 'Not Eligible'
    end 
    when performance_rating= 'C' then 'Not Eligible'
  end as promotion_eligibility
from employee;
