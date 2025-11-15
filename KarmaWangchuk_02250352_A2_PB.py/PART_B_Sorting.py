
# --- Bubble Sort Function (sorts names alphabetically) --
def Bubble_sort(arr):   
    n = len(arr)        # Get total number of elements in the list
    for i in range(n):       # Outer loop for passes
        swapped = False     # Track if any swap occurred during this pass
        for j in range(0, n-i-1):       # Inner loop for comparing adjacent elements
            if arr[j] > arr[j+1]:       # Compare alphabetically (case-insensitive)
                arr[j], arr[j+1] = arr[j+1], arr[j]     # Swap if out of order
                swapped = True      # Mark that a swap occurred
        if not swapped:     # If no swaps in this pass → list is already sorted
            break
    return arr      # Return the sorted list

# --- Insertion Sort Function (sorts scores numerically) ---
def Insertion_sort(arr):
    n = len(arr)        # Length of list
    for i in range(1, n):       # Start from 2nd element
        key = arr[i]        # Element to insert in sorted part
        j = i - 1       # Index of previous element
        while j >= 0 and key < arr[j]:      # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key        # Insert key at correct position
    return arr      # Return sorted list

# --- Quick Sort Function (sorts prices, counts recursive calls) ---
def Quick_sort(arr, calls = 0):
    calls += 1      # Count how many times function is called (recursion count)
    if len(arr) <= 1:       # Base case: list of length 0 or 1 is already sorted
        return arr, calls
    else:
        pivot = arr[len(arr) // 2]      # Choose middle element as pivot
        left = [x for x in arr if x < pivot]      # All elements smaller than pivot
        middle = [x for x in arr if x == pivot]     # All elements equal to pivot
        right = [x for x in arr if x > pivot]       # All elements greater than pivot

        # Recursively sort left and right parts, passing along the call counter
        left_sorted, calls = Quick_sort(left, calls)
        right_sorted, calls = Quick_sort(right, calls)
        
        # Combine the results and return both sorted list and total recursive calls
        return left_sorted + middle + right_sorted, calls

# --- Main Menu Function ---
def menu():
    # Hardcoded lists for sorting examples
    student_names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Cemo", "Deki", "Pema", "Tashi", "Kinzang",
                     "Sangay", "Chimi", "Phurba", "Wangdi", "Ugyen"]
    test_scores_unsorted = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 76, 85, 48, 93, 71, 89, 57, 80, 69, 60]
    book_prices = [450, 230, 678, 125, 890, 345, 210, 999, 410, 505, 150, 275, 320, 199, 600]

    # Start infinite loop for the sorting menu
    while True:
        print("\n=== Sorting Algorithms Menu ===")      # Menu header
        print("Select a sorting operation (1-4):")
        print("1. Bubble Sort - Sort Student Names")
        print("2. Insertion Sort - Sort Test Scores")
        print("3. Quick Sort - Sort Book Prices")
        print("4. Exit program")

        choice = input("Enter your choice (1-4): ").strip()     # Get user input and remove extra spaces

        # --- Option 1: Bubble Sort ---
        if choice == "1":
            print("Original:", student_names)       # Show unsorted names
            sorted_names = Bubble_sort(student_names)   # Sort names alphabetically
            print("Sorted:", sorted_names)      # Display sorted list

            # Ask user if they want to perform another sort
            again = input("Would you like to perform another sort? (y/n): ").strip().lower()
            if again != "y":        # Exit if not 'y'
                print("Thank you for using the sorting program!")
                break
        
        # --- Option 2: Insertion Sort ---
        elif choice == "2":
            print("Original scores:", test_scores_unsorted)     # Show unsorted scores
            sorted_scores = Insertion_sort(test_scores_unsorted)    # Sort using insertion sort
            print("Performing Insertion Sort...")       # Inform user
            print("Sorted scores:", sorted_scores)  # Display sorted list
            # Display top 5 scores (highest)
            top5 = sorted_scores[-5:][::-1]  # Take last 5 elements and reverse
            print("Top 5 Scores:")
            for i, score in enumerate(top5, start=1):      # Print numbered top scores
                print(f"{i}. {score}")

            # Ask if user wants to perform another sort
            again = input("Would you like to perform another sort? (y/n): ").strip().lower()
            if again != "y":
                print("Thank you for using the sorting program!")
                break

        # --- Option 3: Quick Sort ---
        elif choice == "3":
            print("Original prices:", book_prices)      # Show unsorted book prices
            sorted_prices, calls = Quick_sort(book_prices)      # Sort and count recursive calls
            print("Sorted prices:", sorted_prices)      # Display sorted prices
            print("Recursive calls:", calls)    # Display recursion count

            # Ask again for continuation
            again = input("Would you like to perform another sort? (y/n): ").strip().lower()
            if again != "y":
                print("Thank you for using the sorting program!")
                break
        # --- Option 4: Exit ---
        elif choice == "4":
            print("Exiting program. Thank you for using the search program!")
            break
        # --- Invalid Option ---
        else:
            print("Invalid choice. Please select a valid option (1-4).")

menu() #calling the menu funtion
