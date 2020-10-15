def route_docs_encryption_1a(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import check_answer, get_text
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=17, score_manual=33)
    text = get_text(link)

    combos_link = 'https://docs.google.com/presentation/d/1Ct3HyZeyCfhrGqjzpLthGdChQMWk4SETLDeRdb_cvI0/' \
                  'edit#slide=id.g8f1a9b6388_0_0'
    tests.append(check_answer('1a', 'How many combos for random substitution?', text,
                              {'answers': [r'26!', r'26 \s* fac', r'26 \s* x \s* 25 \s* x \s* 24', r'4\.03 .*? 26'],
                               'help_link': combos_link}, points=5))
    tests.append(check_answer('1b', 'Explain 1a', text,
                              {'min_words': 1, 'help_link': combos_link}, points=1))
    tests.append(check_answer('2a', 'How much easier to crack Caesar QUALITATIVELY', text,
                              {'min_words': 7, 'help_link': combos_link}, points=1))
    tests.append(check_answer('2b', 'How much easier to crack Caesar QUANTITATIVELY', text,
                              {'answers': r'1 \. 6 .*? 25', 'help_link': combos_link}, points=5))
    tests.append(check_answer('2c', 'Show work for 2b', text,
                              {'min_words': 2, 'help_link': combos_link}, points=1))
    random_link = 'https://docs.google.com/presentation/d/1Ct3HyZeyCfhrGqjzpLthGdChQMWk4SETLDeRdb_cvI0/' \
                  'edit#slide=id.g8f1a9b6388_0_5'
    tests.append(check_answer('3a', 'Hard to crack random?', text,
                              {'min_words': 10, 'help_link': random_link}, points=1))
    tests.append(check_answer('3b', 'Shorter or longer to crack Random and WHY?', text,
                              {'min_words': 10, 'help_link': combos_link}, points=1))
    tests.append(check_answer('4a', 'Algorithm to crack Caesar?', text,
                              {'min_words': 8, 'help_link': random_link}, points=1))
    tests.append(check_answer('4b', 'Algorithm to crack random?', text,
                              {'min_words': 8, 'help_link': random_link}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]