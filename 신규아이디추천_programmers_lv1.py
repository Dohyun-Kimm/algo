def solution(new_id):
    # step1
    new_id = new_id.lower()
    # step2
    able = '-_.'
    temp = ''
    for c in new_id:
        if c.isalnum() or c in able:
            temp += c
    # step 3
    new_id = temp.replace('...', '.')
    # new_id = new_id.replace('..','.')
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # step 4
    if new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    # step 5
    if new_id == '':
        new_id = 'a'

    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # # step 7
    if len(new_id) < 3:
        new_id += new_id[-1] * (3 - len(new_id))
    return new_id