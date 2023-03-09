import sys

# Initialize an empty dictionary to store the guest list and their RSVP status
guest_list = {}

# Function to get the guest list and their RSVP status
def get_guests():
    while True:
        try:
            # Get the guest name
            name = input("\nEnter guest name (or type 'done' to finish): ")
        # If the user presses Ctrl+C, exit the program
        except KeyboardInterrupt:
            sys.exit("\nProgram cancelled by user.\n")

        # If the user enters 'done', exit the loop
        if name.lower() == "done":
            break
        else:
            while True:
                # Get the guest's RSVP status
                rsvp = input("Will " + name + " attend the party? (Yes/No): ")
                # If the user presses Ctrl+C, exit the program
                if rsvp.lower() == "yes" or rsvp.lower() == "no":
                    break
                # If the user enters 'done', exit the loop
                else:
                    print("Invalid input. Please enter 'Yes' or 'No'.")
            # Add the guest to the guest list
            guest_list[name] = rsvp.lower()
    # Display the guest list and their RSVP status
    display_guest_list()

# Function to display the guest list and their RSVP status
def display_guest_list():
    # Print the number of guests invited and the number of guests confirmed
    print("\nNumber of guests invited: " + str(len(guest_list)))
    confirmed = 0
    # Loop through the guest list and count the number of guests confirmed
    for name, rsvp in guest_list.items():
        # If the guest has confirmed their attendance, increment the confirmed counter
        if rsvp == "yes":
            confirmed += 1
    # Print the number of guests confirmed and the number of guests not confirmed
    print("Number of guests confirmed: " + str(confirmed))
    print("Number of guests not confirmed: " + str(len(guest_list) - confirmed))

    while True:
        # Print the guest list and their RSVP status
        print("\nGuest list and RSVP status:")
        for name, rsvp in guest_list.items():
            # If the guest has confirmed their attendance, print their name and RSVP status
            print(name + ": " + rsvp)
        # Get the name of the guest to modify their RSVP status
        name = input("\nSelect a guest to modify their RSVP status (or type 'done' to finish): ")
        if name.lower() == "done":
            # If the user enters 'done', exit the loop
            break
        # If the guest is in the guest list, modify their RSVP status
        elif name in guest_list:
            while True:
                # Get the guest's new RSVP status
                new_rsvp = input("Will " + name + " attend the party? (Y/N): ")
                # If the user presses Ctrl+C, exit the program
                if new_rsvp.lower() == "y":
                    # If the guest has not confirmed their attendance, add them to the guest list
                    if guest_list[name] == "no":
                        # Add the guest to the guest list
                        guest_list[name] = "yes"
                        # Print the guest's name and RSVP status
                        print(name + " has been added to the guest list.")
                    else:
                        # Update the guest's RSVP status
                        update_details(name)
                    break
                # If the user enters 'done', exit the loop
                elif new_rsvp.lower() == "n":
                    # If the guest has confirmed their attendance, remove them from the guest list
                    if guest_list[name] == "yes":
                        # Remove the guest from the guest list
                        guest_list.pop(name)
                        # Print the guest's name and RSVP status
                        print(name + " has been removed from the guest list.")
                    else:
                        # Update the guest's RSVP status
                        print(name + " was already not attending the party.")
                    break
                else:
                    # If the user enters an invalid input, print an error message
                    print("Invalid input. Please enter 'Y' or 'N'.")
        else:
            # If the guest is not in the guest list, print an error message
            print("Guest not found. Please try again.")

# Function to update the guest's RSVP status
def update_details(name):
    while True:
        # Get the guest's new RSVP status
        new_rsvp = input(name + " has already confirmed their attendance. Do you want to modify their details? (Y/N): ")
        # If the user presses Ctrl+C, exit the program
        if new_rsvp.lower() == "y":
            while True:
                # Get the guest's new RSVP status
                rsvp = input("Will " + name + " attend the party? (Y/N): ")
                # If the user presses Ctrl+C, exit the program
                if rsvp.lower() == "y" or rsvp.lower() == "n":
                    # Update the guest's RSVP status
                    guest_list[name] = "yes" if rsvp.lower() == "y" else "no"
                    # Print the guest's name and RSVP status
                    print(name + "'s details have been updated.")
                    break
                else:
                    # If the user enters an invalid input, print an error message
                    print("Invalid input. Please enter 'Y' or 'N'.")
            break
        # If the user enters 'done', exit the loop
        elif new_rsvp.lower() == "n":
            break
        else:
            # If the user enters an invalid input, print an error message
            print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    get_guests()
