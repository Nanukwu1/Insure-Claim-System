# ============================================
# INSURE CLAIM TRACKER SYSTEM
# Authors: Nini Anukwu, Gopi Kacha, Jordan Davis, Chinelo Aniekwu
# Description:
# This program allows users to manage insurance claims
# using Create, Read, Update, and Delete (CRUD) operations.
# Data is stored in a CSV file.
# ============================================


import os

FILE_NAME = "claims.csv"


# --------------------------------------------
# Initialize the CSV file if it does not exist
# --------------------------------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("Claim ID,Patient Name,Amount,Status\n")


# --------------------------------------------
# Add a new claim to the system
# --------------------------------------------
def add_claim():
    print("\n--- Add Claim ---")

    try:
        claim_id = input("Enter Claim ID: ").strip()
        name = input("Enter Patient Name: ").strip()
        amount = input("Enter Claim Amount: ").strip()
        status = input("Enter Claim Status: ").strip()
    except KeyboardInterrupt:
        print("\nInput interrupted. Returning to menu.")
        return

    # Validate input
    if claim_id == "" or name == "" or amount == "" or status == "":
        print("Error: All fields are required.")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{claim_id},{name},{amount},{status}\n")

    print("Claim added successfully.")


# --------------------------------------------
# View all claims
# --------------------------------------------
def view_claims():
    print("\n--- All Claims ---")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

            if len(lines) <= 1:
                print("No claims found.")
                return

            for line in lines:
                print(line.strip())

    except FileNotFoundError:
        print("Error: File not found.")


# --------------------------------------------
# Update an existing claim
# --------------------------------------------
def update_claim():
    print("\n--- Update Claim ---")

    try:
        claim_id = input("Enter Claim ID to update: ").strip()
    except KeyboardInterrupt:
        print("\nInput interrupted. Returning to menu.")
        return

    updated = False

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(FILE_NAME, "w") as file:
            for line in lines:
                data = line.strip().split(",")

                if data[0] == "Claim ID":
                    file.write(line)
                    continue

                if data[0] == claim_id:
                    print("Updating claim...")
                    try:
                        name = input("Enter new Patient Name: ").strip()
                        amount = input("Enter new Amount: ").strip()
                        status = input("Enter new Status: ").strip()
                    except KeyboardInterrupt:
                        print("\nUpdate cancelled.")
                        return

                    file.write(f"{claim_id},{name},{amount},{status}\n")
                    updated = True
                else:
                    file.write(line)

        if updated:
            print("Claim updated successfully.")
        else:
            print("Error: Claim ID not found.")

    except FileNotFoundError:
        print("Error: File not found.")


# --------------------------------------------
# Delete a claim
# --------------------------------------------
def delete_claim():
    print("\n--- Delete Claim ---")

    try:
        claim_id = input("Enter Claim ID to delete: ").strip()
    except KeyboardInterrupt:
        print("\nInput interrupted. Returning to menu.")
        return

    deleted = False

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(FILE_NAME, "w") as file:
            for line in lines:
                data = line.strip().split(",")

                if data[0] == "Claim ID":
                    file.write(line)
                    continue

                if data[0] == claim_id:
                    deleted = True
                    continue
                else:
                    file.write(line)

        if deleted:
            print("Claim deleted successfully.")
        else:
            print("Error: Claim ID not found.")

    except FileNotFoundError:
        print("Error: File not found.")


# --------------------------------------------
# Main menu for user interaction
# --------------------------------------------
def menu():
    while True:
        print("\n--- Insure Claim Tracker ---")
        print("1. Add Claim")
        print("2. View Claims")
        print("3. Update Claim")
        print("4. Delete Claim")
        print("5. Exit")

        try:
            choice = input("Select an option: ").strip()
        except KeyboardInterrupt:
            print("\nProgram interrupted safely. Exiting.")
            break

        if choice == "1":
            add_claim()
        elif choice == "2":
            view_claims()
        elif choice == "3":
            update_claim()
        elif choice == "4":
            delete_claim()
        elif choice == "5":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")


# --------------------------------------------
# Run the program
# --------------------------------------------
if __name__ == "__main__":
    initialize_file()
    menu()