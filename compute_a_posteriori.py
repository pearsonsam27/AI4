import sys
input = sys.argv[1]

def compute_a_posteriori():
    ph1=.1
    ph2=.2
    ph3=.4
    ph4=.2
    ph5=.1

    def totalCalc(character):
        total=0
        if character =='C':
            total+=ph1*1+ph2*.75+ph3*.5+ph4*.25+ph5*0
        if character =='L':
            total+=ph1*0+ph2*.25+ph3*.5+ph4*.75+ph5*1
        return total


    for character in input:
        if(character =='C'):
            pqh1=1
            pqh2=.75
            pqh3=.5
            pqh4=.25
            pqh5=0

        if(character =='L'):
            pqh1 = 0
            pqh2 = .25
            pqh3 = .5
            pqh4 = .75
            pqh5 = 1

        denominator = totalCalc(character)

        ph1=(pqh1*ph1)/denominator
        ph2=(pqh2*ph2)/denominator
        ph3=(pqh3*ph3)/denominator
        ph4=(pqh4*ph4)/denominator
        ph5=(pqh5*ph5)/denominator


    f=open ("results.txt",'w')
    f.write("Observation sequence Q: "+input+'\n')
    f.write("Length of Q: "+str(len(input))+'\n')
    f.write("P(h1 | Q) = "+'%.5f'%ph1+'\n')
    f.write("P(h2 | Q) = "+'%.5f'%ph2+'\n')
    f.write("P(h3 | Q) = "+'%.5f'%ph3+'\n')
    f.write("P(h4 | Q) = "+'%.5f'%ph4+'\n')
    f.write("P(h5 | Q) = "+'%.5f'%ph5+'\n')
    f.write('\n')
    f.write("Probability that the next candy we pick will be C, given Q: " + '%.5f' % totalCalc('C')+'\n')
    f.write("Probability that the next candy we pick will be L, given Q: "+'%.5f'%totalCalc('L')+'\n')
    f.close()


compute_a_posteriori()