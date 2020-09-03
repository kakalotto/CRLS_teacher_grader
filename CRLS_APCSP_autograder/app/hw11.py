def route_docs_hw11(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=6, score_manual=4)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g8b4a3f7eec_2_0'

    tests.append(check_answer('1a', 'You have a list named exactly top5 with at least 5 items', text,
                              {'answers': r'top5 \s*= .* \[ .*? , .*? ,.*? , .*? , .*? ] ',
                               'help_link': site, }, points=1))
    tests.append(check_answer('1a', 'Asks question', text, {'answers': r'= .*? input ', 'help_link': site, }, points=1))
    tests.append(check_answer('1a', 'Uses "in" to check if something in list', text,
                              {'answers': r'if .*? in .*? top5 ', 'help_link': site, }, points=1))
    tests.append(check_answer('1a', 'Code does something if it is not in top5 (else)', text,
                              {'answers': r'else', 'help_link': site, }, points=1))
    tests.append(check_answer('2a', 'Screenshot lists-5-1', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2b', 'Screenshot lists-5-2', text, {'screenshot': True}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
