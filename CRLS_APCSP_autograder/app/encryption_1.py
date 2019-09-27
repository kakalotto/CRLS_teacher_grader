def docs_feedback_encryption_1(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1a = keyword_and_length('question 1a', ['\s*26!\s*', '\ss*4\.[0-9]+ .+ 26\s*', '\s* 26 \s* factorial',
                                                '\s*26\s*x\s*25\s*x\s*24'], text,
                                search_string=r'1a. .+? tabledata (.+) 1b', min_length=1, points=5)
    test1b = keyword_and_length('question 1b', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'1b. .+? tabledata (.+?) 2a', min_length=1, points=1)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 2b', min_length=10, points=1)
    test2b = keyword_and_length('question 2b', [r'\s* 1\.6[0-9]+ .+ 25'], text,
                                search_string=r'2b. .+? tabledata (.+) 2c', min_length=1, points=5)
    test2c = keyword_and_length('question 2c', [r'[a-zA-Z]+'], text,
                                search_string=r'2c. .+? tabledata (.+?) 3a', min_length=3, points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 3b', min_length=10, points=1)
    test3b = keyword_and_length('question 3b', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .+? tabledata (.+) 4a', min_length=10, points=1)
    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+) 4b', min_length=8, points=1)
    test4b = keyword_and_length('question 4b', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) ith', min_length=8, points=1)
                                  
    tests.extend([test1a, test1b, test2a, test2b, test2c, test3a, test3b, test4a, test4b, ])
    return tests
