def docs_feedback_routers_and_redundancy(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1 = keyword_and_length('question 1', [r'[a-zA-Z]+'], text,
                               search_string=r'1. .+? tabledata (.+) 2.', min_length=1,
                               points=1)
    test2 = keyword_and_length('question 2', [r'[a-zA-Z]+'], text,
                               search_string=r'2. .+? tabledata (.+) 3.', min_length=5,
                               points=1)
    test3 = keyword_and_length('question 3', [r'[a-zA-Z]+'], text,
                               search_string=r'3. .+? tabledata (.+) 4.', min_length=1,
                               points=1)
    test4 = keyword_and_length('question 4', [r'[a-zA-Z]+'], text,
                               search_string=r'4\. .+? tabledata (.+?) ind', min_length=10,
                               points=1)
    test5 = keyword_and_length('question 5', [r'[a-zA-Z]+'], text,
                               search_string=r'5. .+? tabledata (.+) 6.', min_length=1,
                               points=1)
    test6 = keyword_and_length('question 6', [r'[a-zA-Z]+'], text,
                               search_string=r'6. .+? tabledata (.+) 7.', min_length=7,
                               points=1)
    test7 = keyword_and_length('question 7', [r'[a-zA-Z]+'], text,
                               search_string=r'7. .+? tabledata (.+) 8.', min_length=1,
                               points=1)
    test8 = keyword_and_length('question 8', [r'[a-zA-Z]+'], text,
                               search_string=r'8. .+? tabledata (.+) 9.', min_length=5,
                               points=1)
    test9 = keyword_and_length('question 9', [r'[a-zA-Z]+'], text,
                               search_string=r'9. .+? tabledata (.+) 10a.', min_length=5,
                               points=1)
    test10a = keyword_and_length('question 10a', [r'[a-zA-Z]+'], text,
                                 search_string=r'10a. .+? tabledata (.+) 10b.', min_length=5,
                                 points=1)
    test10b = keyword_and_length('question 10b', [r'[a-zA-Z]+'], text,
                                 search_string=r'10b. .+? tabledata (.+) $', min_length=10,
                                 points=1)

    tests.extend([test1, test2, test3, test4, test5, test6, test7, test8, test9, test10a, test10b])
    return tests

