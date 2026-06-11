class MedianFinder:

    def __init__(self):
        self.data=[]

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        self.data.sort()
        n=len(self.data)
        if n%2==1:
            return self.data[n//2]
        else:
            x=self.data[n//2]
            y=self.data[(n//2)-1]
            return (x+y)/2
        
        