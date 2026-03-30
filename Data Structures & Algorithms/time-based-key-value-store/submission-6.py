class TimeMap:

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []
        self.values[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.values.get(key, [])
        result = "" #return nothing if there is not a valid value

        left = 0
        right = len(values) - 1

        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                result = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        return result

