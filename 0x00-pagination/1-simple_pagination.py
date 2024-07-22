#!/usr/bin/env python3

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset."""
        # Validate input arguments
        assert isinstance(
            page, int) and page > 0
        assert isinstance(
            page_size, int) and page_size > 0

        # Get the dataset
        dataset = self.dataset()

        # Get the start and end indices for pagination
        start_index, end_index = index_range(page, page_size)

        # Check if the indices are out of range
        if start_index >= len(dataset):
            # Return empty list if start index is beyond dataset length
            return []

        # Return the appropriate page of the dataset
        return dataset[start_index:end_index]


# Example usage
if __name__ == "__main__":
    server = Server()
    page = 1
    page_size = 10
    print(server.get_page(page, page_size))
