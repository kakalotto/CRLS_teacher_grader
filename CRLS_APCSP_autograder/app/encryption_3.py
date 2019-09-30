
def docs_feedback_encryption_3(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)
    test1a = keyword_and_length('question 1a', [r'[a-zA-Z]+'], text,
                                search_string=r'1a. .+? tabledata (.+) 2a.', min_length=10,
                                points=1)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 3a.', min_length=10,
                                points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 4a', min_length=7, points=1)

    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]'], text,
                                search_string=r'4a. .+? tabledata (.+) 4b', min_length=7, points=1)
    test4b = keyword_and_length('question 4b', [r'\s*secur'], text,
                                search_string=r'4b. .+? tabledata (.+) 5', min_length=1, points=5)
    test5a = keyword_and_length('question 5a', [r'[a-zA-Z]+'], text,
                                search_string=r'5a. .+? tabledata (.+) 6a', min_length=8, points=1)
    test6a = keyword_and_length('question 6a', [r'[a-zA-Z]+'], text,
                                search_string=r'6a. .+? tabledata (.+?) 6b', min_length=7, points=1)
    test6b = keyword_and_length('question 6b', [r'[a-zA-Z]+'], text,
                                search_string=r'6b. .+? tabledata (.+?) 6c', min_length=7, points=1)
    test6c = keyword_and_length('question 6c', [r'[a-zA-Z]+'], text,
                                search_string=r'6c. .+? tabledata (.+?) $', min_length=7, points=1)

    tests.extend([test1a, test2a, test3a, test4a, test4b, test5a, test6a, test6b, test6c ])
    return tests


