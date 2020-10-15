# noinspection SpellCheckingInspection
def route_docs_encryption_3(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import check_answer, get_text
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=22, score_manual=28)
    text = get_text(link)
    code_org_link = 'https://www.youtube.com/watch?v=ZghMPWGXexs'
    ssl_link = 'https://docs.google.com/presentation/d/1KAj7ZMwOAmp7T_4oHptE1QKooz4wYhDopXAv-ffEiXU/' \
               'edit#slide=id.g20b16bedb6_0_12'
    ca_link = 'https://drive.google.com/file/d/15QeJGgZm4mfd0nyNVjHrLOkhnr6RvQKX/view?t=3m36s'
    summary_link = 'https://docs.google.com/presentation/d/1KAj7ZMwOAmp7T_4oHptE1QKooz4wYhDopXAv-ffEiXU/' \
                   'edit#slide=id.g8f35ed13ac_0_11'
    tests.append(check_answer('2a', 'Describe process checkoff', text,
                              {'answers': ['public', 'private', 'encrypt', 'decrypt'],  'min_matches': 4,
                               'help_link': code_org_link}, points=5))
    tests.append(check_answer('3a', 'Why public key hard to crack', text,
                              {'min_words': 7, 'help_link': code_org_link}, points=1))
    tests.append(check_answer('4a', 'What is SSL/TLS', text,
                              {'min_words': 7, 'help_link': ssl_link}, points=1))
    tests.append(check_answer('4b', 'What does s refer to in https', text,
                              {'answers': r'secur', 'help_link': ssl_link}, points=5))
    tests.append(check_answer('5a', 'What are digital certificates', text,
                              {'min_words': 8, 'help_link': ca_link}, points=1))
    tests.append(check_answer('6a', 'Oh no public key out', text, {'min_words': 7, }, points=1))
    tests.append(check_answer('6b', 'Be like Amazon, set up a key', text, {'min_words': 7, }, points=1))
    tests.append(check_answer('6c', 'Logging onto instachat', text, {'min_words': 7, }, points=1))
    tests.append(check_answer('7a', 'Pick all that are true part 1', text,
                              {'answers': ['a', 'b', 'd'], 'wrong_answers': ['c', 'e'],
                               'help_link': summary_link}, points=2.5))
    tests.append(check_answer('7b', 'Pick all that are true part 2', text,
                              {'answers': ['b', 'c'], 'wrong_answers': ['a', 'd', 'e'],
                               'help_link': summary_link}, points=2.5))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]