def route_docs_encoding_color(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=21, score_manual=9)
    text = get_text(link)
    vid_1_link = 'https://www.youtube.com/watch?time_continue=173&v=763E3_Z6Hng&feature=emb_title'
    vid_2_link = 'https://www.youtube.com/watch?v=xK9z51Tin4E&feature=emb_title'
    color_link = 'https://docs.google.com/presentation/d/1lfpOt-GgrmS_a3A47ir3SumrkmtCRYngGHJe04EJloE/' \
                 'edit#slide=id.g8c2e1fa145_0_10'
    size_link = 'https://docs.google.com/presentation/d/1lfpOt-GgrmS_a3A47ir3SumrkmtCRYngGHJe04EJloE/' \
                'edit#slide=id.g8c2e1fa145_0_18'
    tests.append(check_answer('1a', '6 other colors?', text,
                              {'answers': [r'0000 \s 0100 \n 0000 \s 0010 \n 0000 \s 0011 \n .*? 001 ',
                                           r'0000 \s 0100 \n 0000 \s 0010 \n 0000 \s 0011 \n .*? 011 ',
                                           r'0000 \s 0100 \n 0000 \s 0010 \n 0000 \s 0011 \n .*? 101 ',
                                           r'0000 \s 0100 \n 0000 \s 0010 \n 0000 \s 0011 \n .*? 110 ',
                                           r'0000 \s 0100 \n 0000 \s 0010 \n 0000 \s 0011 \n .*? 000 ',
                                           r'0000 \s 0100 \n 0000 \s 0010 \n 0000 \s 0011 \n .*? 111 ',
                                           r'0000 \s 0100 \n 0000 \s 0010 \n 0000 \s 0011 \n .*? 100 ',
                                           r'0000 \s 0100 \n 0000 \s 0010 \n 0000 \s 0011 \n .*? 110 '
                                           ],
                               'min_matches': 8, 'help_link': vid_1_link}, points=5))
    tests.append(check_answer('2a', '8 other colors, green/blue?', text,
                              {'answers': [r'0000 \s 0100 \n 0000 \s 0011 \n 0000 \s 0110 \n '
                                           r'000000 \s 010000 \s 100000 \s 110000  .*? 001000',
                                           r'0000 \s 0100 \n 0000 \s 0011 \n 0000 \s 0110 \n '
                                           r'000000 \s 010000 \s 100000 \s 110000  .*? 000100',
                                           r'0000 \s 0100 \n 0000 \s 0011 \n 0000 \s 0110 \n '
                                           r'000000 \s 010000 \s 100000 \s 110000  .*? 001100',
                                           r'0000 \s 0100 \n 0000 \s 0011 \n 0000 \s 0110 \n '
                                           r'000000 \s 010000 \s 100000 \s 110000  .*? 000000',
                                           r'0000 \s 0100 \n 0000 \s 0011 \n 0000 \s 0110 \n '
                                           r'000000 \s 010000 \s 100000 \s 110000  .*? 000010',
                                           r'0000 \s 0100 \n 0000 \s 0011 \n 0000 \s 0110 \n '
                                           r'000000 \s 010000 \s 100000 \s 110000  .*? 000011',
                                           r'0000 \s 0100 \n 0000 \s 0011 \n 0000 \s 0110 \n '
                                           r'000000 \s 010000 \s 100000 \s 110000  .*? 000001',
                                           r'0000 \s 0100 \n 0000 \s 0011 \n 0000 \s 0110 \n '
                                           r'000000 \s 010000 \s 100000 \s 110000  .*? 000000',
                                           ],
                               'min_matches': 8, 'help_link': vid_2_link}, points=5))
    tests.append(check_answer('3a', 'Multiple choice', text, {'answers': r'b'}, points=2))
    tests.append(check_answer('3b', '3b checkoff', text, {'min_words': 10}, points=1))

    tests.append(check_answer('4a', 'How many times more color', text,
                              {'answers': r'(8|2 .*? 3)', 'help_link': color_link}, points=1))
    tests.append(check_answer('4b', 'Explain 4a', text, {'min_words': 2, 'help_link': color_link}, points=1))
    tests.append(check_answer('4c', 'How many times bigger file?', text, {'answers': r'2', 'help_link': size_link},
                              points=5))
    tests.append(check_answer('4d', 'Explain 4c', text, {'min_words': 3, 'help_link': size_link}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
