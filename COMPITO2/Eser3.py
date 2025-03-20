def find_element(lst: list[int]=[1,2,3,4,5], element: int=5) -> bool:
    for item in lst:
        if item == element:
            return True
   
    find_element([10,20,30],20)
    for item in lst:
        if item==element:
            return False
    find_element([1,2,3,4,5],6)
    if item!=element:
        return False

     

