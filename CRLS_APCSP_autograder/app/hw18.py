def route_docs_hw18(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=5, score_manual=5)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g82408b16e1_4_0'

    tests.append(check_answer('1a', 'nested if', text, {'answers': r'if .+? : .*? \n .*? if.', 'help_link': site, },
                              points=2))
    tests.append(check_answer('1a', 'print', text, {'answers': r'print .*? \(  ', 'help_link': site, }, points=1))
    tests.append(check_answer('2a', 'Screenshot select-6-1', text, {'screenshot': True}, points=2))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]