from typing import List


class DataReader:

    @staticmethod
    def getDataListFromFile(filePath: str) -> List:
        with open(filePath) as f:
            lines = [line.rstrip('\n') for line in f]
        return lines
