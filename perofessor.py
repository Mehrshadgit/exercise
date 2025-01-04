import random


def main():
    n=0
    get_level()
    for i in range(10):
        gen_int(get_level.level)
        for i in range(3):
            try:
                answer=float(input(f"{gen_int.a} + {gen_int.b} = "))
                if answer == gen_int.a + gen_int.b:
                    break
                else:
                    print("EEE")
                    continue
            except:
                print("EEE")
                continue
        if not answer == gen_int.a + gen_int.b:
            print(f"{gen_int.a} + {gen_int.b} = {gen_int.a + gen_int.b}")
            n+=1
    print(f"Score: {10-n}")



def get_level():
    while True:
        try:
            get_level.level=int(input("Level: "))
            if get_level.level in [1, 2 ,3]:  #or range(1, 4)
                break
            else:
                continue
        except:
            continue



def gen_int(level):
    if level in [1, 2, 3]:
        if level==1:
            gen_int.a=random.randint(0,9)
            gen_int.b=random.randint(0,9)
        elif level==2:
            gen_int.a=random.randint(10,99)
            gen_int.b=random.randint(10,99)
        elif level==3:
            gen_int.a=random.randint(100,999)
            gen_int.b=random.randint(100,999)
    else:
        raise ValueError



if __name__ == "__main__":
    main()
