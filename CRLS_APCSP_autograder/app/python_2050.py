def route_docs_python_2051(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=8, score_manual=0)
    text = get_text(link)
    tests.append(check_answer('1a', 'Expected result', text, {'answers':  r'[0-9a-zA-Z]+'}, points=1))
    tests.append(check_answer('1b', 'Actual result', text, {'answers':  r'a \s* d \s* .+?'}, points=1))
    tests.append(check_answer('2a', 'Expected result', text, {'answers':  r'[0-9a-zA-Z]+'}, points=1))
    tests.append(check_answer('2b', 'Actual result', text, {'answers':  r'c .+?'}, points=1))
    tests.append(check_answer('3a', 'Expected result', text, {'answers':  r'[0-9a-zA-Z]+'}, points=1))
    tests.append(check_answer('3b', 'Actual result', text, {'answers':  r'e .+?'}, points=1))
    tests.append(check_answer('4a', 'Expected result', text, {'answers':  r'[0-9a-zA-Z]+'}, points=1))
    tests.append(check_answer('4b', 'Actual result', text,
                              {'answers':  r' a .+? b.+? c .+? haha .+? e .+?'}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
