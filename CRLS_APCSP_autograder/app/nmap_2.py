def route_docs_nmap_2(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='IT2 Scholar', score_max=73, score_manual=27)
    text = get_text(link)
    help_1a = 'https://docs.google.com/presentation/d/1tfiyk4CUPF8neb34ddLt3fHGWDekVPDrBypGw2kBFIQ/e' \
              'dit#slide=id.g2721f22eed_1_1'
    help_2 = 'https://docs.google.com/document/d/1h1ny17on080mZsEv2fSMVq5noGiNrXML491Aqj6JarY/' \
             'edit#bookmark=id.ytbirhc8iqs6'
    help_calc = 'https://docs.google.com/presentation/d/1YCGT-dIi1q-qvnTVgJLDTnDis_EgBWbfSsHJHSMxMXo/' \
                'edit#slide=id.ga60d3c1f3c_0_0'
    help_ip = 'https://www.howtogeek.com/117371/how-to-find-your-computers-private-public-ip-addresses/'
    help_my_network = 'https://docs.google.com/presentation/d/1YCGT-dIi1q-qvnTVgJLDTnDis_EgBWbfSsHJHSMxMXo/' \
                      'edit#slide=id.ga60d3c1f3c_0_13'
    help_services = 'http://duckduckgo.com'
    tests.append(check_answer('1a', 'Explain scan efficient not complete', text,
                              {'min_words': 10, 'help_link': help_1a}, points=1))
    tests.append(check_answer('1b', 'Scenarios where scan could miss machines or services', text,
                              {'min_words': 7, 'help_link': help_1a}, points=1))
    tests.append(check_answer('2a', '20 random IPs with nmap', text,
                              {'answers': r'20 \s ip \s addresses .*? scanned', 'help_link': help_2},
                              points=15))
    tests.append(check_answer('3a', 'Your IP address', text,
                              {'answers': r'172\.25\.233\. *?', 'help_link': help_ip, }, points=5))
    tests.append(check_answer('3b', 'Your IP address', text,
                              {'answers': r'172\.25\.233\.0', 'help_link': help_calc, }, points=5))
    tests.append(check_answer('3c', 'Range of usable addresses', text,
                              {'answers': [r'172\.25\.233\.1', r'172\.25\.233\.254 '],
                               'help_link': help_calc, 'min_matches': 2}, points=5))
    tests.append(check_answer('3d', 'Copy+paste last 10 lines of scan', text,
                              {'answers': [r'ip \s addresses .*? hosts \s up '],
                               'help_link': help_my_network, }, points=19))
    tests.append(check_answer('3e', 'How many machines are alive', text,
                              {'answers': [r'[0-9]'], 'help_link': help_my_network, }, points=5))
    tests.append(check_answer('3f', 'Describe services', text,
                              {'min_words': 7, 'help_link': help_services,}, points=1))
    tests.append(check_answer('4a', '10.10.5.2/24 Network address', text,
                              {'answers': r'10\.10\.5\.0', 'help_link': help_calc, }, points=2))
    tests.append(check_answer('4b', '10.10.5.2/24 Usable hosts', text,
                              {'answers': '254', 'help_link': help_calc, }, points=2))
    tests.append(check_answer('4c', '192.168.3.22 / 255.255.240.0 Network address', text,
                              {'answers': r'192\.168\.0\.0', 'help_link': help_calc, }, points=2))
    tests.append(check_answer('4d', '192.168.3.22 / 255.255.240.0 Usable hosts', text,
                              {'answers': r'4,*094', 'help_link': help_calc, }, points=2))
    tests.append(check_answer('4e', '172.25.244.9 / 255.255.192.0  Network address', text,
                              {'answers': r'172\.25\.192\.0', 'help_link': help_calc, }, points=2))
    tests.append(check_answer('4f', '172.25.244.9 / 255.255.192.0  Usable hosts', text,
                              {'answers': r'16 ,* 382 .*?', 'help_link': help_calc, }, points=2))
    tests.append(check_answer('4g', '2.3.4.5 / 255.0.0.0 Network address', text,
                              {'answers': r'2\.0\.0\.0 ', 'help_link': help_calc, }, points=2))
    tests.append(check_answer('4h', '2.3.4.5 / 255.0.0.0  Usable hosts', text,
                              {'answers': r' 16,*777,*214', 'help_link': help_calc, }, points=2))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]