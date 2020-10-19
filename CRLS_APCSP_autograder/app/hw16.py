def route_docs_hw16(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=6, score_manual=4)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g82408b16e1_2_0'

    tests.append(check_answer('1a', 'You have a list named exactly foods', text,
                              {'answers': r'foods \s*= .* \[ .*?  ] ',
                               'help_link': site, }, points=1))
    tests.append(check_answer('1a', 'You have a list named exactly foods with 5+ items', text,
                              {'answers': r'foods \s*= .* \[ .*? , .*? ,.*? , .*? , .*? ] ',
                               'help_link': site, }, points=1))
    tests.append(check_answer('1a', 'For loop used correctly', text, {'answers': r'for .*? in .*? foods .*? :'
                                                                                 r'', 'help_link': site, }, points=4))

    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]