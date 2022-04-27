class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        task =defaultdict(int)
    
        a = tasks[0]
        for i in tasks:
            task[i] += 1
            if task[i] > task[a]:
                a = i
       
        max_ = []
        
        for j in task:
            if task[j] == task[a]:
                max_.append([j, task[j]])
        x = len(tasks) - task[a]
      
        y =(((task[a] - 1)*(n)) - x) + (len(max_) - 1)
        
        if y <= 0:
            y = 0
        
        return (y + len(tasks))