import time

#Probabilities of change between happy (H) neutral (N) and sad (S).
HH = 0.5033112582781457
HN = 0.33112582781456956
HS = 0.16556291390728478
NH = 0.3728813559322034
NN = 0.3728813559322034
NS = 0.2542372881355932
SH = 0.3263157894736842
SN = 0.25263157894736843
SS = 0.42105263157894735

moodlist = []
daylist= []
day = 0

#feel function should occur every day (every 86400 seconds)
def feel():
  time.sleep(86400)
  day += 1
  
