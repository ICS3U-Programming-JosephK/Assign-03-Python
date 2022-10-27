#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: Oct 12
# This program compares your income to the national average and provincial average


# imports constants since there are no constants in python
import constants


def main():

    # asks the user for input (their income), the input "income" can be an integer, negative, or decimal
    print(
        "This program will compare your income to the national average and the selected province"
    )

    user_income = input("Enter your income in $: ")

    # process and output, check the income input
    try:
        user_income = float(user_income)

    # similar to an else statement, if a number is not inputted...
    except:
        print("You must enter a number (decimals and negatives allowed)")

        # Restarts program after any key is entered
        wait = input("Enter any key to restart: ")
        return main()

    # list of provinces show to the user to pick, end= was used to avoid spaghetti code
    print(
        "List of provinces:\nNunavut - 1\nNorthwest Territories - 2\nAlberta - 3\nYukon - 4\n",
        end="",
    )
    print(
        "Ontario - 5\nNewfoundland and Labrador - 6\nSaskatchewan - 7\nBritish Columbia - 8\n",
        end="",
    )
    print(
        "Quebec - 9\nManitoba - 10\nNew Brunswick - 11\nNova Scotia - 12\n Prince Edward Island - 13\n",
        end="",
    )

    # ask the user for their province by selecting a province's number
    user_province = input("What province are you from (select number): ")

    # If the user chose this "province", apply the following if statements
    if user_province == "1":
        if user_income >= constants.INCOME and user_income >= constants.NUNAVUT:
            print(
                "Your income is above or equal to the national average and Nunavut's average"
            )

        elif user_income <= constants.INCOME and user_income <= constants.NUNAVUT:
            print(
                "Your income is lower or equal to the national average and Nunavut's average"
            )

        elif user_income >= constants.INCOME and user_income <= constants.NUNAVUT:
            print(
                "Your income is higher than the national average but lower than Nunavut's average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "2":
        if (
            user_income >= constants.INCOME
            and user_income >= constants.NORTHWEST_TERRITORIES
        ):
            print(
                "Your income is above or equal to the national average and Northwest Territories' average"
            )

        elif (
            user_income <= constants.INCOME
            and user_income <= constants.NORTHWEST_TERRITORIES
        ):
            print(
                "Your income is lower or equal to the national average and Northwest Territories' average"
            )

        elif (
            user_income >= constants.INCOME
            and user_income <= constants.NORTHWEST_TERRITORIES
        ):
            print(
                "Your income is higher than the national average but lower than Northwest Territories' average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "3":
        if user_income >= constants.INCOME and user_income >= constants.ALBERTA:
            print(
                "Your income is above or equal to the national average and Alberta's average"
            )

        elif user_income <= constants.INCOME and user_income <= constants.ALBERTA:
            print(
                "Your income is lower or equal to the national average and Alberta's average"
            )

        elif user_income >= constants.INCOME and user_income <= constants.ALBERTA:
            print(
                "Your income is higher than the national average but lower than Alberta's average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "4":
        if user_income >= constants.INCOME and user_income >= constants.YUKON:
            print(
                "Your income is above or equal to the national average and yukon's average"
            )

        elif user_income <= constants.INCOME and user_income <= constants.YUKON:
            print(
                "Your income is lower or equal to the national average and yukon's average"
            )

        elif user_income >= constants.INCOME and user_income <= constants.YUKON:
            print(
                "Your income is higher than the national average but lower than yukon's average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "5":
        if user_income >= constants.INCOME and user_income >= constants.ONTARIO:
            print(
                "Your income is above or equal to the national average and Ontario's average"
            )

        elif user_income <= constants.INCOME and user_income <= constants.ONTARIO:
            print(
                "Your income is lower or equal to the national average and Ontario's average"
            )

        elif user_income <= constants.INCOME and user_income >= constants.ONTARIO:
            print(
                "Your income is lower than the national average but higher than Ontario's average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "6":
        if (
            user_income >= constants.INCOME
            and user_income >= constants.NEWFOUNDLAND_AND_LABRADOR
        ):
            print(
                "Your income is above or equal to the national average and Newfoundland and Labrador's average"
            )

        elif (
            user_income <= constants.INCOME
            and user_income <= constants.NEWFOUNDLAND_AND_LABRADOR
        ):
            print(
                "Your income is lower or equal to the national average and Newfoundland and Labrador's average"
            )

        elif (
            user_income <= constants.INCOME
            and user_income >= constants.NEWFOUNDLAND_AND_LABRADOR
        ):
            print(
                "Your income is lower than the national average but higher than Newfoundland and Labrador's average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "7":
        if user_income >= constants.INCOME and user_income >= constants.SASKATCHEWAN:
            print(
                "Your income is above or equal to the national average and Saskatchewan's average"
            )

        elif user_income <= constants.INCOME and user_income <= constants.SASKATCHEWAN:
            print(
                "Your income is lower or equal to the national average and Saskatchewan's average"
            )

        elif user_income <= constants.INCOME and user_income >= constants.SASKATCHEWAN:
            print(
                "Your income is lower than the national average but higher than Saskatchewan's average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "8":
        if (
            user_income >= constants.INCOME
            and user_income >= constants.BRITISH_COLUMBIA
        ):
            print(
                "Your income is above or equal to the national average and British Columbia's average"
            )

        elif (
            user_income <= constants.INCOME
            and user_income <= constants.BRITISH_COLUMBIA
        ):
            print(
                "Your income is lower or equal to the national average and British Columbia's average"
            )

        elif (
            user_income <= constants.INCOME
            and user_income >= constants.BRITISH_COLUMBIA
        ):
            print(
                "Your income is lower than the national average but higher than British Columbia's average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "9":
        if user_income >= constants.INCOME and user_income >= constants.QUEBEC:
            print(
                "Your income is above or equal to the national average and Quebec's average"
            )

        elif user_income <= constants.INCOME and user_income <= constants.QUEBEC:
            print(
                "Your income is lower or equal to the national average and Quebec's average"
            )

        elif user_income <= constants.INCOME and user_income >= constants.QUEBEC:
            print(
                "Your income is lower than the national average but higher than Quebec's average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "10":
        if user_income >= constants.INCOME and user_income >= constants.MANITOBA:
            print(
                "Your income is above or equal to the national average and Manitoba's average"
            )

        elif user_income <= constants.INCOME and user_income <= constants.MANITOBA:
            print(
                "Your income is lower or equal to the national average and Manitoba's average"
            )

        elif user_income <= constants.INCOME and user_income >= constants.MANITOBA:
            print(
                "Your income is lower than the national average but higher than Manitoba's average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "11":
        if user_income >= constants.INCOME and user_income >= constants.NEW_BRUNSWICK:
            print(
                "Your income is above or equal to the national average and New Brunswick's average"
            )

        elif user_income <= constants.INCOME and user_income <= constants.NEW_BRUNSWICK:
            print(
                "Your income is lower or equal to the national average and New Brunswick's average"
            )

        elif user_income <= constants.INCOME and user_income >= constants.NEW_BRUNSWICK:
            print(
                "Your income is lower than the national average but higher than New Brunswick's average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "12":
        if user_income >= constants.INCOME and user_income >= constants.NOVA_SCOTIA:
            print(
                "Your income is above or equal to the national average and Nova Scotia's average"
            )

        elif user_income <= constants.INCOME and user_income <= constants.NOVA_SCOTIA:
            print(
                "Your income is lower or equal to the national average and Nova Scotia's average"
            )

        elif user_income <= constants.INCOME and user_income >= constants.NOVA_SCOTIA:
            print(
                "Your income is lower than the national average but higher than Nova Scotia's average"
            )

    # If the user chose this "province", apply the following if statements
    elif user_province == "13":
        if user_income >= constants.INCOME and user_income >= constants.PEI:
            print(
                "Your income is above or equal to the national average and PEI's average"
            )

        elif user_income <= constants.INCOME and user_income <= constants.PEI:
            print(
                "Your income is lower or equal to the national average and Nova PEI's average"
            )

        elif user_income <= constants.INCOME and user_income >= constants.PEI:
            print(
                "Your income is lower than the national average but higher than PEI's average"
            )

    # else, if none of the of the if statement's requirements were met, print the following
    else:
        print("Enter a valid Canadian province (just the number)")


if __name__ == "__main__":
    main()
    # give the user to try again using "y" or "n"
    answer = input("Would you like to try again? (y/n): ")
    while answer == "y":
        main()
        answer = input("Would you like to try again? (y/n): ")
