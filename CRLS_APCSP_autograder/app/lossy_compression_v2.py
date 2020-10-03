def route_docs_lossy_compression_v2(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=9, score_manual=21)
    text = get_text(link)
    help_lossy = 'https://drive.google.com/file/d/154inij1Qdz4vYcBCbtcLu1QI2MMtxmsn/view?t=0m52s'

    tests.append(check_answer('1a', 'Quality of the image when you compress it', text,
                              {'min_words': 5, 'help_link': help_lossy}, points=1))
    tests.append(check_answer('1b', 'Quality of the image when you compress it', text,
                              {'min_words': 5, 'help_link': help_lossy}, points=1))
    tests.append(check_answer('2a', 'Record compression, show math', text, {'min_words': 5}, points=1))
    tests.append(check_answer('2b', 'Screenshot', text, {'screenshot': True, }, points=5))
    tests.append(check_answer('3a', 'Explain categories for images, video, music (include all 3 words)',
                              text, {'answers': [r'video', 'music', 'image'], 'min_matches': 3}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]