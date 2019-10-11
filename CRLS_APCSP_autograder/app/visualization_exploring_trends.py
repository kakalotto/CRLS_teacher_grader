def docs_feedback_visualization_exploring_trends(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Where data comes from', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+) 2a\.', min_length=7, points=1)
    test2a = keyword_and_length('2a. How data adjusted', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+) 2b\.', min_length=7, points=1)
    test2b = keyword_and_length('2b. Value of 100?', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+) 3a\.', min_length=7, points=1)
    test3a = keyword_and_length('3a. Digital divide?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=10, points=1)
    test3b = keyword_and_length('3b. Digital divide affect result?', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) exploring', min_length=10, points=1)
    test4a = exact_answer('4a. screenshot', [r'4a\. .+? tabledata \s* aaa \s* inlineobject \s*  5a\.'], text, points=5)
    test5a = keyword_and_length('5a. Describe terms?', [r'[a-zA-Z]+'], text,
                               search_string=r'5a\. .+? tabledata (.+)  6a\.', min_length=10, points=1)
    test6a = keyword_and_length('6a. Describe charts?', [r'[a-zA-Z]+'], text,
                               search_string=r'6a\. .+? tabledata (.+)  7a\.', min_length=10, points=1)
    test7a = keyword_and_length('7a. Plausible story?', [r'[a-zA-Z]+'], text,
                                search_string=r'7a\. .+? tabledata (.+)  $', min_length=15, points=1)

    tests.extend([test1a, test2a, test2b, test3a, test3b, test4a, test5a, test6a, test7a, ])
    return tests
    

