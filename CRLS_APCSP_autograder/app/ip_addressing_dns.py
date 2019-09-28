def docs_feedback_ip_addressing_dns(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1 = keyword_and_length('question 1a', [r'(standard|rule)'], text,
                                search_string=r'1. .+? tabledata (.+) 2a.', min_length=5,
                                points=5)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 2b.', min_length=1,
                                points=1)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b. .+? tabledata (.+) 3a', min_length=7, points=1)
    test3a = keyword_and_length('question 3a', [r'32 \s* b*'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=1, points=5)

    test3b = keyword_and_length('question 3b', [r'4\s*billion', '2 .+32', '4[\s,]*294[\s,]*967[\s,]*296'], text,
                                search_string=r'3b. .+? tabledata (.+) 4a', min_length=1, points=5)

    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]'], text,
                                search_string=r'4a\. .+? tabledata (.+?) 4b\.', min_length=7, points=1)
    test4b = keyword_and_length('question 4b', [r'[a-zA-Z]'], text,
                                search_string=r'4b\. .+? tabledata (.+?) 5', min_length=7, points=1)
    test5 = keyword_and_length('question 5', [r'[a-zA-Z]+'], text,
                                search_string=r'5\. .+? tabledata (.+?) 6\.', min_length=6, points=1)
    test6 = keyword_and_length('question 6', [r'[a-zA-Z]+'], text,
                                search_string=r'6\. .+? tabledata (.+?) 7\.', min_length=10, points=1)
    test7 = keyword_and_length('question 7', [r'[a-zA-Z]+'], text,
                                search_string=r'7\. .+? tabledata (.+?) 8\.', min_length=5, points=1)
    tests.extend([test1, test2a, test2b, test3a, test3b, test4a, test4b, test5, test6, test7,  ])
    return tests
