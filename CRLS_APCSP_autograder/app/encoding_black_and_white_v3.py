def route_docs_encoding_black_and_white(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=28, score_manual=12)
    text = get_text(link)
    help_a = 'https://docs.google.com/presentation/d/1dqMZxtjQEokaLjBUSIwKkuO4lDIoPM33ae8wm8WGs98/' \
             'edit#slide=id.g8c1b8af0ca_0_6'
    help_two = 'https://docs.google.com/presentation/d/1dqMZxtjQEokaLjBUSIwKkuO4lDIoPM33ae8wm8WGs98/' \
               'edit#slide=id.g8c1b8af0ca_0_26'
    help_pros_cons = 'https://docs.google.com/presentation/d/1dqMZxtjQEokaLjBUSIwKkuO4lDIoPM33ae8wm8WGs98/' \
                     'edit#slide=id.g8c1b8af0ca_0_11'
    tests.append(check_answer('1a', 'Bits for A?', text,
                              {'answers': r'1\s*0\s*1 \s*'
                                          r'0\s*1\s*0 \s*'
                                          r'0\s*0\s*0\s*'
                                          r'0\s*1\s*0 \s*'
                                          r'0\s*1\s*0 .*?',
                               'help_link': help_a}, points=10))
    tests.append(check_answer('2a', 'Total bits needed?', text, {'answers': r'48', 'help_link': help_two}, points=4))
    tests.append(check_answer('2b', 'How long?', text, {'min_words': 2, 'help_link': help_two}, points=1))
    tests.append(check_answer('2c', ' How much does the digital image resemble this ', text,
                              {'min_words': 10, 'help_link': help_two}, points=1))
    tests.append(check_answer('2d', 'Total bits needed?', text, {'answers': r'192', 'help_link': help_two}, points=4))
    tests.append(check_answer('2e', 'How long?', text, {'min_words': 2, 'help_link': help_two}, points=1))
    tests.append(check_answer('2f', 'What are the pros and cons of sampling an image more frequently', text,
                              {'min_words': 10, 'help_link': help_pros_cons}, points=1))
    tests.append(check_answer('3a', 'Screenshot picture', text, {'screenshot': True}, points=1))
    tests.append(check_answer('3b', 'Screenshot bits', text, {'answers': r'[0-9]+'}, points=5))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]