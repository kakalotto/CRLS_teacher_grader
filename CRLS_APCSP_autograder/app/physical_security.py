def route_docs_physical_security(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=2, score_manual=38)
    text = get_text(link)
    google_link = 'https://www.youtube.com/watch?v=kd33UVZhnAA'
    tests.append(check_answer('1a', 'Describe Google physical security', text,
                              {'min_words': 20, 'help_link': google_link}, points=1))
    tests.append(check_answer('2a', 'Describe break-in to CRLS', text, {'min_words': 20, }, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]