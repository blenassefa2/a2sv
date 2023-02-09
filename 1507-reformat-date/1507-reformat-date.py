class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        monthNumber = defaultdict(str)
        
        for i in range(len(months)):
            val = str(i + 1)
            if i + 1 < 10:
                val = "0" + str(i + 1)
            monthNumber[months[i]] = val
        
        day, month, year = date.split(" ")
        if len(day[:-2]) == 1:
            day = "0" + day
        return year + "-"+ monthNumber[month] + "-"+ day[:-2]