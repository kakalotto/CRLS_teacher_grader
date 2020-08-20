def route_docs_hw08(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer, return_answer_run
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=9, score_manual=1)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g8b2165ea13_1_11'

    tests.append(check_answer('1a', 'Contains if and else', text, {'answers': ['if', r'else \s* :'],
                                                                   'help_link': site, 'min_matches': 2}, points=1))
    answer = return_answer_run('1a', text)
    tests.append(check_answer('1a', 'Prints "my name is" ', answer, {'answers': r'my \s name \s is',
                                                                     'help_link': site, }, points=1))
    tests.append(check_answer('2a', 'Screenshot select-4-1', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2b', 'Screenshot select-4-2', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2c', 'Screenshot select-4-3', text, {'screenshot': True}, points=1))
    tests.append(check_answer('3a', 'Contains if', text, {'answers': 'if', 'help_link': site, }, points=1))
    answer = return_answer_run('3a', text)
    tests.append(check_answer('3a', 'Prints "my name is" ', answer, {'answers': r'my \s name \s is',
                                                                     'help_link': site, }, points=1))
    tests.append(check_answer('4a', 'Screenshot select-5-1', text, {'screenshot': True}, points=1))
    tests.append(check_answer('4b', 'Screenshot select-5-2', text, {'screenshot': True}, points=1))

    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
