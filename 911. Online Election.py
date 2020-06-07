from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        person_hash = {}
        leader_votes = 0
        leader = -1
        self.recode = []
        for i in range(len(times)):
            time = times[i]
            person = persons[i]
            if person in person_hash:
                person_hash[person] += 1
            else:
                person_hash[person] = 1
            if person_hash[person] >= leader_votes:
                leader_votes = person_hash[person]
                leader = person
            self.recode.append(Recode(time, leader))

    def q(self, t: int) -> int:
        s = 0
        e = len(self.recode)
        # 二分找离t最近，小于等于t的时间
        while s + 1 < e:
            m = s + (e - s + 1) // 2
            if self.recode[m].time < t:
                s = m
            elif self.recode[m].time > t:
                e = m
            else:
                return self.recode[m].leader
        if s <= t:
            return self.recode[s].leader
        else:
            return self.recode[e].leader


class Recode:
    def __init__(self, time, leader):
        self.time = time
        self.leader = leader

    def __lt__(a, b):
        return a.time < b.time

# Your TopVotedCandidate object will be instantiated and called as such:
# persons = [0,1,1,0,0,1,0]
# times = [0,5,10,15,20,25,30]
# obj = TopVotedCandidate(persons, times)
#
# print(obj.q(3))
# print(obj.q(12))
# print(obj.q(25))
# print(obj.q(15))
# print(obj.q(24))
# print(obj.q(8))




persons = [0,1,1,0,2,3,2,3,4,4,3,1,4,0,2]
times = [0,1,4,11,14,19,23,30,44,51,73,86,87,88,97]
obj = TopVotedCandidate(persons, times)

list = [[86],[88],[52],[22],[0],[87],[23],[87],[10],[0],[1],[30],[44],[88],[87],[98],[12],[13],[97],[43],[1],[73],[2],[5],[31],[11],[29],[24],[72],[18]]
for ele in list:
    print(ele[0])
    print(obj.q(ele[0]))
