Projects = {}
while True:
    print("1. Initiate a project\n"
          "2. Delete a project\n"
          "3. Update a project\n"
          "4. Print a specific project\n"
          "5. Print all projects\n"
          "Type any other number to quit\n")
    Option = int(input("Type any number of your choice"))
    if Option == 1:
        id = input("Type project id")
        ptitle = input("Type title of project")
        num = int(input("How many managers do you have?"))
        manager = []
        for i in range (0, num):
            manager.append(input("Type manager name"))


        sdate = input("Type the starting date")
        edate = input("Type the ending date")

        num = int(input("How many sponsors do you have?"))
        sponsor = []
        for i in range(0, num):
            sponsor.append(input("Type sponsor name"))


        budget = input("Type the budget")

        num = int(input("How many technology do you have?"))
        tech = []
        for i in range(0, num):
            tech.append(input("Type technology name"))

        num = int(input("How many members do you have?"))
        member = []
        for i in range(0, num):
            member.append(input("Type member name"))

        Projects.update({id:{"Title":ptitle, "Managers":manager,
                             "startingDate":sdate, "endingDate":edate,
                             "Sponsor":sponsor, "budget":budget,
                             "Technology":tech, "Members":member}})

    elif Option == 2:
        del Projects[input("What is the project id you want to delete?")]

    elif Option == 3:
        id = input("Type project id to edit")
        while True:
            print("1. Title\n 2. Managers\n 3. Starting Date\n 4. Ending Date\n 5. Sponsor\n 6. Budget\n 7. Technology\n 8. Members\n Type any other number to end")
            Option = int(input("Choose your Options"))
            if Option == 1:
                Projects[id]["Title"] = input("Type new Title")

            elif Option == 2:
                num = int(input("How many managers do you have?"))
                manager = []
                for i in range(0, num):
                    manager.append(input("Type manager name"))

                Projects[id]["Managers"] = manager

            elif Option == 3:
                Projects[id]["startingDate"] = input("Type new Starting Date")

            elif Option == 4:
                Projects[id]["endingDate"] = input("Type new Ending Date")

            elif Option == 5:
                num = int(input("How many sponsors do you have?"))
                sponsor = []
                for i in range(0, num):
                    sponsor.append(input("Type sponsor name"))

                Projects[id]["Sponsor"] = sponsor

            elif Option == 6:
                Projects[id]["budget"] = input("Type new budget")

            elif Option == 7:
                num = int(input("How many technology do you have?"))
                tech = []
                for i in range(0, num):
                    tech.append(input("Type technology name"))

                Projects[id]["Technology"] = tech

            elif Option == 8:
                num = int(input("How many technology do you have?"))
                member = []
                for i in range(0, num):
                    member.append(input("Type member name"))

                Projects[id]["Member"] = member
            else:
                break


    elif Option == 4:
        print(Projects[input("Type project id")])

    elif Option == 5:
        print(Projects)

    else:
        break
