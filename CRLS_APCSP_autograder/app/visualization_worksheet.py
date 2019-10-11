def docs_feedback_visualization_worksheet(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. GPA, what is wrong?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+) 2\.', min_length=10, points=1)
    test2a = exact_answer('2a. screenshot', [r'2a\. .+? tabledata \s* aaa \s* inlineobject \s*  2b\.'], text, points=5)
    test2b = keyword_and_length('2b. Describe what you see', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+?) 2c\.', min_length=7, points=1)
    test2c = keyword_and_length('2c. Tricks?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) 3\.', min_length=10, points=1)

    test3a = keyword_and_length('3a. Correlation does not imply causation?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=10, points=1)
    test3b = keyword_and_length('3b. Dismissing correlation.', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) 4\.', min_length=10, points=1)
    test4a = exact_answer('4a. screenshot', [r'4a\. .+? tabledata \s* aaa \s* inlineobject \s*  4b\.'], text, points=1)
    test4b = keyword_and_length('4b. Explain what showing, explain why good', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) 5\.', min_length=10, points=1)
    test5a = exact_answer('5a. screenshot', [r'5a\. .+? tabledata \s* aaa \s* inlineobject \s*  5b\.'], text, points=1)
    test5b = keyword_and_length('5b. Explain why bad', [r'[a-zA-Z]+'], text,
                                search_string=r'5b\. .+? tabledata (.+?) 5c\.', min_length=10, points=1)
    test5c = exact_answer('5c. screenshot', [r'5c\. .+? tabledata \s* aaa \s* inlineobject \s*  5d\.'], text, points=1)
    test5d = keyword_and_length('5d. Explain why bad', [r'[a-zA-Z]+'], text,
                                search_string=r'5d\. .+? tabledata (.+?) 5e\.', min_length=10, points=1)
    test5e = exact_answer('5e. screenshot', [r'5e\. .+? tabledata \s* aaa \s* inlineobject \s*  5f\.'], text, points=1)
    test5f = keyword_and_length('5f. Explain why bad', [r'[a-zA-Z]+'], text,
                                search_string=r'5f\. .+? tabledata (.+?) $', min_length=10, points=1)

    tests.extend([test1a, test2a, test2b, test2c, test3a, test3b, test4a, test4b, test5a, test5b, test5c, test5d,
                  test5e, test5f])

    return tests
