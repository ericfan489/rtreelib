from rtreelib import RStarTree, Rect
from unittest import TestCase
from rtreelib.diagram import create_rtree_diagram


class Test(TestCase):

    def test_build(self):
        t = RStarTree(max_entries = 4,min_entries = 2)
        t.insert(30.0, Rect(10, 10, 11, 11))
        t.insert(5.0, Rect(2, 6, 3, 9))
        t.insert(20.0, Rect(1, 1, 2, 4))
        t.insert(8.0, Rect(8, 8, 10, 10))
        t.insert(9.0, Rect(7, 7, 9, 9))
        t.insert(10.0, Rect(8, 8, 9, 9))
        t.insert(11.0, Rect(0, 0, 1, 1))
        t.insert(12.0, Rect(6, 8, 7, 9))

        t.insert(40.0, Rect(9, 9, 11, 11))
        t.insert(50.0, Rect(2, 2, 5, 6))
        t.insert(22.0, Rect(0, 0, 3, 5))
        t.insert(7.0, Rect(4, 4, 11, 11))
        t.insert(23.0, Rect(3, 3, 4, 5))
        t.insert(19.0, Rect(0, 9, 9, 10))
        t.insert(28.0, Rect(9, 0, 10, 1))
        t.insert(13.0, Rect(6, 4, 7, 9))

        t.insert(12.0,Rect(1,1,1,1))
        create_rtree_diagram(t)
        nodes = t.get_nodes()
        print("Nodes")
        for x in nodes:
            print(type(x.lin_sum))
            print("lin_sum: "+ str(x.lin_sum))
            print("sq_sum: " + str(x.sq_sum))
            print("count: " + str(x.count))
            print("parent: " + str(x.parent))
            print(x.entries)
        print(t.get_levels())
        #print("Entries")
        entries = t.get_leaf_entries()
        for x in entries:
            #print(x.__repr__)
            print(x.rect)
            #print(x.child)
