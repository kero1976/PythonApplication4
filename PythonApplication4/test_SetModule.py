import SetModule

def test_add_passing():
    lists = []
    lists.append({1,3,5})
    lists.append({2,5})
    lists.append({5,10})
    lines = SetModule.add(lists)
    assert lines == {1,2,3,5,10}

def test_intersection_passing():
    lists = []
    lists.append({1,3,5})
    lists.append({2,5})
    lists.append({5,10})
    lines = SetModule.intersection(lists)
    assert lines == {5}