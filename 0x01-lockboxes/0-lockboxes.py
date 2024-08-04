#!/usr/bin/python3
"""Solves the lock boxes puzzle"""

def find_next_box_to_check(opened_boxes):
    """
    Finds the next box that is opened but not yet checked for keys.

    Args:
        opened_boxes (dict): Dictionary containing information about boxes that have been opened.

    Returns:
        list: List of keys found in the next box to be checked, or None if no such box exists.
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'checked'
            return box.get('keys')
    return None


def can_unlock_all_boxes(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list): List of lists, where each sublist contains the keys for the corresponding box.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    opened_boxes = {}
    while True:
        if len(opened_boxes) == 0:
            opened_boxes[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = find_next_box_to_check(opened_boxes)
        if keys:
            for key in keys:
                if key < len(boxes):
                    if opened_boxes.get(key) and opened_boxes.get(key).get('status') == 'checked':
                        continue
                    opened_boxes[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
        elif 'opened' in [box.get('status') for box in opened_boxes.values()]:
            continue
        elif len(opened_boxes) == len(boxes):
            break
        else:
            return False

    return len(opened_boxes) == len(boxes)


def main():
    """Entry point"""
    print(can_unlock_all_boxes([[]]))  # Example usage


if __name__ == '__main__':
    main()

