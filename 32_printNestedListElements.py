def printNested(arr):
    for each_item in arr:
        if isinstance(each_item, list):
            for nested_item in each_item:
                print(nested_item)
        else:
            print(each_item)

printNested([1,2,3,[4,5,[6]]])
