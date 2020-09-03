def route_docs_hw10(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=10, score_manual=0)
    text = get_text(link)
    site = 'https://docs.google.com/presentation/d/1VHirrn2Gdjjb-GIdQ8min6OzkhzNwNuX8pmye-5AmG8/' \
           'edit#slide=id.g8b2165ea13_3_32'

    tests.append(check_answer('1a', 'You have a list named exactly nice_list with exactly 5 items', text,
                              {'answers': r'nice_list \s*= .* \[ .*? , .*? ,.*? , .*? , .*? ] ',
                               'help_link': site, }, points=1))
    tests.append(check_answer('1a', 'Print second item in list, positive index', text,
                              {'answers': r'nice_list[\s* 1 \s*] ', 'help_link': site, }, points=1))
    tests.append(check_answer('1a', 'Print second item in list, positive index', text,
                              {'answers': r'nice_list[\s* -4 \s*] ', 'help_link': site, }, points=1))
    tests.append(check_answer('2a', 'Screenshot lists-7-1', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2b', 'Screenshot lists-7-2', text, {'screenshot': True}, points=1))
    tests.append(check_answer('2c', 'Screenshot lists-7-3', text, {'screenshot': True}, points=1))
    tests.append(check_answer('3a', 'You have a list named exactly naught_list with exactly 6 items', text,
                              {'answers': r'naughty_list \s *= .* \[ .*? , .*? ,.*? , .*? , .*? , .*?] ',
                               'help_link': site, }, points=1))
    tests.append(check_answer('3a', 'Print first two items in list, slices', text,
                              {'answers': r'naughty_list[ .*? : 2 \s*] ', 'help_link': site, }, points=1))
    tests.append(check_answer('3a', 'Print last four items in list, slices', text,
                              {'answers': r'naughty_list[ \s*3 : .*? ] ', 'help_link': site, }, points=1))
    tests.append(check_answer('4a', 'Screenshot lists-7-1', text, {'screenshot': True}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]