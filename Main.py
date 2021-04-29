from Apriori_Module import Apriori
print("WELCOME TO THE PROFIT DISTRIBUTOR INCREMENT TOOL")
print("1.FOOD")
print("2.GROCERY")
print("3.ELECTRONIC APPLIANCES")
Filenameinput=input("Enter the no 1,2.,3..")
if Filenameinput=="1":
    print("Please choose subcategories:\n")
    print("1.Fruits\n")
    print("2.Vegetables\n")
    userchoice=input("Enter the no 1,2")
    if userchoice=="1":
        P1=Apriori(5/30,0.6,"fruits.txt")
        P1.CkLkAr()

    elif userchoice=="2":
        P2=Apriori(5/30,0.6,"Vegetables.txt")
        P2.CkLkAr()
    else:
        print("Please enter valid subcategories")
elif Filenameinput=="2":
    print("Please choose subcategories:\n")
    print("1.Pulses & Grains\n")
    print("2.Dairy\n")
    print("3.Toileraties\n")
    print("4.Household Essential\n")
    userchoice=input("Enter the no 1,2,3,4")
    if userchoice=="1":
        P3=Apriori(5/30,0.6,"Pulses&Grains.txt")
        P3.CkLkAr()
    elif userchoice=="2":
        P4=Apriori(5/30,0.6,"Dairy.txt")
        P4.CkLkAr()
    elif userchoice=="3":
        P5=Apriori(5/30,0.6,"Toileraties.txt")
        P5.CkLkAr()
    elif userchoice=="4":
        P6=Apriori(5/30,0.6,"HouseholdEssential.txt")
        P6.CkLkAr()
    else:
        print("Please enter valid subcategories")
elif Filenameinput=="3":
    print("Please enter choice:\n")
    print("1.HomeAppliances\n")
    print("2.ComputerAppliances\n")
    userchoice=input("Enter the no 1,2")
    if userchoice=="1":
        P7=Apriori(5/30,0.6,"Home_Appliances.txt")
        P7.CkLkAr()
        
    elif userchoice=="2":
        P8=Apriori(5/30,0.6,"ComputerAppliances.txt")
        P8.CkLkAr()
    else:
        print("Please enter valid subcategories")

