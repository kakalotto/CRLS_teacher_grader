def route_docs_tcp_worksheet(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=1, score_manual=14)
    text = get_text(link)
    site = "https://drive.google.com/file/d/1ZDGwLIhzH4FDHb9juESkX8uDJp6FM6Eu/view"
    tests.append(check_answer('1a', 'Describe your protocol', text, {'min_words': 10, 'help_link': site}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]