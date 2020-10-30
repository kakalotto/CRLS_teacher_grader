def route_docs_hw20(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=8, score_manual=2)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g82408b16e1_4_13'

    tests.append(check_answer('1a', 'dictionary eng2martian', text, {'answers': r'eng2martian \s* = \s* { .*? }',
                                                                     'help_link': site, }, points=2))
    tests.append(check_answer('1a', 'print', text, {'answers': r'print .*? \( (eng2martian\[ | eng2martian\.get\( )',
                                                    'help_link': site, }, points=2))
    tests.append(check_answer('2a', 'Screenshot dict-1-1', text, {'screenshot': True}, points=2))
    tests.append(check_answer('2b', 'Screenshot dict-1-2', text, {'screenshot': True}, points=2))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
