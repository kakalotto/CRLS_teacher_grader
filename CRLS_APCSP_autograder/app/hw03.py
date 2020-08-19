def route_docs_hw03(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=8, score_manual=2)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g8b2165ea13_2_38'

    tests.append(check_answer('1a', 'Write a program that prints a bunch of stuff"', text,
                              {'answers': [r"c \s* =", r"f \s* = .*? c", r'print \s* \( \s* f'],
                               'help_link': site, 'min_matches': 3},
                              points=5))
    tests.append(check_answer('2a', 'Screenshot data-7-1', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2b', 'Screenshot data-7-2', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2c', 'Screenshot data-7-3', text, {'screenshot': True}, points=1))

    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
