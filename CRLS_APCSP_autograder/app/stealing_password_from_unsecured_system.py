def route_docs_stealing_passwords_from_unsecured_systems(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='IT2 Scholar', score_max=80, score_manual=0)
    text = get_text(link)

    help_howto = 'https://docs.google.com/document/d/1P9AGkbtb9dmQSzpi_KZuK8Jv9GmvTD9TIpu58-r0OoM/' \
                 'edit#bookmark=id.ldgnfnn3hh5y'
    help_screensaver = 'https://www.thewindowsclub.com/lock-computer-inactivity-windows-10'
    help_chrome = 'https://applygist.com/2017/12/' \
                  'how-to-disable-saved-password-settings-in-chrome-firefox-opera-other-browsers.html'
    tests.append(check_answer('1a', 'Copy+paste inspect elements', text,
                              {'answers': r'type\=\"password\"', 'help_link': help_howto, }, points=20))
    tests.append(check_answer('1b', 'Screenshot password', text,
                              {'screenshot': True, 'help_link': help_howto}, points=20))
    tests.append(check_answer('2a', 'Settings to lock?', text,
                              {'answers': [r'screen \s* saver', r'machine \s* inactivity'],
                               'help_link': help_screensaver, 'min_matches': 1},
                              points=10))
    tests.append(check_answer('2b', 'Screenshot settings', text,
                              {'screenshot': True, 'help_link': help_howto}, points=10))
    tests.append(check_answer('3a', 'Chrome settings do not save pword', text,
                              {'answers': r'offer \s* to \s* save \s* password', 'help_link': help_chrome}, points=10))
    tests.append(check_answer('3b', 'Screenshot settings', text,
                              {'screenshot': True, 'help_link': help_chrome}, points=10))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]