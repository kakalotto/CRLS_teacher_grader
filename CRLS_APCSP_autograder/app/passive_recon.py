def route_docs_passive_recon(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='IT2 Scholar', score_max=27, score_manual=73)
    text = get_text(link)

    one_link = 'https://docs.google.com/presentation/d/1NC3z7UyPFNnns6KpimwoW2xPj5vpq_6B0picPb0jXFQ/edit'
    oneb_link = 'https://docs.google.com/presentation/d/1NC3z7UyPFNnns6KpimwoW2xPj5vpq_6B0picPb0jXFQ/' \
                'edit#slide=id.g2702873b0f_0_23'
    video_link = 'https://drive.google.com/file/d/1sw1tC-ZYLJjCqNLm5E4K0fRbiMOWL9zF/view?usp=sharing'
    heartbleed_link = 'https://duckduckgo.com/?q=what+is+heartbleed&t=h_&ia=web'
    heartbleed_fix = 'https://duckduckgo.com/?q=fix+heartbleed&t=h_&ia=web'
    freak_link = 'https://duckduckgo.com/?q=what+is+freak+vulnerability&t=h_&ia=web'
    freak_fix = 'https://duckduckgo.com/?q=fix+freak+vulnerability&t=h_&ia=web'

    tests.append(check_answer('1a', 'Advantage/disadvantage of passive recon', text,
                              {'min_words': 12, 'help_link': one_link}, points=1))
    tests.append(check_answer('1b', 'Contact info exploited by bad entities', text,
                              {'min_words': 7, 'help_link': oneb_link}, points=1))
    tests.append(check_answer('2a', 'Google as passive recon', text, {'min_words': 15}, points=1))
    tests.append(check_answer('3a', 'Whois as passive recon', text,
                              {'min_words': 10, 'help_link': video_link}, points=1))
    tests.append(check_answer('4a', 'Netcraft as passive recon', text,
                              {'min_words': 10, 'help_link': video_link}, points=1))
    tests.append(check_answer('5a', 'What is heartbleed', text, {'min_words': 7, 'help_link': heartbleed_link},
                              points=1))
    tests.append(check_answer('5b', 'Sceenshot censys.io heartbleed', text, {'screenshot': True, }, points=5))
    tests.append(check_answer('5c', 'How to fix heartbleed?', text, {'answers': ['update', 'patch', 'ssl', 'disable'],
                                                                     'help_link': heartbleed_fix}, points=5))
    tests.append(check_answer('5d', 'What is FREAK', text, {'min_words': 7, 'help_link': freak_link}, points=1))
    tests.append(check_answer('5e', 'Sceenshot censys.io FREAK', text, {'screenshot': True, }, points=5))
    tests.append(check_answer('5f', 'How to fix FREAK?', text, {'answers': ['update', 'patch', 'ssl', 'disable'],
                                                                'help_link': freak_fix}, points=5))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]