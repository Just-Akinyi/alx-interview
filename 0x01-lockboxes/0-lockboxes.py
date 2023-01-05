#!/usr/bin/python3
'''canUnlockAll'''
def canUnlockAll(boxes):
    '''
    Args:
        boxes: list
    '''
    # Step 1
    boxes_set = set(range(len(boxes)))

    # Step 2
    keys = set(boxes[0])

    # Step 3
    while keys:
        key = keys.pop()
        if key in boxes_set:
            boxes_set.remove(key)
            keys.update(boxes[key])

    # Step 4
    return not boxes_set
