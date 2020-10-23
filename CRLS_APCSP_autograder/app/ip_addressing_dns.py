def route_docs_ip_addressing_dns(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=22, score_manual=28)
    text = get_text(link)
    site = 'https://www.youtube.com/watch?v=5o8CwafCxnU'
    tests.append(check_answer('1a', 'What is a protocol', text, {'answers': r'(standard|rule)', 'help_link': site, },
                              points=5))
    tests.append(check_answer('2a', 'What is IP address', text, {'min_words': 4, 'help_link': site, },
                              points=1))
    tests.append(check_answer('2b', 'How IP organized hierarchically', text, {'min_words': 5, 'help_link': site, },
                              points=1))
    tests.append(check_answer('3a', 'How many bits in IP address', text, {'answers': '32', 'help_link': site, },
                              points=5))
    tests.append(check_answer('3b', 'How many IP address', text,
                              {'answers': [r'4\s*billion', '2 .+32', r'4[\s,]*294[\s,]*967[\s,]*296',
                                           r'4 [\s,]* 000 [\s,]* 000 [\s,]* 000'], 'help_link': site, },
                              points=5))
    tests.append(check_answer('4a', 'Difference btwn IPv6 and IPv4', text, {'min_words': 7, 'help_link': site, },
                              points=1))
    tests.append(check_answer('4b', 'Why need IPv6', text, {'min_words': 7, 'help_link': site, }, points=1))
    tests.append(check_answer('5a', 'What is packet', text, {'min_words': 6, 'help_link': site, }, points=1))
    tests.append(check_answer('6a', 'Packet, address difference', text, {'min_words': 7, 'help_link': site, },
                              points=1))
    tests.append(check_answer('7a', 'Purpose of DNS', text, {'min_words': 5, 'help_link': site, },
                              points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]