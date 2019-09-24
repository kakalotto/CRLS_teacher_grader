def docs_feedback_encryption_4(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1a = keyword_and_length('question 1a', [r'5\s*s'], text,
                                search_string=r'1a. .+? tabledata (.+) 2a.', min_length=1,
                                points=10)
    test2a = keyword_and_length('question 2a', [r'2\s*d'], text,
                                search_string=r'2a. .+? tabledata (.+) 2b.', min_length=1,
                                points=5)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b. .+? tabledata (.+) 3a', min_length=10, points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 3b', min_length=2, points=1)
    test3b = keyword_and_length('question 3b', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .+? tabledata (.+) 4a', min_length=8, points=1)

    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]'], text,
                                search_string=r'4a. .+? tabledata (.+) 5a', min_length=1, points=1)
    test5a = keyword_and_length('question 5a', [r'[a-zA-Z]+'], text,
                                search_string=r'5a. .+? tabledata (.+) $', min_length=10, points=1)
    tests.extend([test1a, test2a, test2b, test3a, test3b, test4a, test5a, ])
    return tests
