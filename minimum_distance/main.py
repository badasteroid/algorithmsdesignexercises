import instancesgenerator as ig

def min_distance(pointslist):

    for p1 in pointslist:
        for p2 in pointslist:
            if p1!=p2:
                distances_couples=[(distance(p1,p2),p1,p2)]

    return min(distances_couples)

def distance(p1,p2):

    x1,y1 = p1
    x2,y2 = p2

    return (x1-x2)**2 + (y1-y2)**2

def main():
    print('wtf is happening')
    pointexample = 0,0
    singletonl = ig.generate(pointexample,[],1)
    nullton = ig.generate(pointexample, [], 0)
    coupleton = ig.generate(pointexample, [], 2)
    randomton = ig.generate(pointexample, [],int.__rand__())

    print("minimum distances are\n")
    min0 = min_distance(nullton)
    print("for nullton: \t\t\t\t", min0)
    min1 = min_distance(singletonl)
    print('\nfor singleton: \t\t\t\t', min1)
    min2 = min_distance(coupleton)
    print('\nfor the couple: \t\t\t\t',min2)
    minr = min_distance(randomton)
    print('for a random number of points:\t',minr)
    print('\n\nbye bitch')