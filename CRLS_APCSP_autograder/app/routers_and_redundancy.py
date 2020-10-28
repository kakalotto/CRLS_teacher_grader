def route_docs_routers_and_redundancy(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=11, score_manual=39)
    text = get_text(link)
    help_link = 'https://drive.google.com/drive/folders/1KzIBD-ivxqHGd1HDlK5x51wrf3QqoDQ0'
    tests.append(check_answer('1a', 'All messages get through?', text, {'min_words': 1, 'help_link': help_link},
                              points=1))
    tests.append(check_answer('2a', 'Why might message be dropped?', text,
                              {'min_words': 10, 'help_link': help_link}, points=1))
    tests.append(check_answer('3a', 'Trace full conversation??', text, {'min_words': 1, }, points=1))
    tests.append(check_answer('4a', 'What types of things ppl talking about?', text,
                              {'min_words': 10, 'help_link': help_link}, points=1))
    tests.append(check_answer('5a', 'Trace conversation on different router?', text,
                              {'min_words': 1, 'help_link': help_link}, points=1))
    tests.append(check_answer('6a', 'What talking about?', text, {'min_words': 7, 'help_link': help_link}, points=1))
    tests.append(check_answer('7a', 'Always same path??', text, {'min_words': 1, 'help_link': help_link}, points=1))
    tests.append(check_answer('8a', 'What simulating?', text, {'min_words': 5, 'help_link': help_link}, points=1))
    tests.append(check_answer('9a', 'Know path in advance?', text, {'min_words': 5, 'help_link': help_link}, points=1))
    tests.append(check_answer('10a', 'What can ISP do?', text, {'min_words': 5, 'help_link': help_link}, points=1))
    tests.append(check_answer('10b', 'Comfortable with this?', text,
                              {'min_words': 10, 'help_link': help_link}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
