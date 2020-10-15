def route_docs_encryption_4a(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import check_answer, get_text
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=19, score_manual=31)
    text = get_text(link)

    help_link = 'https://docs.google.com/presentation/d/1jWMz0VcZyDHcbrKYH_5iunoq7Dvh4cAfy5LHXLNGj7g/' \
                'edit#slide=id.g8e3ca8917c_0_0'
    tests.append(check_answer('1a', '8 char lowercase time?', text,
                              {'answers': r'5 \s* s', 'help_link': help_link}, points=10))
    tests.append(check_answer('2a', '8 char  any character time?', text,
                              {'answers': r'2 \s* d', 'help_link': help_link}, points=5))
    tests.append(check_answer('2b', 'What did you have to do?', text,
                              {'min_words': 7, 'help_link': help_link}, points=1))
    tests.append(check_answer('3a', 'Most significant factor?', text,
                              {'min_words': 3, 'help_link': help_link}, points=1))
    tests.append(check_answer('3b', 'Why?', text,
                              {'min_words': 8, 'help_link': help_link}, points=1))
    tests.append(check_answer('4a', 'Long enough password??', text,
                              {'min_words': 10, 'help_link': help_link}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
