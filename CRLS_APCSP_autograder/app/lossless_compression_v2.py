def route_docs_lossless_compression_v2(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=15, score_manual=22)
    text = get_text(link)
    help_widget = 'https://www.youtube.com/watch?v=LCGkcn1f-ms&t=2m46s'
    help_lossless = 'https://docs.google.com/presentation/d/1cyP2FnxtN6JsI2EMKMUWW8675z7d2VmV0HjR55rzAxQ/' \
                    'edit#slide=id.g8d9ec4a23d_0_10'
    tests.append(check_answer('1a', 'song name', text, {'answers': r'[a-zA-Z0-9]+'}, points=5))
    tests.append(check_answer('2a', 'Copy+paste compressed song', text, {'answers': r'[a-zA-Z0-9]+',
                                                                         'help_link': help_widget}, points=1))
    tests.append(check_answer('3a', 'Copy+paste dictionary', text, {'answers': r'[a-zA-Z0-9]+',
                                                                    'help_link': help_widget}, points=1))
    tests.append(check_answer('4a', 'Copy+paste stats', text, {'min_words': 13,
                                                               'help_link': help_widget}, points=1))
    tests.append(check_answer('5a', 'What made compression hard', text, {'min_words': 10}, points=1))
    tests.append(check_answer('5b', 'What is the most important quality of lossless compression?', text,
                              {'answers': 'b', 'help_link': help_lossless}, points=5))
    tests.append(check_answer('5c', 'explain what is happening?', text,
                              {'min_words': 10, 'help_link': help_lossless}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
