def flatten(lists):
    '''
    :param lists: 传入的多维列表
    '''
    new_list = []
    for element in lists:
        if not isinstance(element, list):
            new_list.append(element)
        else:
            new_list.extend(flatten(element))

    return new_list
def test_answer():
    assert flatten([1,[2,3]])==[1,2,3]
