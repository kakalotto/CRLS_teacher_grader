def route_docs_python_2040(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=8, score_manual=0)
    text = get_text(link)
    tests.append(check_answer('1a', '', text, {'answers': r'(pretty \s good \s grade)'}, points=2))
    tests.append(check_answer('2a', '', text, {'answers': r'[0-9a-zA-Z]+'}, points=3))
    tests.append(check_answer('3a', '', text, {'answers': r'[0-9a-zA-Z]+'}, points=3))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]