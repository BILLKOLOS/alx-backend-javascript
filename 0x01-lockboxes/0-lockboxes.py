#!/usr/bin/python3
"""
This module provides a function to determine if all boxes can be opened.
"""

def canUnlockAll(boxes):
        """
            Determine if all boxes can be opened.

                Args:
                        boxes (list of list): A list of lists representing the boxes and their keys.

                            Returns:
                                    bool: True if all boxes can be opened, False otherwise.
                                        """

                                            n = len(boxes)  # Total number of boxes
                                                visited = set()  # Set to keep track of visited boxes

                                                    def dfs(box):
                                                                visited.add(box)
                                                                        for key in boxes[box]:
                                                                                        if key not in visited:
                                                                                                            dfs(key)

                                                                                                                dfs(0)  # Start DFS from the first box (boxes[0])

                                                                                                                    return len(visited) == n

                                                                                                                if __name__ == "__main__":
                                                                                                                        # Example usage:
                                                                                                                            boxes1 = [[1], [2], [3], [4], []]
                                                                                                                                print(canUnlockAll(boxes1))  # Output: True

                                                                                                                                    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
                                                                                                                                        print(canUnlockAll(boxes2))  # Output: True

                                                                                                                                            boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
                                                                                                                                                print(canUnlockAll(boxes3))  # Output: False
                                                                                                                                                #!/usr/bin/python3
                                                                                                                                                """
                                                                                                                                                This module provides a function to determine if all boxes can be opened.
                                                                                                                                                """

                                                                                                                                                def canUnlockAll(boxes):
                                                                                                                                                        """
                                                                                                                                                            Determine if all boxes can be opened.

                                                                                                                                                                Args:
                                                                                                                                                                        boxes (list of list): A list of lists representing the boxes and their keys.

                                                                                                                                                                            Returns:
                                                                                                                                                                                    bool: True if all boxes can be opened, False otherwise.
                                                                                                                                                                                        """

                                                                                                                                                                                            n = len(boxes)  # Total number of boxes
                                                                                                                                                                                                visited = set()  # Set to keep track of visited boxes

                                                                                                                                                                                                    def dfs(box):
                                                                                                                                                                                                                visited.add(box)
                                                                                                                                                                                                                        for key in boxes[box]:
                                                                                                                                                                                                                                        if key not in visited:
                                                                                                                                                                                                                                                            dfs(key)

                                                                                                                                                                                                                                                                dfs(0)  # Start DFS from the first box (boxes[0])

                                                                                                                                                                                                                                                                    return len(visited) == n

                                                                                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                                                                                        # Example usage:
                                                                                                                                                                                                                                                                            boxes1 = [[1], [2], [3], [4], []]
                                                                                                                                                                                                                                                                                print(canUnlockAll(boxes1))  # Output: True

                                                                                                                                                                                                                                                                                    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
                                                                                                                                                                                                                                                                                        print(canUnlockAll(boxes2))  # Output: True

                                                                                                                                                                                                                                                                                            boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
                                                                                                                                                                                                                                                                                                print(canUnlockAll(boxes3))  # Output: False

