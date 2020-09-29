def route_docs_scratch_12(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=38, score_manual=12)
    text = get_text(link)
    help_link = ''
    tests.append(check_answer('1c', 'Category for say X for Y seconds', text,
                              {'answers': r'look', 'help_link': help_link}, points=1))
    tests.append(check_answer('1d', 'Function for say X for Y seconds', text,
                              {'answers': ['say', 'seconds', 'time', 'text', 'bubble', 'speak'],
                               'help_link': help_link}, points=1))
    tests.append(check_answer('1e', 'Category for play sound X until done', text,
                              {'answers': r'sound', 'help_link': help_link}, points=1))
    tests.append(check_answer('1f', 'Function for play sound X until done', text,
                              {'answers': ['play', 'sound', 'meow', 'noise'], 'help_link': help_link}, points=1))
    tests.append(check_answer('1g', 'Category for switch costume to X', text,
                              {'answers': r'look', 'help_link': help_link}, points=1))
    tests.append(check_answer('1h', 'Function for switch costume to X', text,
                              {'answers': ['costume', 'switch', 'look', 'appear'], 'help_link': help_link}, points=1))
    tests.append(check_answer('1i', 'Category for glide N seconds to X Y', text,
                              {'answers': r'motion', 'help_link': help_link}, points=1))
    tests.append(check_answer('1j', 'Function for glide N seconds to X Y', text,
                              {'answers': ['move', 'glide', 'location', 'smooth', 'slow', 'position', 'slide'],
                               'help_link': help_link}, points=1))
    tests.append(check_answer('1k', 'Category for set size to X%', text,
                              {'answers': r'look', 'help_link': help_link}, points=1))
    tests.append(check_answer('1l', 'Function for set size to X%', text,
                              {'answers': ['size', 'change'], 'help_link': help_link}, points=1))
    tests.append(check_answer('1m', 'Category for repeat X', text,
                              {'answers': r'control', 'help_link': help_link}, points=1))
    tests.append(check_answer('1n', 'Function for repeat X', text,
                              {'answers': ['repeat', 'control'], 'help_link': help_link}, points=1))
    tests.append(check_answer('1o', 'Category for set X effect to Y', text,
                              {'answers': r'look', 'help_link': help_link}, points=1))
    tests.append(check_answer('1p', 'Function for repeat X', text,
                              {'answers': ['color', 'sprite', 'change', ], 'help_link': help_link}, points=1))
    tests.append(check_answer('1q', 'Category for go to X Y ', text,
                              {'answers': r'motion', 'help_link': help_link}, points=1))
    tests.append(check_answer('1r', 'Function for go to X Y', text,
                              {'answers': ['move', 'go', 'location', 'position', 'appear', 'teleport', 'jump'],
                               'help_link': help_link}, points=1))
    tests.append(check_answer('1s', 'Category for change pen size by X ', text,
                              {'answers': r'pen', 'help_link': help_link}, points=1))
    tests.append(check_answer('1t', 'Function for change pen size by X ', text,
                              {'answers': ['pen', 'change', 'size', ], 'help_link': help_link}, points=1))
    tests.append(check_answer('1u', 'Category for set pen color to X ', text,
                              {'answers': r'pen', 'help_link': help_link}, points=1))
    tests.append(check_answer('1v', 'Function for set pen color to X ', text,
                              {'answers': ['pen', 'change', 'color', 'set'], 'help_link': help_link}, points=1))
    tests.append(check_answer('1w', 'Category for point towards X ', text,
                              {'answers': r'motion', 'help_link': help_link}, points=1))
    tests.append(check_answer('1x', 'Function for point towards X', text,
                              {'answers': ['point', 'sprite', 'mouse'], 'help_link': help_link}, points=1))
    tests.append(check_answer('2a', 'What does motion category do', text,
                              {'answers': ['motion', 'move', 'moving', 'category', 'speed', 'way', 'blocks',
                                           'glide', 'turn', 'go', 'set', 'sprite', 'left', 'right', 'locate',],
                               'help_link': help_link}, points=4))
    tests.append(check_answer('2b', 'What does looks category do', text,
                              {'answers': ['look', 'appear', 'effect', 'talk', 'say', 'disappear', 'category',
                                           'blocks', 'costume', 'set', 'sprite', 'backdr'],
                               'help_link': help_link}, points=4))
    tests.append(check_answer('2c', 'What does sound category do', text,
                              {'answers': ['noise', 'sound', 'music', 'effect', 'cat', 'meow', 'category', 'blocks',
                                           'set', 'sprite'],
                               'help_link': help_link}, points=4))
    tests.append(check_answer('2d', 'What does pen category do', text,
                              {'answers': ['tools', 'pen', 'thickness', 'color', 'size', 'erase', 'clear', 'draw',
                                           'sprite', 'write'],
                               'help_link': help_link}, points=4))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]