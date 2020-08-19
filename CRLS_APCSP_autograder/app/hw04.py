def route_docs_hw04(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer, return_answer_run
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=8, score_manual=2)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g8b2165ea13_2_27'
    tests.append(check_answer('1a', 'Set number variable (twice)', text,
                              {'answers': [r'number \s* =', r'number .*? ='], 'min_matches': 2, 'help_link': site},
                              points=1))
    answer = return_answer_run('1a', text)
    tests.append(check_answer('1a', 'Prints twice', answer, {'answers': r'.+ \n .+', 'help_link': site},
                              points=1))
    tests.append(check_answer('2a', 'Ask a question', text, {'answers': r'input .* \( .+? \)', 'help_link': site},
                              points=1))
    tests.append(check_answer('2a', 'Prints out response', text, {'answers': r'print \s* \(', 'help_link': site},
                              points=1))
    tests.append(check_answer('3a', 'Screenshot data-3-1', text, {'screenshot': True}, points=2))
    tests.append(check_answer('4a', 'Screenshot data-8-1', text, {'screenshot': True}, points=2))

    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
