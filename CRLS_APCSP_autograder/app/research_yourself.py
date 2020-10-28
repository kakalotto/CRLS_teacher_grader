def route_docs_research_yourself(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=5, score_manual=45)
    text = get_text(link)
    five_word_test = {'min_words': 5, 'help_link': 'https://docs.google.com/presentation/d/1quGvNvv-IE9vXYRkKKnOUEU24L'
                                                   'KbMnPXMnF1zjFeNqo/edit#slide=id.p'}
    tests.append(check_answer('1a', 'Information', text, five_word_test, points=1))
    tests.append(check_answer('1b', 'Where you found it', text, five_word_test, points=1))
    tests.append(check_answer('2a', 'Connect the dots', text, five_word_test, points=1))
    tests.append(check_answer('3a', 'Biggest threat to security', text, five_word_test, points=1))
    tests.append(check_answer('3b', 'Why do you think so', text, five_word_test, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]