def route_docs_hw21(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=8, score_manual=2)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g82408b16e1_4_54'

    tests.append(check_answer('1a', 'dictionary ', text, {'answers': r'.*? = \s* { .*? }', 'help_link': site, },
                              points=1))
    tests.append(check_answer('1a', 'subtract one from value', text, {'answers': r'(\[ | \.get\() .+? -',
                                                                      'help_link': site, }, points=1))
    tests.append(check_answer('2a', 'Screenshot dict-2-1', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2b', 'Screenshot dict-3-1', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2c', 'Screenshot dict-3-2', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2d', 'Screenshot dict-3-3', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2e', 'Screenshot dict-3-4', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2f', 'Screenshot dict-3-5', text, {'screenshot': True}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]