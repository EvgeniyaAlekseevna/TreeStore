import unittest

from tree_store import TreeStore

items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

if __name__ == '__main__':
    ts = TreeStore(items)

    print(ts.getAll())
    print(ts.getItem(7))
    print(ts.getChildren(4))
    print(ts.getChildren(5))
    print(ts.getAllParents(7))

    # Запуск тестов
    unittest.main(module='tests.test_tree_store', exit=False)
