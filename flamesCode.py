from time import sleep

print("Welcome to FLAMES Automated Game")
sleep(1)
play_again = False

while not play_again:
    #Prompts the user for the names of the two players
    first_name = input("Enter the name of the first player: ")
    second_name = input("Enter the name of the second player: ")

    count1 = 0
    count2 = 0


    #Counts the number of letters in the two names
    for letter in first_name:
        if letter == " ":
            continue
        count1 += 1

    for letter in second_name:
        if letter == " ":
            continue
        count2 += 1

    sum = count1 + count2

    #Checks which letter in FLAMES(6 letters) the sum of the number of letters in the two names coincides with
    if sum % 6 == 0:
        print("S:", end=" ")
        print(first_name, "and", second_name, "are Secret Admirers.")

    elif sum % 6 == 1:
        print("F:", end=" ")
        print(first_name, "and", second_name, "are Friends.")

    elif sum % 6 == 2:
        print("L:", end=" ")
        print(first_name, "and", second_name, "are Lovers.")

    elif sum % 6 == 3:
        print("A:", end=" ")
        print(first_name, "and", second_name, "are Admirers.")

    elif sum % 6 == 4:
        print("M:", end=" ")
        print(first_name, "and", second_name, "are Married.")

    elif sum % 6 == 5:
        print("E:", end=" ")
        print(first_name, "and", second_name, "are Enemies.")
    print()

    response = input("Do you want to play again?(Yes/No): ")
    if response == "No" or response == "no":
        play_again = True
        break
    else:
        play_again = False

print("Thank you for playing FLAMES.")


    
    