def route_docs_visualization_exploring_trends(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=13, score_manual=37)
    text = get_text(link)
    google_help = 'https://support.google.com/trends/answer/' \
                  '4365533?hl=en&ref_topic=4365599&visit_id=637325474152657857-2432839014&rd=1'
    # dd_help = 'https://apcentral.collegeboard.org/pdf/ap-computer-science-principles-' \
    #          'conceptual-framework-2020-21.pdf#page=38'
    tests.append(check_answer('1a', 'Where data comes from', text,
                              {'min_words': 7, 'help_link': google_help}, points=1))
    tests.append(check_answer('2a', 'How data adjusted', text,
                              {'min_words': 7, 'help_link': google_help}, points=1))
    tests.append(check_answer('2b', 'Value of 100', text,
                              {'min_words': 7, 'help_link': google_help}, points=1))
    tests.append(check_answer('3a', 'Digital divide?', text,
                              {'min_words': 10, 'help_link': google_help}, points=1))
    tests.append(check_answer('3b', 'Digital divide affect result?', text,
                              {'min_words': 10, 'help_link': google_help}, points=1))
    help_link = 'https://docs.google.com/document/d/1DMWiEW-bCBr2_Per1pK74193x5kSiqPPvBxdNai9FWc/edit'
    tests.append(check_answer('4a', 'Screenshot', text,
                              {'screenshot': True, 'help_link': help_link}, points=5))
    tests.append(check_answer('5a', 'Describe terms?', text,
                              {'min_words': 10, 'help_link': help_link}, points=1))
    tests.append(check_answer('6a', 'Describe charts?', text,
                              {'min_words': 10, 'help_link': help_link}, points=1))
    tests.append(check_answer('7a', 'Plausible story?', text,
                              {'min_words': 10, 'help_link': help_link}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
