#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Parameters:
    boxes (list of lists): List of lists where each sublist contains keys for other boxes.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False
    
    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    stack = [0]  # Use a stack for DFS

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n

if __name__ == "__main__":
    # Test cases
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected output: False

