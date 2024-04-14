class recTang:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def getWidth(self):
        return self.width 

    def getHeight(self):
        return self.height


def main():
    GW=int(input('How many * should the width Be:'))
    print('*'*GW,' /n/n','*'*GW)
    recTang.getWidth=GW
main()
rotat