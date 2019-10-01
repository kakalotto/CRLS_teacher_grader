def docs_feedback_encryption_2(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test1a = keyword_and_length('question 1a', [r'[^\s]+'], text,
                                search_string=r'1a. .+? tabledata .+? tabledata (.+) tabledata .+? 1b', min_length=1,
                                points=3)
    test1b = keyword_and_length('question 1b', [r'[^\s]+'], text,
                                search_string=r'1b. .+? tabledata .+? tabledata (.+) tabledata .+? 1c', min_length=1,
                                points=3)
    test1c = keyword_and_length('question 1c', [r'[^\s]+'], text,
                                search_string=r'1c. .+? tabledata .+? tabledata (.+) tabledata .+? 1d', min_length=1,
                                points=3)
    test1d = keyword_and_length('question 1d', [r'[^\s]+'], text,
                                search_string=r'1d. .+? tabledata .+? tabledata (.+) tabledata .+? 1e', min_length=1,
                                points=3)
    test1e = keyword_and_length('question 1e', [r'[^\s]+'], text,
                                search_string=r'1e. .+? tabledata .+? tabledata (.+) hought', min_length=1,
                                points=3)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 2b', min_length=10, points=1)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b. .+? tabledata (.+) 3a', min_length=10, points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 4a', min_length=10, points=1)
    test4a = keyword_and_length('question 4a', [r'no'], text,
                                search_string=r'4a. .+? tabledata (.+?) 4b', min_length=1, points=5)
    test4b = keyword_and_length('question 4b', [r'[a-zA-Z]+'], text,
                                search_string=r'4b. .+? tabledata (.+?) utograder', min_length=7, points=1)
    
    tests.extend([test1a, test1b, test1c, test1d, test1e, test2a, test2b, test3a, test4a, test4b, ])
    return tests
