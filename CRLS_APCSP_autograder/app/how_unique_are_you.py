def route_docs_how_unique_are_you(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=2, score_manual=8)
    text = get_text(link)
    tests.append(check_answer('1a', 'How unique are you?', text, {'min_words': 2, }, points=1))
    tests.append(check_answer('1b', 'How does that make you feel', text, {'min_words': 7, }, points=1))
    score_info = sum_score(tests, score_info)
    print("tests " + str(tests))
    return [user, tests, score_info]