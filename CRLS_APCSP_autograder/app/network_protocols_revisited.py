def route_docs_network_protocols_revisited(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='IT2 Scholar', score_max=50, score_manual=50)
    text = get_text(link)
    help_ping = 'https://docs.google.com/presentation/d/1N3cpcrAftjiR8a_dR5-sULx_3IUjkzfO8zHC2wkz9vA/' \
                'edit#slide=id.g9d3ea45fdc_0_0'
    help_tracert = 'https://docs.google.com/presentation/d/1N3cpcrAftjiR8a_dR5-sULx_3IUjkzfO8zHC2wkz9vA/' \
                   'edit#slide=id.g9d3ea45fdc_0_8'
    help_udptcp = 'https://drive.google.com/drive/folders/1S3FDXNtNp7HdT9Z9zrkpEl0YMaulEDZK'
    help_tcp = 'https://duckduckgo.com/?q=tcp+handshake&t=h_&ia=web'
    help_ports = 'https://duckduckgo.com/?q=http+port'
    help_duckduckgo = 'https://duckduckgo.com/?q=http+port'
    help_netstat = 'https://help.fasthosts.co.uk/app/answers/detail/a_id/1552/~/netstat-explained'
    tests.append(check_answer('1a', 'Ping a machine', text,
                              {'answers': ['pinging', 'reply'], 'min_matches': 2,  'help_link': help_ping}, points=5))
    tests.append(check_answer('1b', 'Ping africa.mit.edu', text,
                              {'answers': ['ping', r'request \s timed \s out'],
                               'min_matches': 2, 'help_link': help_ping}, points=5))
    tests.append(check_answer('2a', 'tracert', text,
                              {'answers': ['hops', r'ms'], 'min_matches': 2, 'help_link': help_tracert}, points=5))
    tests.append(check_answer('2b', 'Explain the tracert?', text,
                              {'min_words': 10, 'help_link': help_tracert}, points=1))
    tests.append(check_answer('2c', 'tracert on local machine?', text,
                              {'min_words': 10, 'help_link': help_tracert}, points=1))
    tests.append(check_answer('3a', 'UDP/TCP table?', text, {'min_words': 1, 'help_link': help_udptcp}, points=1))
    tests.append(check_answer('3b', 'Explain handshake', text, {'min_words': 8, 'help_link': help_tcp}, points=1))
    tests.append(check_answer('4a', 'http port', text, {'answers': '80', 'help_link': help_ports}, points=2))
    tests.append(check_answer('4b', 'http use', text, {'min_words': 2, 'help_link': help_duckduckgo}, points=1))
    tests.append(check_answer('5a', 'https port', text, {'answers': '443', 'help_link': help_ports}, points=2))
    tests.append(check_answer('5b', 'https use', text, {'min_words': 2, 'help_link': help_duckduckgo}, points=1))
    tests.append(check_answer('6a', 'DNS port', text, {'answers': '53', 'help_link': help_ports}, points=2))
    tests.append(check_answer('6b', 'DNS use', text, {'min_words': 2, 'help_link': help_duckduckgo}, points=1))
    tests.append(check_answer('7a', 'DHCP port', text, {'answers': '67', 'help_link': help_ports}, points=2))
    tests.append(check_answer('7b', 'DHCP use', text, {'min_words': 2, 'help_link': help_duckduckgo}, points=1))
    tests.append(check_answer('8a', 'RDP port', text, {'answers': '3389', 'help_link': help_ports}, points=2))
    tests.append(check_answer('8b', 'RDP use', text, {'min_words': 2, 'help_link': help_duckduckgo}, points=1))
    tests.append(check_answer('9a', 'Netstat', text,
                              {'answers': ['tcp', 'established', 'udp', 'connections'], 'min_matches': 4,
                               'help_link': help_netstat}, points=15))
    tests.append(check_answer('9b', 'Ports and their use', text, {'min_words': 10, 'help_link': help_ports}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]