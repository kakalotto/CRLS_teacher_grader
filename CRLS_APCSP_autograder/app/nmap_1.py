def route_docs_nmap_remote_1(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='IT2 Scholar', score_max=50, score_manual=4)
    text = get_text(link)
    help_1 = 'https://www.pearsonitcertification.com/articles/article.aspx?p=1868080'
    help_explain = 'https://drive.google.com/file/d/1JeX33pCif5X3N8YY_RI3qgXZ3DS33XM7/view?t=2m35s'

    tests.append(check_answer('1a', 'SSH protocol', text, {'answers': 'tcp',  'help_link': help_1}, points=2))
    tests.append(check_answer('1b', 'SSH port', text, {'answers': '22',  'help_link': help_1}, points=2))
    tests.append(check_answer('2a', 'HTTP protocol', text, {'answers': 'tcp',  'help_link': help_1}, points=2))
    tests.append(check_answer('2b', 'HTTP port', text, {'answers': '80',  'help_link': help_1}, points=2))
    tests.append(check_answer('3a', 'HTTPS protocol', text, {'answers': 'tcp',  'help_link': help_1}, points=2))
    tests.append(check_answer('3b', 'HTTPS port', text, {'answers': '443',  'help_link': help_1}, points=2))
    tests.append(check_answer('4a', 'ping protocol', text, {'answers': 'icmp',  'help_link': help_1}, points=2))
    tests.append(check_answer('4b', 'ping port', text, {'answers': 'none',  'help_link': help_1}, points=2))
    tests.append(check_answer('5a', 'DNS protocol', text, {'answers': '(both|tcp|udp)',  'help_link': help_1}, points=2))
    tests.append(check_answer('5b', 'DNS port', text, {'answers': '53',  'help_link': help_1}, points=2))
    tests.append(check_answer('6a', 'DHCP protocol', text, {'answers': 'udp',  'help_link': help_1}, points=2))
    tests.append(check_answer('6b', 'DHCP port', text, {'answers': ['67', '68'], 'min_matches': 2,
                                                        'help_link': help_1}, points=2))
    tests.append(check_answer('7a', 'RDP protocol', text, {'answers': '(both|tcp)', 'help_link': help_1}, points=2))
    tests.append(check_answer('7b', 'RDP port', text, {'answers': '3389', 'help_link': help_1}, points=2))
    tests.append(check_answer('8a', 'Screenshot Nmap is running', text, {'screenshot': True, }, points=1))
    tests.append(check_answer('9a', 'Nmap scan', text,
                              {'answers': [r'starting \s nmap', r' host \s is \s up', r'nmap \s done'],
                               'min_matches': 3, 'help_link': help_explain}, points=5))
    tests.append(check_answer('9b', 'Nmap scan, ports', text, {'answers': r'[0-9]+',  'help_link': help_1}, points=4))
    tests.append(check_answer('9c', 'Nmap scan, TCP/UDP', text, {'answers': r'tcp',  'help_link': help_1}, points=1))
    tests.append(check_answer('9d', 'Nmap scan, Describe services?', text,
                              {'min_words': 7,  'help_link': help_1}, points=1))
    tests.append(check_answer('10a', 'Nmap scan, UDP port', text,
                              {'answers': [r'starting \s nmap', r'nmap \s done', '53'],
                               'min_matches': 3, 'help_link': help_explain}, points=10))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]