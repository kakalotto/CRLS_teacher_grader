def route_docs_hw06(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer, return_answer_run
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=8, score_manual=2)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g8b2165ea13_2_0'

    tests.append(check_answer('1a', 'No letter "T"', text, {'answers': ['.+ [^T]', '[a-zA-Z]'],
                                                            'help_link': site, 'min_matches': 2},
                              points=2))
    answer = return_answer_run('1a', text)
    tests.append(check_answer('1a', 'print "True" in Boolean sense', answer, {'answers': 'true', 'help_link': site, },
                              points=2))
    tests.append(check_answer('2a', 'No letter "F"', text, {'answers': ['.+ [^F]', '[a-zA-Z]'],
                                                            'help_link': site, 'min_matches': 2},
                              points=2))
    answer = return_answer_run('2a', text)
    tests.append(check_answer('2a', 'print "False" in Boolean sense', answer, {'answers': 'false', 'help_link': site, },
                              points=2))
    tests.append(check_answer('3a', 'Screenshot select-1-1', text, {'screenshot': True}, points=2))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
