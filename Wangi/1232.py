class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if((coordinates[1][0]-coordinates[0][0])!=0):
            slope=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        for point in coordinates[2:]:
            if((coordinates[1][0]-coordinates[0][0])==0):
                if((point[0]-coordinates[0][0])!=0):
                    return False
            else:
                temp=(point[1]-coordinates[0][1])/(point[0]-coordinates[0][0])
                if(slope!=temp):
                    return False
        return True