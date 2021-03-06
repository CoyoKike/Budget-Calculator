while True:
  
  language = input("""Please select your language -
   1) English 
   2) Spanish - """)
  if language.lower() == "english" or language == "1":
    
    while True:
      print("\n---Breaking Down Your Income---")
      print("""Welcome to the Budget Calculator, this is a tool that will help you create a monthly income so you can allocate money to your needs, savings and wants!. If you think that this budget doesn't reflect your situation, please feel free to contact us to schedule a Free Financial Coaching session!""")
      your_income = input("\nPlease enter the monthly income that you would like to breakdown:")
      try:
        your_income = float(your_income)
      except:
        print("\nPlease enter a valid number")
        continue

      if your_income > 0:
        needs = your_income*0.5
        savings = your_income*0.2
        wants = your_income*0.3
        print("You entered a total income of:", "${:,.2f}".format(your_income), """Here is a suggested budget for your income: """)
      while True:
        choice_menu = input("""\nWhat would you like to know?
        1) How much money should I spend in needs?
        2) How much money should I be saving?
        3) How much money can I spend in wants?
        4) Enter a different amount
        5) Exit
        """)
      

        if choice_menu == "1":
            print("""\nThis section includes things that you and your family require such as rent, utilities, groceries, medical bills, etc. Based on your income, you should allocate the following ammount for your needs: """, "\nNeeds =", "${:,.2f}".format(needs), "\nPress Enter to continue")
            input()
        elif choice_menu == "2":
          print("""\nYou should be putting some money away in a savings account or investing every month, this will help you build your wealth and prepare for emergencies""", "\nSavings/Investment =", "${:,.2f}".format(savings), "\nPress Enter to continue")
          input()
        elif choice_menu == "3":
          print("""\nMoney! This is the amount that you can give yourself to spend on the things that you want. Remember to cover your needs and savings before spending this money""","\nWants! = ","${:,.2f}".format(wants), "\nPress Enter to continue")
          input()
        elif choice_menu == "4":
          break
        elif choice_menu == "5":
            quit()
        else:
          "Please enter a valid option"

      choice = input("Would you like to breakdown another amount? y/n: ")
      if choice.lower() == "y":
        continue
      else:
        break

    else:
        print("Please enter an amount larger than 0, try again. ")

  elif language.lower() == "spanish" or language.lower() == "espanol" or language == "2":
    while True:
      print("\n---An??lisis de su Ingreso Mensual---")
      print("""
??Bienvenido a la Calculadora de Presupuesto, esta es una herramienta que te ayudar?? a crear un ingreso mensual para que puedas destinar dinero a tus necesidades, ahorros y deseos!. Si cree que este presupuesto no refleja su situaci??n, ??no dude en contactarnos para programar una sesi??n gratuita de asesoramiento financiero!""")
      your_income = input("\nPor favor ingrese el ingreso mensual que le gustar??a analizar:")
      try:
        your_income = float(your_income)
      except:
        print("\nPor favor ingrese una cantidad v??lida")
        continue

      if your_income > 0:
        necesidades = your_income*0.5
        ahorros = your_income*0.2
        deseos = your_income*0.3
      
        print("Usted ingres?? la cantidad de:", "${:,.2f}".format(your_income), "Aqu?? le presentamos un desglose de como puede repartir sus ingresos: ")

        while True:
          choice_menu = input("""\nWhat would you like to know?
        1) Cu??nto dinero deber??a destinar a mis necesidades?
        2) Cu??nto dinero deber??a de ahorrar o invertir?
        3) Cu??nto dinero puedo destinar a mis deseos?
        4) Ingresar otra cantidad
        5) Salir
        """)
      

          if choice_menu == "1":
            print("""\nEsta secci??n incluye las cosas que usted ysu familia requiren tales como la renta, hipoteca, comida, luz, gas, etc. Bas??ndonos en su ingreso usted deber??a destinar la siguiente cantidad a sus necesidades: ""","Necesidades =", "${:,.2f}".format(necesidades))
            input("\nPresione Enter para continuar")
          elif choice_menu == "2":
            print("""\nEsta cantidad deber??a ser depositada en una cuenta de ahorros o invertida en el mercado cada semana. Esto le ayudar?? a contruir su prosperidad y prepararse para emergencias.""","\nDe acuerdo a su ingres mensual, se le recomienda ahorrar o invertir la siguiente cantidad. Ahorros e Inversiones =" "${:,.2f}".format(ahorros))
            input("\nPresione Enter para continuar")
          elif choice_menu == "3":
            print("""Dinero! Este es el dinero que se puede dar a usted mismo para comprar las cosas que le gustan. Aseg??rese de que ha pagado sus necesidades y ahorros antes de gastar este dinero.""","\nDeseos! = ","${:,.2f}".format(deseos))
            input("\nPresione Enter para continuar")
          elif choice_menu == "4":
            break
          elif choice_menu == "5": 
              quit()
          else:
            print("\nPor favor ingrese una cantidad v??lida")

        choice = input("\nLe gustar??a analizar otra cantidad? s/n: ")
        if choice.lower() == "s":
          continue
        else:
          break

  else:
    print("\nSorry, we currently don't provide services in that language")

