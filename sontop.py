
import random

def sontop(x):
    mus=random.randint(1, x)
    print(f"Men 1 dan {x} gacha son uyladim topa olasizmi?")
    urinishlar=0
    while 1:
        urinishlar+=1
        taxmin=int(input(">>>"))
        if taxmin<mus:
            print("Xato men o'ylagan son bundan kattaroq.Yana harakat qiling:")
        elif taxmin>mus:
            print("Xato men o'ylagan son bundan kichikroq.Yana harakat qiling:")
        else:
            break
    print(f"Tabriklaymiz. Siz {urinishlar} taxmin bilan topdingiz!")
    return urinishlar

def top_pc(x):
    input(f"1 dan {x} gacha son o'ylang va boshlash uchun istalgan tugmani bosing.Men topaman")
    pc_taxmin=0
    a=x//2
    b=x//2
    while 1:
        pc_taxmin+=1
        javob = input(f"Siz {a} sonini o'yladingiz: tog'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), kichikroq (-),"
                      ">>>")
        b=b//2
        if javob=="+":
            if b==1:
                b=1
            a=a+b
            
        elif javob=="-":
            if b==1:
                b=1
            a=a-b
            
        else:
            break
    print(f"Men {pc_taxmin} ta taxmin bilan topdim!")
    return pc_taxmin
        
def play():
    yana=1
    
    while yana:
        x=int(input("Shunday son kiritin men siz bilan 1 dan siz kiritgan songacha son o'ylab"
            " usha sonni topish o'yinini o'ynaymiz >>>")) 
        my_taxmin=sontop(x)
        pc_taxmin1=top_pc(x)
        
        if my_taxmin < pc_taxmin1:
            print("Siz yutdingiz tabriklayman! "
                  f"Hisob {my_taxmin}:{pc_taxmin1}")
        elif my_taxmin > pc_taxmin1:
            print("Afsus bu uyinda siz yutqazdingiz!"
                  f"Hisob {my_taxmin}:{pc_taxmin1}")
        else:
            print("Qoyil taxminlarimiz teng chiqdi"
                  f"Hisob {my_taxmin}:{pc_taxmin1}")
        yana=int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))
    
    
    

print(play())
    
    
    
