def route_docs_cybersecurity(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=14, score_manual=86)
    text = get_text(link)
    tests.append(check_answer('1a', 'keylogger', text, {'min_words': 15}, points=1))
    tests.append(check_answer('2a', 'phishing', text, {'min_words': 15},  points=1))
    tests.append(check_answer('3a', 'malware', text, {'min_words': 15}, points=1))
    tests.append(check_answer('4a', 'rogue access point', text, {'min_words': 15}, points=1))
    tests.append(check_answer('5a', '2FA screenshot', text, {'screenshot': True, }, points=10))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]