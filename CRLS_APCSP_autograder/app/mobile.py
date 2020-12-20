def route_docs_mobile(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import check_answer, get_text
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=36, score_manual=24)
    text = get_text(link)
    tests.append(check_answer('1a', 'Android vs. iPhone', text, {'min_words': 15}, points=1))
    tests.append(check_answer('2a', 'Connect to wireless', text, {'screenshot': True}, points=5))
    tests.append(check_answer('2b', 'Connect to bluetooth', text, {'screenshot': True}, points=5))
    tests.append(check_answer('2c', 'Connect to cellular', text, {'screenshot': True}, points=5))
    tests.append(check_answer('2d', 'Connect to email', text, {'screenshot': True}, points=5))
    tests.append(check_answer('3a', 'Screen lock screenshot', text, {'screenshot': True}, points=5))
    tests.append(check_answer('3b', 'Multiple failed login?', text, {'min_words': 3}, points=1))
    tests.append(check_answer('3c', 'Remote wipe app?', text, {'min_words': 5}, points=1))
    tests.append(check_answer('3d', 'Locator app?', text, {'min_words': 1}, points=1))
    tests.append(check_answer('3e', 'Screenshot update OS?', text, {'screenshot': True}, points=5))
    tests.append(check_answer('4a', 'Reduce power use?', text, {'min_words': 5}, points=1))
    tests.append(check_answer('5a', 'identifyone app that is synced', text, {'min_words': 1}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
