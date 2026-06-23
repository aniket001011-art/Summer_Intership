countdown = int(input("\n Enter the number--"))  

while(countdown>=1):
    print(countdown)
    countdown-=1
    if countdown==4:
        break
        print("Loop stopped early!")