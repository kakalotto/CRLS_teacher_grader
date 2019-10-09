def docs_feedback_research_yourself(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, keyword_and_length

    tests = list()
    text = get_text(link)
    print(text)
    test_info = keyword_and_length('Info', [r'[a-zA-Z]+'], text,
                                   search_string=r'here\syou\sfound\sit\ntabledata (.+?) tabledata', min_length=2,
                                   points=1)
    test_where = keyword_and_length('Where you found it', [r'.+'], text,
                                    search_string=r'here\syou\sfound\sit\ntabledata .+? tabledata (.+?) 2a',
                                    min_length=2, points=1)
    test2a = keyword_and_length('2a connect the dots', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 3a', min_length=4, points=1)
    test3a = keyword_and_length('3a biggest threat to security', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 3b', min_length=4, points=1)
    test3b = keyword_and_length('3b Why do you think so', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .+? tabledata (.+) ', min_length=4, points=1)
    tests.extend([test_info, test_where, test2a, test3a, test3b])
    return tests
