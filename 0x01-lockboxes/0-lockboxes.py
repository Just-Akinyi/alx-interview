#!/usr/bin/python3
'''defines canUnlockAll function'''


def canUnlockAll(boxes):
    '''
    Args:
        boxes: list
    returns:
        True or False
    '''
    # Set of boxes that have been visited
    visited = set()

    # Queue for boxes that need to be checked
    queue = [0]

    # While there are boxes in the queue
    while queue:
        # Get the next box to check
        box = queue.pop(0)

        # If the box has not been visited
        if box not in visited:
            # Mark the box as visited
            visited.add(box)

            # Add the keys in the box to the queue
            queue.extend(boxes[box])

    # Return whether all boxes have been visited
    return len(visited) == len(boxes)
