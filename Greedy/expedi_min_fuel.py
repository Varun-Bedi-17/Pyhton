# -------------------------------------------- Basic Recursion

import sys
def minReFuel(target, startFuel, stations):    # stations= [(distance from end_point(destination), fuel available in station)]
    def minFuel(target_left, currentFuel, start):          
        if target_left <= currentFuel:
            return 0
        
        if start == len(stations):
            return sys.maxsize
        
        take, not_take = sys.maxsize, sys.maxsize

        distance = stations[start][0] - (target - target_left)   # distance = distane from curent position to next station
        fuel_available = stations[start][1]

        if currentFuel >= distance:      # If enough fuel is in car to reach at next station
            take = 1 + minFuel(target_left-distance, currentFuel-distance+fuel_available, start+1)
            not_take = minFuel(target_left-distance, currentFuel-distance, start+1)

        ans = min(take,not_take)
        return ans
    

    answer = minFuel(target, startFuel, 0) 
    if answer != sys.maxsize:
        return answer
    else: 
        return -1

# target = 100
# startFuel = 10
# stations = [[10,60],[20,30],[30,30],[60,40]]      #(distance,fuel)
# stations2 = [[10,100]]

# print(minReFuel(target, startFuel, stations))



# ------------------------------------------------ Memoization


def minReFuel_memo(target, startFuel, stations):    # stations= [(distance from starting, fuel available in station)]
    def recurse(target_left, currentFuel, start):          
        if target_left <= currentFuel:
            return 0
        
        if start == len(stations):
            return sys.maxsize
        
        key = (target_left, currentFuel, start)

        if key in memo:
            return memo[key]

        
        take, not_take = sys.maxsize, sys.maxsize

        distance = stations[start][0] - (target - target_left)   # distance = distane from curent position to next station
        fuel_available = stations[start][1]

        if currentFuel >= distance:      # If enough fuel is in car to reach at next station
            take = 1 + recurse(target_left-distance, currentFuel-distance+fuel_available, start+1)
            not_take = recurse(target_left-distance, currentFuel-distance, start+1)

        memo[key] = min(take,not_take)
        return memo[key]
    

    memo = {}
    answer = recurse(target, startFuel, 0) 
    if answer != sys.maxsize:
        return answer
    else: 
        return -1
    
# target = 100
# startFuel = 10
# stations = [[10,60],[20,30],[30,30],[60,40]]
# print(minReFuel_memo(target, startFuel, stations))

    


    
# -------------------------------------------------------  DP

    
def minReFuelDp(target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        # print(dp)

        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

            # print(dp)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1

# target = 100
# startFuel = 10
# stations = [[10,60],[20,30],[30,30],[60,40]]
# print(minReFuelDp(target, startFuel, stations))





# -------------------------------------------------- Greedy Approach(Heap)
import heapq
def minReFuelGreedy(target, startFuel, stations):
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))

        ans = prev = 0
        for location, capacity in stations:
            startFuel -= location - prev
            while pq and startFuel < 0:  # must refuel in past
                startFuel += -heapq.heappop(pq)
                ans += 1
            if startFuel < 0: return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans


target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
print(minReFuelGreedy(target, startFuel, stations))