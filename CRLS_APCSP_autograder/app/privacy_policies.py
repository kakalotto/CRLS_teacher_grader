def route_docs_privacy_policies(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=11, score_manual=39)
    text = get_text(link)
    site = "https://docs.google.com/presentation/d/1NeT_90quKMia9GyMkF2gr30IHuvrCrHutAjoRvzHajQ/" \
           "edit#slide=id.g89515ff0b8_0_0"
    five_word_test = {'min_words': 5, 'help_link': site}

    tests.append(check_answer('0a', 'Website', text, {'min_words': 1, 'help_link': site}, points=1))
    tests.append(check_answer('1a', 'What kinds of data being collected?', text, five_word_test, points=1))
    tests.append(check_answer('1b', 'How many different kinds of data?', text, five_word_test, points=1))
    tests.append(check_answer('2a', 'What service or feature is enabled by data?', text, five_word_test, points=1))
    tests.append(check_answer('2b', 'Why are they collecting it?', text, five_word_test, points=1))
    tests.append(check_answer('3a', 'Who else given access to data?', text, five_word_test, points=1))
    tests.append(check_answer('3b', 'How are they using it?', text, five_word_test, points=1))
    tests.append(check_answer('4a', 'Can you access own data?', text, five_word_test, points=1))
    tests.append(check_answer('4b', 'Can you modify or delete data?', text, five_word_test, points=1))
    tests.append(check_answer('5a', 'Rate 1-4?', text, {'min_words': 1, 'help_link': site}, points=1))
    tests.append(check_answer('5b', 'Justify answer', text, five_word_test, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]