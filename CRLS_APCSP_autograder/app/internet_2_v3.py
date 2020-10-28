def route_docs_internet_2_v3(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=32, score_manual=44)
    text = get_text(link)
    protocol_link = 'https://docs.google.com/presentation/d/1h0U4H1Nhk-r5-01I-_vZlQArdDcsaEjuZeW7QlCn5Gs/' \
                    'edit#slide=id.g8fe2f3ca74_0_0'
    scaling_link = 'https://docs.google.com/presentation/d/1h0U4H1Nhk-r5-01I-_vZlQArdDcsaEjuZeW7QlCn5Gs/' \
                   'edit#slide=id.g8fe2f3ca74_2_0'
    routing_link = 'https://docs.google.com/presentation/d/1h0U4H1Nhk-r5-01I-_vZlQArdDcsaEjuZeW7QlCn5Gs/' \
                   'edit#slide=id.g8fe2f3ca74_1_0'
    tests.append(check_answer('1a', 'Packets guaranteed to arrive in order? ', text,
                              {'answers': r'no', 'help_link': protocol_link}, points=5))
    tests.append(check_answer('1b', 'Protocol name? ', text,
                              {'answers': r'tcp', 'help_link': protocol_link}, points=5))
    tests.append(check_answer('1c', 'Explain protocol ', text,
                              {'min_words': 10, 'help_link': protocol_link}, points=1))
    tests.append(check_answer('1d', 'Other protocol name? ', text,
                              {'answers': r'udp', 'help_link': protocol_link}, points=5))
    tests.append(check_answer('2a', 'Computing device ', text, {'min_words': 2}, points=1))
    tests.append(check_answer('2b', 'Computing system ', text, {'min_words': 2}, points=1))
    tests.append(check_answer('2c', 'Computing network ', text, {'min_words': 2}, points=1))
    tests.append(check_answer('3a', 'Fault-tolerant routing and scaling', text,
                              {'min_words': 10, 'help_link': scaling_link}, points=1))
    tests.append(check_answer('3b', 'Protocols and scaling', text,
                              {'min_words': 10, 'help_link': scaling_link}, points=1))
    tests.append(check_answer('4a', 'What is going on?', text,
                              {'min_words': 10, 'help_link': routing_link}, points=1))
    tests.append(check_answer('4b', 'Min number', text,
                              {'answers': '2', 'help_link': routing_link}, points=5))
    tests.append(check_answer('4c', 'Max number', text,
                              {'answers': '8', 'help_link': routing_link}, points=5))
    tests.append(check_answer('5a', 'code.org Jesse', text,
                              {'answers': 'b', 'wrong_answers': ['a', 'c', 'd'], 'help_link': routing_link},
                              points=2.5))
    tests.append(check_answer('5b', 'code.org Internet', text,
                              {'answers': 'd', 'wrong_answers': ['a', 'b', 'c'], 'help_link': scaling_link},
                              points=2.5))
    tests.append(check_answer('5c', 'code.org Internet responding', text,
                              {'answers': 'c', 'wrong_answers': ['a', 'b', 'd'], 'help_link': scaling_link},
                              points=2.5))
    tests.append(check_answer('5d', 'code.org Emilee', text,
                              {'answers': 'd', 'wrong_answers': ['a', 'b', 'c'], 'help_link': protocol_link},
                              points=2.5))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]