class ocean:

    def __init__(self):
        self.ocean = []
    
    def construireOcean(self, x,y):
        self.ocean = [["o" for i in range(x)] for i in range(y)]


    def afficherOcean(self, type):
        for i in range(1,len(self.ocean)+1):
            if(i==len(self.ocean) and type==1):
                if(i<10):
                    print(" "+str(i)+" "+" ".join(self.ocean[i-1])+"  Tirs")
                else:
                    print(str(i)+" "+" ".join(self.ocean[i-1])+"  Tirs")
            else:
                if(i<10):
                    print(" "+str(i)+" "+" ".join(self.ocean[i-1]))
                else:
                    print(str(i)+" "+" ".join(self.ocean[i-1]))

    def largeurOcean(self):
        return len(self.ocean)

    def hauteurOcean(self):
        return len(self.ocean[0])        

#TEST
#ZBRA