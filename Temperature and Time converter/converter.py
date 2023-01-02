#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#Starting statment:-
print("Welcome to Converter")
print("Choose any one option.")
a=input("Press 'Y' to Start or 'N' to Stop program:- " )
if a=="y" or a=="Y":
    print("""1.Temperature 
2.Time """)
    d=int(input("Type your desired option to Convert:- "))
    if d==1:
        f=int(input("""Enter the desired option from the following to Convert:-
1.Celsius to Kelvin
2.Kelvin to Celsius
3.Celsius to Farenhite
4.Farenhite to Celsius
Type your desired option:- """))
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#1
        if f==1:
            def kill():
                o=a+273
                return o
            a = int(input("Enter temperature in Celsius:- "))
            e=kill()
            print("Your answer is",e,"K")

            g=int(input("""Do you want Result in:- 
1.Text file
2.Binary file
3.or Exit
Choose the desired option:- """))
            if g==1:
                    file=open("Temperature.txt","w")
                    file.write(str(a)+"C in Kelvin is "+str(e)+"k")
                    file.close()
                    print("""Value uploaded in "Temperature.txt" file successfully.""")
            elif g==2:
                    import pickle
                    file=open("Tbinary.dat","wb")
                    k=e,"Kelvin"
                    pickle.dump(k,file)
                    file.close()
                    print("""Value uploaded in "Tbinary.dat" text file successfully.
Do you want the Result of Binary file
1)Y
2)N""")
                    l=input("Enter the desired option:- ")
                    if l=="y" or l=="Y":
                        import pickle
                        file=open("Tbinary.dat","rb")
                        str=pickle.load(file)
                        print(str)
                        file.close()
                    elif l=="n" or l=="N":
                        print("Thank You!")
                    else:
                        print("Invalid key pressed")
            elif g==3:
                print("Thank You!!")
            else:
                print("Invalid Key pressed.")

#2
        elif f==2:
            def kill():
                q=e-273
                return q
            e=int(input("Enter temperature in Kelvin:- "))
            s=kill()
            print("Your answer is",s,"C")
            g = int(input("""Do you want Result in:- 
1.Text file
2.Binary file
3.or Exit
Choose the desired option:- """))
            if g == 1:
                file = open("Temperature.txt", "w")
                file.write(str(e) + "K in Celsius is " + str(s) + "C")
                file.close()
                print("""Value uploaded in "Temperature.txt" file successfully.""")
            elif g == 2:
                import pickle

                file = open("Tbinary.dat", "wb")
                k = s, "Celsius"
                pickle.dump(k, file)
                file.close()
                print("""Value uploaded in "Tbinary.dat" text file successfully.
Do you want the Result of Binary file
1)Y
2)N""")
                l = input("Enter the desired option:- ")
                if l == "y" or l == "Y":
                    import pickle

                    file = open("Tbinary.dat", "rb")
                    str = pickle.load(file)
                    print(str)
                    file.close()
                elif l == "n" or l == "N":
                    print("Thank You!")
                else:
                    print("Invalid key pressed")
            elif g == 3:
                print("Thank You!!")
            else:
                print("Invalid Key pressed.")

#3
        elif f==3:
            def kill():
                t=(9/5*c)+32
                return t
            c=float(input("Enter the temperature in Celsius:- "))
            k=kill()
            print("Your answer is",k,"F")
            g = int(input("""Do you want Result in:- 
1.Text file
2.Binary file
3.or Exit
Choose the desired option:- """))
            if g == 1:
                file = open("Temperature.txt", "w")
                file.write(str(c) + "C in Farenhite is " + str(k) + "F")
                file.close()
                print("""Value uploaded in "Temperature.txt" file successfully.""")
            elif g == 2:
                import pickle

                file = open("Tbinary.dat", "wb")
                q = k, "Farenhite"
                pickle.dump(q, file)
                file.close()
                print("""Value uploaded in "Tbinary.dat" text file successfully.
Do you want the Result of Binary file
1)Y
2)N""")
                l = input("Enter the desired option:- ")
                if l == "y" or l == "Y":
                    import pickle

                    file = open("Tbinary.dat", "rb")
                    str = pickle.load(file)
                    print(str)
                    file.close()
                elif l == "n" or l == "N":
                    print("Thank You!")
                else:
                    print("Invalid key pressed")
            elif g == 3:
                print("Thank You!!")
            else:
                print("Invalid Key pressed.")

#4
        elif f==4:
            def kill():
                o=(5/9*a)-32
                return o
            a=int(input("Enter the temperature in Farenhite:- "))
            r=kill()
            print("Your answer is",r,"C")
            g = int(input("""Do you want Result in:- 
1.Text file
2.Binary file
3.or Exit
Choose the desired option:- """))
            if g == 1:
                file = open("Temperature.txt", "w")
                file.write(str(a) + "C in Kelvin is " + str(r) + "k")
                file.close()
                print("""Value uploaded in "Temperature.txt" file successfully.""")
            elif g == 2:
                import pickle
                file = open("Tbinary.dat", "wb")
                q = r, "Celsius"
                pickle.dump(q, file)
                file.close()
                print("""Value uploaded in "Tbinary.dat" text file successfully.
Do you want the Result of Binary file
1)Y
2)N""")
                l = input("Enter the desired option:- ")
                if l == "y" or l == "Y":
                        import pickle

                        file = open("Tbinary.dat", "rb")
                        str = pickle.load(file)
                        print(str)
                        file.close()
                elif l == "n" or l == "N":
                        print("Thank You!")
                else:
                        print("Invalid key pressed")
            elif g == 3:
                print("Thank You!!")
            else:
                print("Invalid Key pressed.")


        else:
            print("Invalid key pressed")

# 1.Temperature to convert:- END

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 2.Time to convert:- START

    elif d==2:
        print("Choose any one option:- ")
        print("""1.Hour to Seconds
2.Minutes to Seconds
3.Seconds to Hour
4.Minutes to Hour 
5.Hour to Minutes """)
        z=int(input("Choose your desired option from the above following to convert:- "))
#1
        if z==1:
            def gta():
                d=s*3600
                return d
            s=int(input("Enter the time in Hour:- "))
            w=gta()
            print("Your answer is",w,"Seconds")
            g =(input("""Do you want Result in Text file
Choose the desired option in "Y" for Yes and "N" for NO:- """))
            if g=="Y" or g=="y":
                file = open("Time.txt", "w")
                file.write(str(s) + "Hour in Seconds is " + str(w) + "S")
                file.close()
                print("""Value uploaded in "Time.txt" file successfully.""")
            elif g=="N" or g=="n":
                print("Thank You!!")
            else:
                print("Invalid key pressed")
#2
        elif z==2:
            def gta():
                s=d*60
                return s
            d=int(input("Enter the Time in Minutes:- "))
            l=gta()
            print("Your answers is",l,"Seconds")
            g = (input("""Do you want Result in Text file
Choose the desired option in "Y" for Yes and "N" for NO:- """))
            if g == "Y" or g == "y":
                file = open("Time.txt", "w")
                file.write(str(d) + "Minutes in Seconds is " + str(l) + "S")
                file.close()
                print("""Value uploaded in "Time.txt" file successfully.""")
            elif g == "N" or g == "n":
                print("Thank You!!")
            else:
                print("Invalid key pressed")

#3
        elif z==3:
            def gta():
                s=d/3600
                return s
            d = int(input("Enter the Time in Seconds:- "))
            y=gta()
            print("Your answer is",y,"Hours")


            g = (input("""Do you want Result in Text file
Choose the desired option in "Y" for Yes and "N" for NO:- """))
            if g == "Y" or g == "y":
                file = open("Time.txt", "w")
                file.write(str(d) + "Seconds in Hours is " + str(y) + "hrs")
                file.close()
                print("""Value uploaded in "Time.txt" file successfully.""")
            elif g == "N" or g == "n":
                print("Thank You!!")
            else:
                print("Invalid key pressed")
#4
        elif z==4:
            def gta():
                s=int(input("Enter the Time in Minutes:- "))
                f=s/60
                return f
            s = int(input("Enter the Time in Minutes:- "))
            h=gta()
            print("Your answer is",h,"Hour")
            g = (input("""Do you want Result in Text file
Choose the desired option in "Y" for Yes and "N" for NO:- """))
            if g == "Y" or g == "y":
                file = open("Time.txt", "w")
                file.write(str(s) + "Minutes in Hours is " + str(h) + "hrs")
                file.close()
                print("""Value uploaded in "Time.txt" file successfully.""")
            elif g == "N" or g == "n":
                print("Thank You!!")
            else:
                print("Invalid key pressed")

#5
        elif z==5:
            def gta():
                d=s*60
                return d
            s=int(input("Enter the Time in Hour:- "))
            j=gta()
            print("Your answer is",j,"Minutes")
            g = (input("""Do you want Result in Text file
Choose the desired option in "Y" for Yes and "N" for NO:- """))
            if g == "Y" or g == "y":
                file = open("Time.txt", "w")
                file.write(str(s) + "Hour in Minutes is " + str(j) + "min")
                file.close()
                print("""Value uploaded in "Time.txt" file successfully.""")
            elif g == "N" or g == "n":
                print("Thank You!!")
            else:
                print("Invalid key pressed")
        # 2
    else:
        print("Invalid key pressed")
# 2.Time to convert:- END
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Ending Statements
elif a=="n" or a=="N":
    print("""Have a nice day!!!
Goodbye!!!""")
else:
    print("Invalid key pressed")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx