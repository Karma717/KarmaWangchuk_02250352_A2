def Linear_search(arr, target):    # Defining a function 
    comparisons = 0             # to track number of comparisons
    for i, val in enumerate(arr):          # Loop through each element with its index
        comparisons += 1        # Add every comparison made
        if val == target:       # Check if current element matches the target
            return i + 1, comparisons       # If found return position (1-indexed) and comparison count
    return None, comparisons         # If not found, return None and total comparisons

def Binary_search(arr, target):     # Defining the function
    left, right = 0, len(arr) - 1       # starting ans ending index of the array
    comparisons = 0         # To track the number of comparisons
    while left <= right:        # Continue searching while valid range exists
        mid = (left + right) // 2            # Find middle index
        comparisons += 1            # Add every comparison made
        if arr[mid] == target:      # If middle element matches target
            return mid + 1, comparisons        # Return position (1-indexed) and comparison count
        elif arr[mid] < target:     # If target is larger, search right half
            left = mid + 1          #adds mid index by 1
        else:
            right = mid - 1         #subtracts mid index by 1
    return None, comparisons         # If not found, return None and total comparisons

def Menu(): #defining the menu function with 6 options
    # Hardcoded 20 student IDs (Unsorted)
    student_ids = [1001, 1005, 1003, 1008, 1002, 1007, 1004, 1010, 1006, 1009,
                   1011, 1015, 1013, 1018, 1012, 1014, 1017, 1020, 1016, 1019]
    # Hardcoded 20 scores (Sorted)
    sorted_scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 88, 90, 92, 95, 98,
                     100, 102, 105, 108, 110]
    while True:
        print("\n----Searching Algorithm Menu----")   # printing the menu title
        print("Select a search operation (1-3):")      # giving the user options to choose from
        print("1. Linear Search - Find Student ID")
        print("2. Binary Search - Find Score")
        print("3. exit the program")     # giving options to exit the program

        choice = input("Enter your choice (1-3): ").strip() # .strip()- removes extra spaces

        if choice == "1":    # --- Option 1: Linear Search ---
            while True:
                print("Searching in the list :", student_ids)      # Show data being searched
                try:        # Ask user for the target ID to search
                    target = int(input("Enter the ID that you want to search: ").strip())
                except ValueError:      # Handle invalid (non-integer) input
                    print("Invalid input. Please enter a valid integer student ID.")
                    continue        # Restart loop and ask again
                position, comparisions = Linear_search(student_ids, target) # Call linear search function
                if position is not None:    # Display results based on whether target was found
                    print(f"   Result: Student ID {target} found at position {position} with {comparisions} comparisons.")
                else:
                    print(f"   Result: Student ID {target} not found after {comparisions} comparisons.")
                    # Ask user if they want try again
                again = input("Do you want to try again? (y/n): ").strip().lower()
                if again != "y":    # If not 'y', exit
                    break
                # Ask user if they want to perform another search
            another = input("Would you like to perform another search? (y/n): ").strip().lower()
            if another != "y":      # If not 'y', exit program
                print("Thank you for using the search program!")
                break

        elif choice == "2":     # --- Option 2: Binary Search ---
            while True:
                print(f"Sorted scores:{sorted_scores}")    # Show sorted list for binary search
                try:    # Ask user for the score to search
                    target = int(input("Enter the score that you want to search: ").strip())
                except ValueError:      # Handle non-numeric input
                    print("Invalid input. Please enter a valid integer score.")
                    continue        # Restart loop
                position, comparisions = Binary_search(sorted_scores, target)   # Call binary search function
                if position is not None:        # Display results
                    print(f"   Result: Score {target} found at position {position} with {comparisions} comparisons.")
                else:
                    print(f"   Result: Score {target} not found after {comparisions} comparisons.")
                # Ask user if they want try again
                again = input("Do you want to try again? (y/n): ").strip().lower()
                if again != "y":    # Ask user if they want try again
                    break
                # Ask user if they want to continue searching
            another = input("Would you like to perform another search? (y/n): ").strip().lower()
            if another != "y":      # If not 'y', exit program
                print("Thank you for using the search program!")
                break
        # --- Option 3: Exit Program ---
        elif choice == "3":
            print("Exiting program. Thank you for using the search program!") # Exit message
            break
        else:
            print("Invalid choice. Please select a valid option (1-3).")

Menu()  # calling the menu function to start the program
