def route_docs_encoding_text(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=10, score_manual=20)
    text = get_text(link)
    lower_help = 'https://docs.google.com/presentation/d/1ETVPLAtChnLJr-mLBF90U8_0RxmDQ-QwmTbLhwB34SE/' \
                 'edit#slide=id.g824b0d1d88_0_0'
    upper_number_help = 'https://docs.google.com/presentation/d/1ETVPLAtChnLJr-mLBF90U8_0RxmDQ-QwmTbLhwB34SE/' \
                        'edit#slide=id.g824b0d1d88_0_8'
    combo_help = 'https://docs.google.com/presentation/d/1ETVPLAtChnLJr-mLBF90U8_0RxmDQ-QwmTbLhwB34SE/' \
                 'edit#slide=id.g824b0d1d88_0_15'
    bytes_help = 'https://docs.google.com/presentation/d/1ETVPLAtChnLJr-mLBF90U8_0RxmDQ-QwmTbLhwB34SE/' \
                 'edit#slide=id.g824b0d1d88_0_28'
    tests.append(check_answer('1a', 'How to transmit lowercase letters (checkoff)', text,
                              {'min_words': 10, 'help_link': lower_help}, points=1))
    tests.append(check_answer('1b', 'How to transmit lowercase+uppercase+numbers (checkoff)', text,
                              {'min_words': 10, 'help_link': upper_number_help}, points=1))
    tests.append(check_answer('2a', 'lowercase bits/character required?', text,
                              {'answers': r'(5|five)', 'help_link': combo_help, }, points=1))
    tests.append(check_answer('2b', 'Explain 2a (checkoff)', text, {'min_words': 1, 'help_link': combo_help}, points=1))
    tests.append(check_answer('2c', 'Rotokas bits/character required?', text,
                              {'answers': r'(4|four)', 'help_link': combo_help, }, points=1))
    tests.append(check_answer('2d', 'Explain 2c (checkoff)', text, {'min_words': 1, 'help_link': combo_help}, points=1))
    tests.append(check_answer('3a', '512 GigaBytes to Gigabits (in GB)', text,
                              {'answers': r'4096', 'help_link': bytes_help, }, points=1))
    tests.append(check_answer('3b', 'Explain 3a (checkoff)', text, {'min_words': 1, 'help_link': bytes_help}, points=1))
    tests.append(check_answer('3c', '0.05 GigaBytes to Gigabit?', text,
                              {'answers': r'\.00625', 'help_link': bytes_help, }, points=1))
    tests.append(check_answer('3d', 'Explain 3c (checkoff)', text, {'min_words': 1, 'help_link': bytes_help}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
