import time

# Sample list of fish (contains a duplicate: "Tilapia")
fish_list = ["Tilapia", "Captain", "Omena", "Nile perch", "Mud fish", "Cat fish", "Tilapia"]

def duplicates(fish_list):
    """
    Checks if a list contains duplicate values.

    Args:
        fish_list (list): List of fish names

    Returns:
        list: [True/False, execution time string]
              True  -> duplicate found
              False -> no duplicates
    """

    # Start timing execution
    start_time = time.time()

    # Set to store already seen items (sets only allow unique values)
    checked = set()

    # Loop through each fish in the list
    for fish in fish_list:

        # If fish is already in the set, it's a duplicate
        if fish in checked:
            print(f"{fish} found twice")

            # End timing
            end_time = time.time()
            total_time = round(end_time - start_time, 5)

            return [True, f"Took {total_time} seconds"]

        else:
            # First time seeing this fish
            print(f"{fish} appeared once... moving on")
            checked.add(fish)

    # If loop completes, no duplicates were found
    end_time = time.time()
    total_time = round(end_time - start_time, 5)

    return [False, f"Took {total_time} seconds"]


# Run the function
print(duplicates(fish_list))