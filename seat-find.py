# DSCM4L3 After Class Project: My Train Seat Finder (starter)
# How to run: python3 seat_finder.py, or paste into one Google Colab cell and press Run.
# Lines marked (given) are done for you. Your job is TODO 1 to TODO 3. Do them in order.
# Each TODO ends with a Check line: run the file after every TODO and compare.
# If the program never stops, press Ctrl+C (Colab: the Stop button) and check that
# low or high changes in every round. Errors appear at the bottom of the output.
# The free seats of a train coach are sorted. Find a seat two ways: a loop and recursion.
# Count the checks of the loop and the depth of the recursion (calls waiting at once).


def find_seat(seats, target):
    """Binary search with a loop. Returns (index or -1, checks)."""
    low, high, checks = 0, len(seats) - 1, 0
    # TODO 1: Binary search with a loop, as in class: find mid, count the check, return
    #         when seats[mid] is the target, otherwise keep the half it can be in.
    #         Check: seat 130 is at index 7 after 4 loop checks.
    mid = (low + high) //2

    while(seats[mid] <= target):
      if(seats[mid] == target):
          return checks
      else:
          low = low + 1
          high = high - 1


    return -1, checks


def find_seat_recursive(seats, target, low, high, depth):
    """Binary search that calls itself on one half. Returns (index or -1, depth)."""
    if low > high:  # (given) B: base case, nothing left to search
        return -1, depth
    mid = (low + high) // 2
    # TODO 2: If the middle seat is the target, send back mid and the current depth.
    #         Check: seat 130 is found by the recursion (index 7 on both sides).
    if(seats[mid] == target):
            mid = mid - 1
            depth = depth - 1
    # TODO 3: Recursive case: call find_seat_recursive on the right half (if seats[mid]
    #         is too small) or on the left half, one level deeper, and send back its answer.
    #         Check: seat 130 shows recursion depth = 4; seat 133 shows depth = 5.

    if(seats[mid] == target):
                mid = mid - 1
                depth = depth - 1

# (given) A: the sorted free seats and four seats to look for (133 is not free).
seats = [101, 104, 108, 112, 115, 120, 125, 130, 135, 140, 145, 150]
print("Free seats:", seats)
for target in [130, 101, 150, 133]:
    index, checks = find_seat(seats, target)
    rindex, depth = find_seat_recursive(seats, target, 0, len(seats) - 1, 1)
    if index == -1:
        print("Seat", target, ": not free   loop checks =", checks, "  recursion depth =", depth)
    else:
        print("Seat", target, ": index", index, "  loop checks =", checks, "  recursion depth =", depth)
print("Same answers with", len(seats), "seats. Loop: O(log n) time, O(1) extra space.")
print("Recursion: O(log n) time, O(log n) extra space (one waiting call per halving).")
print("Empty coach:", find_seat([], 120), find_seat_recursive([], 120, 0, -1, 1))
