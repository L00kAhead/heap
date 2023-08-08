import unittest
from heap import Heap, HeapType


class TestHeapMethods(unittest.TestCase):
    def test_insert_min_heap(self):
        min_heap = Heap([12, 15, 30, 40, 75, 80, 200], heap_type=HeapType.MIN_HEAP)
        min_heap.insert(3)
        self.assertEqual(min_heap.get_heap, [3, 12, 30, 15, 75, 80, 200, 40])

    def test_insert_max_heap(self):
        max_heap = Heap([200, 100, 70, 80, 90, 10, 45], heap_type=HeapType.MAX_HEAP)
        max_heap.insert(110)
        self.assertEqual(max_heap.get_heap, [200, 110, 70, 100, 90, 10, 45, 80])

    def test_extract_min_heap(self):
        min_heap = Heap([3, 12, 30, 15, 75, 80, 200, 40], heap_type=HeapType.MIN_HEAP)
        extracted_value = min_heap.extract()
        self.assertEqual(extracted_value, 3)
        self.assertEqual(min_heap.get_heap, [12, 15, 30, 40, 75, 80, 200])

    def test_extract_max_heap(self):
        max_heap = Heap(
            [200, 110, 70, 100, 90, 10, 45, 80], heap_type=HeapType.MAX_HEAP
        )
        extracted_value = max_heap.extract()
        self.assertEqual(extracted_value, 200)
        self.assertEqual(max_heap.get_heap, [110, 100, 70, 80, 90, 10, 45])

    def test_heapify_min_heap(self):
        impure_min_heap = Heap(
            [40, 20, 30, 35, 75, 80, 200], heap_type=HeapType.MIN_HEAP
        )
        impure_min_heap.heapify(0)
        self.assertEqual(impure_min_heap.get_heap, [20, 35, 30, 40, 75, 80, 200])

    def test_heapify_max_heap(self):
        impure_max_heap = Heap(
            [10, 100, 200, 80, 90, 70, 45], heap_type=HeapType.MAX_HEAP
        )
        impure_max_heap.heapify(0)
        self.assertEqual(impure_max_heap.get_heap, [200, 100, 70, 80, 90, 10, 45])

    def test_delete_max_heap(self):
        max_heap = Heap([200, 100, 70, 80, 90, 10, 45], HeapType.MAX_HEAP)
        max_heap.delete(3)
        self.assertEqual(max_heap.get_heap, [200, 100, 70, 45, 90, 10])

    def test_delete_min_heap(self):
        min_heap = Heap([12, 15, 30, 40, 75, 80, 200], HeapType.MIN_HEAP)
        min_heap.delete(2)
        self.assertEqual(min_heap.get_heap, [12, 15, 80, 40, 75, 200])

    def test_build_min_heap(self):
        min_heap = Heap([32, 5, 65, 23, 45, 678, 12], HeapType.MIN_HEAP)
        min_heap.build_heap()
        self.assertEqual(min_heap.get_heap, [5, 23, 12, 32, 45, 678, 65])

    def test_build_max_heap(self):
        min_heap = Heap([70, 43, 5, 9, 17, 23, 34, 678, 98, 7, 32], HeapType.MAX_HEAP)
        min_heap.build_heap()
        self.assertEqual(min_heap.get_heap, [678, 98, 34, 70, 32, 23, 5, 9, 43, 7, 17])

    def test_heap_sort_ascending(self):
        heap = Heap([4, 10, 3, 5, 1, 8, 2], HeapType.MAX_HEAP)
        heap.heap_sort()
        self.assertEqual(heap.get_heap, [1, 2, 3, 4, 5, 8, 10])

    def test_heap_sort_descending(self):
        heap = Heap([4, 10, 3, 5, 1, 8, 2], HeapType.MIN_HEAP)
        heap.heap_sort()
        self.assertEqual(heap.get_heap, [10, 8, 5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
