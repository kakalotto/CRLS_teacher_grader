def route_docs_hw09(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer, return_answer_run
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=8, score_manual=2)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g8b2165ea13_1_23'

    tests.append(check_answer('1a', 'You have a list of at least 4 items', text,
                              {'answers': r'= .* \[ .*? , .*? ,.*? , .*? ] ', 'help_link': site, }, points=1))
    answer = return_answer_run('1a', text)
    tests.append(check_answer('1a', 'Prints list" ', answer, {'answers': r' \[ .*? \]', 'help_link': site, }, points=1))
    tests.append(check_answer('2a', 'Screenshot list-2-1', text, {'screenshot': True}, points=1))
    tests.append(check_answer('3a', 'You have a list of at least 4 items and calculate length', text,
                              {'answers': [r'= .* \[ .*? , .*? ,.*? , .*? ] ', 'len'], 'min_matches': 2,
                               'help_link': site, }, points=1))
    answer = return_answer_run('3a', text)
    tests.append(check_answer('3a', 'Prints list" ', answer, {'answers': r' \[ .*? \]', 'help_link': site, }, points=1))
    tests.append(check_answer('4a', 'Screenshot list-3-1', text, {'screenshot': True}, points=1))
    tests.append(check_answer('4a', 'Screenshot list-3-2', text, {'screenshot': True}, points=1))
    tests.append(check_answer('4a', 'Screenshot list-3-3', text, {'screenshot': True}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]