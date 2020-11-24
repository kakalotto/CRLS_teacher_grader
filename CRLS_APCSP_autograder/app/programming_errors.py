def route_docs_programming_errors(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=10, score_manual=40)
    text = get_text(link)
    tests.append(check_answer('1a', 'Code w/syntax error', text, {'min_words': 1}, points=1))
    tests.append(check_answer('2a', 'Code w/logic error', text, {'min_words': 1}, points=1))
    tests.append(check_answer('3a', 'Code w/runtime error', text, {'min_words': 1}, points=1))
    tests.append(check_answer('4a', 'AP CSP overflow error question', text, {'min_words': 5}, points=1))
    tests.append(check_answer('5a', 'Prints True/False?', text, {'answers': 'f'}, points=5))
    tests.append(check_answer('5b', 'Why?', text, {'min_words': 2}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
