import pygame
from time import sleep
pygame.init()
pygame.font.init()
w = pygame.display.set_mode((400,520))
pygame.display.set_caption("Kalkulator")
ll = []
hittb = []
indekss = [i for i in range(0,20)]
klicks = ("1","2","3","4","5","6","7","8","9","0","+","-","/","*","**","<-","(",")","=","clear")
value2 = 120
value = 20
act = 1
for l in range(20):
    ll.append((value,value2,60,60))
    hittb.append((value,value+60,value2,value2+60))
    act+=1
    value+=100
    if act == 5:
        value = 20
        value2+=80
        act = 1
def main():
    t = ""
    font = pygame.font.Font(None,32)
    f = font.render("",False,(0,0,0))
    xx,yy = font.size("")
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            w.fill((0,0,0))
            x,y = pygame.mouse.get_pos()
            pygame.draw.rect(w,(150,255,150),(20,20,360,80))
            for lll in ll:
                pygame.draw.rect(w,(255,255,255),lll)
            count = 0
            actt = 0
            for hhh in hittb:
                if x>hhh[0] and x<hhh[1] and y>hhh[2] and y<hhh[3]:
                    pygame.draw.rect(w,(255,0,0),(hhh[0],hhh[2],60,60))
                    actt = 1
                if actt == 0:
                    count += 1
            if actt == 0:
                count = None
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if count==None:
                    pass
                elif count==18:
                        llll = []
                        for i in range(len(t)):
                            if t[i]=="0":
                                try:
                                    k = int(t[i+1])
                                    llll.append(i)
                                except Exception:
                                    pass
                        tt=""
                        for i in range(len(t)):
                            if i in llll:
                                pass
                            else:
                                tt += t[i]
                        f = font.render(str(eval(tt)),False,(0,0,0))
                        xx,yy = font.size(str(eval(tt)))

                elif count==19:
                    pygame.display.set_caption("Clear")
                    t = ""
                    f = font.render("",False,(0,0,0))
                    xx,yy = font.size("")
                elif count==15:
                    t = t[:-1]
                    f = font.render(t,False,(0,0,0))
                    xx,yy = font.size(t)
                else:
                    t+=klicks[count]
                    f = font.render(t,False,(0,0,0))
                    xx,yy = font.size(t)
                sleep(0.1)
            if count==None:
                pygame.display.set_caption("Kalkulator")
            else:
                pygame.display.set_caption("Kalkulator "+str(klicks[count]))

            w.blit(f, (190-xx/2,50-yy/2))
            pygame.display.update()

if __name__ == "__main__":
    main()