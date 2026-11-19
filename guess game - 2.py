import random 
#لعبة تخمين الارقام هنا يطلب من المستخدم ادخال رقم وتخزينه في متغير 

secret_number = random.randint(1, 100)

while True:

   player_choice =int (input("what is the number:"))

   if player_choice == secret_number : 
        print("congrtulations! you are correct")
       
        break

   else :
    
    print("false! try again")


   

    