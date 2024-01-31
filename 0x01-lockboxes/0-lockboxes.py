#!/usr/bin/python3
"""
Module to determine the fewest number of boxes needed
    to meet a given amount total"
"""


def canUnlockAll(boxes):
    # Set to keep track of opened boxes
    opened_boxes = set()

    # Queue for BFS, starting with first box
    queue = [0]

    while queue:
        present_box = queue.pop(0)

        # If the current box is not opened yet
        if present_box not in opened_boxes:
            opened_boxes.add(present_box)

            # Add keys from the current box to the queue
            queue.extend(boxes[present_box])

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
