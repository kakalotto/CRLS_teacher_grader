def route_docs_hw05(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=7, score_manual=3)
    text = get_text(link)
    tests.append(check_answer('1a', 'Screenshot data-3-1', text, {'screenshot': True}, points=7))

    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
