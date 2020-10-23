def route_docs_hw19a(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=6, score_manual=4)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g8b4a3f7eec_2_11'

    tests.append(check_answer('1a', 'sequencing (>3 lines)', text, {'answers': r' .+? \n .+? \n .+? ',
                                                                    'help_link': site, }, points=2))
    tests.append(check_answer('1b', 'Selection', text, {'answers': r'if', 'help_link': site, }, points=2))
    tests.append(check_answer('1c', 'Iteration', text, {'answers': r'(for|while)', 'help_link': site, }, points=2))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]