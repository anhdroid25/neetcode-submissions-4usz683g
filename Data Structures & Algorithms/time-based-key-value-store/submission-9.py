class TimeMap:

    def __init__(self):
      self.store = {} #make a hashmap

    def set(self, key: str, value: str, timestamp: int) -> None:
      if not key in self.store:
         self.store[key]= [(timestamp, value)]
      else:
         self.store[key].append([timestamp, value])
        
        
    def get(self, key: str, timestamp: int) -> str:
      if key not in self.store:
         return ""
      left = 0
      right = len(self.store[key]) - 1

      while left <= right:
         middle = (left + right) // 2
         if self.store[key][middle][0] == timestamp:
            return self.store[key][middle][1]
         elif self.store[key][middle][0] < timestamp:
            left = middle + 1
         elif self.store[key][middle][0] > timestamp:
            right = middle - 1
      if right >= 0:
         return self.store[key][right][1]
      return ""

            



