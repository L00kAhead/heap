from enum import Enum


class HeapType(Enum):
    MIN_HEAP = "min_heap"
    MAX_HEAP = "max_heap"


class Heap:
    def __init__(self, arr: list[int | float], heap_type: HeapType) -> None:
        self.__arr = arr
        self.__heap_type = heap_type

    @property
    def get_heap(self):
        return self.__arr

    def insert(self, value: int | float, idx=None) -> list[int | float]:
        """
        Insert a value into the binary heap at the specified index or at the end of the heap.

        Args:
            value (int or float): The value to be inserted into the heap.
            idx (int, optional): The index at which the value should be inserted. If None or out of bounds,
                                the value will be appended to the end of the heap.

        Returns:
            list[int | float]: The updated heap after inserting the value.
        """
        if idx != None and 0 <= idx < len(self.__arr):
            self.__arr[idx] = value
            curr_idx = idx
        else:
            self.__arr.append(value)
            curr_idx = len(self.__arr) - 1

        for _ in range(len(self.__arr)):
            parent_idx = abs((curr_idx - 1) // 2)

            if self.__heap_type == HeapType.MIN_HEAP:
                if self.__arr[parent_idx] < self.__arr[curr_idx]:
                    break
                elif curr_idx == 0:
                    break
                else:
                    self.__arr[parent_idx], self.__arr[curr_idx] = (
                        self.__arr[curr_idx],
                        self.__arr[parent_idx],
                    )
                    curr_idx = parent_idx
            else:
                if self.__arr[parent_idx] > self.__arr[curr_idx]:
                    break
                elif curr_idx == 0:
                    break
                else:
                    self.__arr[parent_idx], self.__arr[curr_idx] = (
                        self.__arr[curr_idx],
                        self.__arr[parent_idx],
                    )
                    curr_idx = parent_idx
        return self.__arr

    def heapify(self, idx: int) -> None:
        """
        Rearrange the heap rooted at the given index to maintain the heap property.

        Args:
            idx (int): The index of the element to start heapifying from.
        """
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        curr_idx = idx

        if self.__heap_type == HeapType.MIN_HEAP:
            # Min Heap
            if (
                left_child < len(self.__arr)
                and self.__arr[left_child] < self.__arr[curr_idx]
            ):
                curr_idx = left_child

            # Compare with right child
            if (
                right_child < len(self.__arr)
                and self.__arr[right_child] < self.__arr[curr_idx]
            ):
                curr_idx = right_child
        else:
            # Max Heap
            if (
                left_child < len(self.__arr)
                and self.__arr[left_child] > self.__arr[curr_idx]
            ):
                curr_idx = left_child

            # Compare with right child
            if (
                right_child < len(self.__arr)
                and self.__arr[right_child] > self.__arr[curr_idx]
            ):
                curr_idx = right_child

        # Swap if needed and continue heapifying
        if curr_idx != idx:
            self.__arr[idx], self.__arr[curr_idx] = (
                self.__arr[curr_idx],
                self.__arr[idx],
            )
            self.heapify(curr_idx)  # Recursive call to heapify the swapped subtree

    def extract(self) -> int | float:
        """
        Extracts the extreme value (min or max) from the heap and balances the heap structure.

        Args:
            min (bool, optional): If True, extracts the minimum value (for a min-heap).
                                If False, extracts the maximum value (for a max-heap).
                                Defaults to True.

        Returns:
            int | float: The extracted extreme value from the heap.
        """
        # Swap the first and last index
        self.__arr[-1], self.__arr[0] = self.__arr[0], self.__arr[-1]
        extracted_val = self.__arr.pop()
        self.heapify(0)
        return extracted_val

    def delete(self, idx: int) -> None:
        """
        Delete the element at the specified index from the heap.

        Args:
            idx (int): The index of the element to be deleted.

        Raises:
            IndexError: If the index is out of range.

        Note:
            For a min-heap, the element at the specified index is replaced with negative infinity
            before performing an extract operation to maintain the heap property.
            For a max-heap, the element at the specified index is replaced with positive infinity
            before performing an extract operation to maintain the heap property.
        """
        if 0 <= idx < len(self.__arr):
            if self.__heap_type == HeapType.MIN_HEAP:
                self.insert(float("-inf"), idx)
            else:
                self.insert(float("inf"), idx)
            self.extract()
        else:
            raise IndexError("Index out of range")

    def build_heap(self):
        """
        Build the heap from the given array by applying heapify operations.

        Note:
            This method rearranges the elements in the heap to satisfy the heap property,
            starting from the bottom-most right-most node and working upwards.
        """
        start_idx = abs((len(self.__arr) - 2) // 2)
        for idx in range(start_idx, -1, -1):
            self.heapify(idx)
