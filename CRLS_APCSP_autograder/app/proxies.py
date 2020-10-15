def route_docs_proxies(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=6, score_manual=94)
    text = get_text(link)
    help_1a = 'https://docs.google.com/presentation/d/1aFLrgG6TH2ttmO4U0HsE-537dc1NwztpBe2grzTiyJw/' \
              'edit#slide=id.g53697ff523_0_0'
    help_1b = 'https://docs.google.com/presentation/d/1aFLrgG6TH2ttmO4U0HsE-537dc1NwztpBe2grzTiyJw/' \
              'edit#slide=id.g1309dc45c6_0_25'
    help_2b = 'https://docs.google.com/presentation/d/1aFLrgG6TH2ttmO4U0HsE-537dc1NwztpBe2grzTiyJw/' \
              'edit#slide=id.g53697ff523_0_5'
    help_2c = 'https://docs.google.com/presentation/d/1aFLrgG6TH2ttmO4U0HsE-537dc1NwztpBe2grzTiyJw/' \
              'edit#slide=id.g273a29f038_4_0'
    tests.append(check_answer('1a', 'What is a proxy?', text, {'min_words': 10, 'help_link': help_1a}, points=1))
    tests.append(check_answer('1b', 'Convince head of company?', text, {'min_words': 10, 'help_link': help_1b},
                              points=1))
    tests.append(check_answer('2a', 'Screenshot proxy usage', text, {'screenshot': True, }, points=1))
    tests.append(check_answer('2b', 'How does it compare?', text, {'min_words': 10, 'help_link': help_2b}, points=1))
    tests.append(check_answer('2c', 'Advise classmates?', text, {'min_words': 10, 'help_link': help_2c}, points=1))
    tests.append(check_answer('3a', 'Research', text, {'min_words': 40, }, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]