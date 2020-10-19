def route_docs_tor_1(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=8, score_manual=92)
    text = get_text(link)
    help_vid = 'https://drive.google.com/file/d/1vA_CNZH-bvcWHbJXUV9Wl_pMPgsSNjyv/view'
    tests.append(check_answer('1a', 'Screenshot Tor running', text,
                              {'screenshot': True, 'help_link': help_vid}, points=1))
    tests.append(check_answer('1b', 'Screenshot Tor circuit', text,
                              {'screenshot': True, 'help_link': help_vid}, points=1))
    tests.append(check_answer('1c', 'Test network settings', text,
                              {'screenshot': True, 'help_link': help_vid}, points=1))
    tests.append(check_answer('2a', 'Usability', text, {'min_words': 25, }, points=1))
    tests.append(check_answer('3a', 'Screenshot Tor bridges', text,
                              {'screenshot': True, 'help_link':help_vid}, points=1))
    tests.append(check_answer('4a', 'Describe how Tor works', text, {'min_words': 20, }, points=1))
    tests.append(check_answer('4b', 'Describe Tor encryption', text, {'min_words': 20, }, points=1))
    tests.append(check_answer('4c', ' Why use Tor?', text, {'min_words': 20, }, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
