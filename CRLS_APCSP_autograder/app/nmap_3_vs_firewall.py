def route_docs_nmap_3_vs_firewall(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    help_video = 'https://drive.google.com/file/d/1LNcw7yiO2Pa0creQ41fatw7iUUpdi8kg/view?usp=sharing'

    [user, tests, score_info] = initialize_scoring(username='IT2 Scholar', score_max=61, score_manual=9)
    text = get_text(link)
    tests.append(check_answer('1a', 'Screenshot firewall up and default is block', text,
                              {'screenshot': True, 'help_link': help_video}, points=10))
    tests.append(check_answer('1b', 'Screenshot logging on, drops recorded', text,
                              {'screenshot': True, 'help_link': help_video}, points=10))
    tests.append(check_answer('1c', 'Nmap scan of self', text,
                              {'answers': [r'starting \s nmap', r' host \s is \s up', r'nmap \s done', '135',
                                           '445'],
                               'min_matches': 5, 'help_link': help_video}, points=10))
    tests.append(check_answer('1d', 'Nmap scan machine 2', text,
                              {'answers': [r'starting \s nmap', r' host \s is \s up', r'nmap \s done', r'1000'],
                               'min_matches': 4, 'help_link': help_video}, points=10))
    tests.append(check_answer('1e', 'Logs machine 2', text,
                              {'answers': [r'drop', r'445', r'135', r'tcp'],
                               'min_matches': 4, 'help_link': help_video}, points=10))
    tests.append(check_answer('2a', 'Logs machine 2 scanned under decoy at least one is 172.25.233.1', text,
                              {'answers': [r'drop', r'445', r'135', r'tcp', r'172\.25\.233\.1'],
                               'min_matches': 5, 'help_link': help_video}, points=10))
    tests.append(check_answer('2b', 'What should I look for in logs while under attack?', text,
                              {'min_words': 8, 'help_link': help_video}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
