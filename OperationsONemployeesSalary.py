from __future__ import division 
import numpy
from collections import defaultdict,Counter
import matplotlib.pyplot as plt

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

salary_by_tenure=defaultdict(list)

for tenure,salary in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)


average_salary_by_tenure={
                   tenure:sum(salaries)/len(salaries)
                   for tenure,salaries in salary_by_tenure.items()
                   }
def tenure_by_bucket(tenure):
  if tenure < 2:
     return " less than two years of expereince"
  elif tenure < 5:
    return " greater than two and less than five years of experience"
  else:
      return " more than five years of expereince"
    

salary_by_tenure_bucket=defaultdict(list)

for salary,tenure in salaries_and_tenures:

    bucket=tenure_by_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
average_salary_by_bucket={
              tenure_bucket:sum(salaries)/len(salaries)
              for tenure_bucket,salaries in salary_by_tenure_bucket.items()
              }
def apply_to_one(f):
    return f(1)


