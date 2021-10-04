#right-angled triangle star_pattern
def star_pattern(num):
    if num==0:
        return
    else:
        star_pattern(num-1)
        print("*" * num)

num = int(input("enter the no. of rows: "))
star_pattern(num)  
