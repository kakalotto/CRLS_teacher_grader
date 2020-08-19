def route_docs_hw02(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer, return_answer_run
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=9, score_manual=1)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g8b2165ea13_1_0'
    answer = return_answer_run('1a', text)
    tests.append(check_answer('1a', 'Write a program that prints a bunch of stuff"', answer,
                              {'answers': [r"<class \s 'str'>", r"<class \s 'int'>", r"<class \s 'float'>",  r'^5',
                                           r'^6\.9', r'name \s is', r'is \s the \s best'], 'help_link': site,
                               'min_matches': 6},
                              points=5))
    tests.append(check_answer('2a', 'Screenshot data-2-1', text, {'screenshot': True}, points=2))
    tests.append(check_answer('2b', 'Screenshot data-2-2', text, {'screenshot': True}, points=2))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]