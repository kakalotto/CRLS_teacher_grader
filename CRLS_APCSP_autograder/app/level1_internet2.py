
def route_docs_level1_internet_2(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=52, score_manual=8)
    text = get_text(link)

    ip_help = 'https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm'
    ip_do_help = 'https://docs.google.com/document/d/1NvIejwN_QqwRFNNx7zqPwwThnlS-B1vLZEFoYSl1wYo/' \
                 'edit#bookmark=id.5xvsbxvda9hj'
    dns_help = 'https://docs.google.com/document/d/1NvIejwN_QqwRFNNx7zqPwwThnlS-B1vLZEFoYSl1wYo/edit' \
               '#bookmark=id.o3blb3t16m2f'
    router_help = 'https://docs.google.com/document/d/1NvIejwN_QqwRFNNx7zqPwwThnlS-B1vLZEFoYSl1wYo/' \
                  'edit#bookmark=id.xzq2e5saunfi'
    dhcp_help = 'https://docs.google.com/document/d/1NvIejwN_QqwRFNNx7zqPwwThnlS-B1vLZEFoYSl1wYo/' \
                'edit#bookmark=id.kopkmtuk9fqg'
    help_ping = 'https://docs.google.com/presentation/d/1N3cpcrAftjiR8a_dR5-sULx_3IUjkzfO8zHC2wkz9vA/' \
                'edit#slide=id.g9d3ea45fdc_0_0'
    nslookup_help = 'https://docs.google.com/document/d/1NvIejwN_QqwRFNNx7zqPwwThnlS-B1vLZEFoYSl1wYo/' \
                    'edit#bookmark=id.2j0fs3ia0pzd'
    nslookup_google = 'https://www.ionos.com/digitalguide/server/tools/nslookup/'
    help_tracert = 'https://docs.google.com/presentation/d/1N3cpcrAftjiR8a_dR5-sULx_3IUjkzfO8zHC2wkz9vA/' \
                   'edit#slide=id.g9d3ea45fdc_0_8'

    tests.append(check_answer('1a', 'What is an IP address', text, {'min_words': 5, 'help_link': ip_help, },
                              points=1))
    tests.append(check_answer('1b', 'Your IP address?', text, {'answers': r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+',
                                                               'help_link': ip_do_help, }, points=5))
    tests.append(check_answer('1c', 'Your DNS addresses?', text, {'answers': r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+',
                                                                  'help_link': dns_help, }, points=5))
    tests.append(check_answer('1d', 'Your router??', text, {'answers': r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+',
                                                            'help_link': router_help, }, points=5))
    tests.append(check_answer('1e', 'Your DHCP server??', text, {'answers': r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+',
                                                                 'help_link': dhcp_help, }, points=5))
    tests.append(check_answer('2a', 'Ping a machine', text,
                              {'answers': ['pinging', 'reply'], 'min_matches': 2,  'help_link': help_ping}, points=5))
    tests.append(check_answer('2b', 'Ping a amazon in Japan', text,
                              {'answers': ['pinging', 'reply', r'amazon\.co\.jp'],
                               'min_matches': 3,  'help_link': help_ping}, points=5))
    tests.append(check_answer('2c', 'Ping africa.mit.edu', text,
                              {'answers': ['ping', r'request \s timed \s out'],
                               'min_matches': 2, 'help_link': help_ping}, points=5))
    tests.append(check_answer('3a', 'nslookup', text,
                              {'answers': ['server', r'name'],
                               'min_matches': 2, 'help_link': nslookup_help}, points=5))
    tests.append(check_answer('3b', 'What does nslookup mean', text, {'min_words': 5, 'help_link': nslookup_google, },
                              points=1))
    tests.append(check_answer('4a', 'tracert', text,
                              {'answers': ['hops', r'ms'], 'min_matches': 2, 'help_link': help_tracert}, points=5))
    tests.append(check_answer('4b', 'Explain the tracert?', text,
                              {'min_words': 10, 'help_link': help_tracert}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]