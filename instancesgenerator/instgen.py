def __init__(self, datapoint, structure, istances):
    if structure == []:
        return generate(type(datapoint), structure, istances)



def generate(t: type, structure: object, n: int) -> object:
    outputdata = structure
    if t is int:
        dpexample = 0
        generate(int)
        for i in n:
                outputdata.append(dpexample.__rand__())
    return outputdata

