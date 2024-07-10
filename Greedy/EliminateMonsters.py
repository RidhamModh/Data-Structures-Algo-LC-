class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        reachTime = []
        for i in range(len(dist)):
            reachTime.append(math.ceil(dist[i]/speed[i]))
        time= 0
        count = 0
        reachTime.sort()
        print("reachTime",reachTime)
        while time<len(reachTime):
            if time>=reachTime[time]:
                return count
            count+=1
            time+=1
        return count