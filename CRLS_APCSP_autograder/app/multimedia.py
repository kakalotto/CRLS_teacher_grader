def route_docs_multimedia(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=6, score_manual=94)
    text = get_text(link)
    onea_link = 'https://docs.google.com/presentation/d/1bQ8HfJUt67Lby9jASR0AVy8YW6sDl3lsP77IHlybHF0/' \
                'edit#slide=id.g9975bef7c4_0_0'
    twoa_link = 'https://docs.google.com/presentation/d/1bQ8HfJUt67Lby9jASR0AVy8YW6sDl3lsP77IHlybHF0/' \
                'edit#slide=id.g9975bef7c4_0_5'
    tests.append(check_answer('1a', '3 electronic interactive media tools', text,
                              {'min_words': 12, 'help_link': onea_link}, points=1))
    tests.append(check_answer('2a', 'Make a graphic', text,
                              {'screenshot': True, 'help_link': twoa_link}, points=1))
    tests.append(check_answer('3a', 'Make a PDF, write "done"', text, {'answers': 'done'}, points=1))
    tests.append(check_answer('4a', 'image, audio, video, 6 total', text, {'min_words': 7}, points=1))
    tests.append(check_answer('5a', 'Make a video', text, {'answers': 'done'}, points=1))
    tests.append(check_answer('6a', 'Record a sound (not) video', text, {'answers': 'done'}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
