#!/usr/bin/python3
'''0-lockboxes'''


def canUnlockAll(boxes):
    # Set to keep track of opened boxes
    opened_boxes = {0}

    # List to keep track of keys found
    keys_found = set(boxes[0])

    # Continue until no new keys are found
    while keys_found:
        # Get a key from the set
        key = keys_found.pop()

        # Check if the key opens a new box
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys_found.update(boxes[key])

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
