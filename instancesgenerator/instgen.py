def __init__(self, datapoint, structure, istances):
    if structure == []:
        return generate(type(datapoint), structure, istances)



def generate(t: type, structure: object, n: int) -> object:

    outputdata = structure

    if t is int:
        dpexample = 0

        for i in n:
                outputdata.append(dpexample.__rand__())

    if t is tuple and t[0] is int and t[1] is int:
        dpexample = (0,0)

        for i in n:
            outputdata.append(dpexample[0].__rand__(), dpexample[1].__rand__())
    return outputdata

