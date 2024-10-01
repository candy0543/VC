#add.py

def add(a,b):
    return a+b

if __name__ == "__main__":
    name = input("Enter your name: " )
    fav_sport = input("Enter your favorite sport: ")
    
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    
    result = add(num1, num2)
    print(f"Ths sum of num1 and num2 is :{result}")

