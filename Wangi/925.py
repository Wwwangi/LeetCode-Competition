class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pointerName=0
        previous=''
        pointerTyped=0
        while pointerTyped<len(typed):
            print(typed[pointerTyped],name[pointerName],previous)
            if(typed[pointerTyped]==name[pointerName]):
                previous=name[pointerName]
                pointerTyped+=1
                if(pointerName<len(name)-1):
                    pointerName+=1
            elif(typed[pointerTyped]==previous):
                pointerTyped+=1
            else:
                return False
        if(pointerName==len(name)-1 and typed[pointerTyped-1]==name[pointerName]):
            return True
        return False