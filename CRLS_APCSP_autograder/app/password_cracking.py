def docs_feedback_password_crack(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    score_info = {'score': 0, 'max_score': 7, 'manually_scored': 93, 'finished_scoring': True}

    text = get_text(link)

    print(text)
    test2a = exact_answer('2a. screenshot new users', [r'2a\. .+? tabledata \s aaa \s inlineobject .+? 3\.'],
                           text, points=1)
    test6a = exact_answer('6a. screenshot brute force', [r'6a\. .+? tabledata \s aaa \s inlineobject .+? 6b\.'],
                           text, points=1)
    test6b = exact_answer('6b. screenshot precomputation', [r'6b\. .+? tabledata \s aaa \s inlineobject .+? 7a\.'],
                          text, points=1)
    test7a = keyword_and_length('7a. Interpret your results', [r'[a-zA-Z]+'], text,
                                search_string=r'7a\. .+? tabledata (.+) 8\.', min_length=15, points=1)
    test8a = keyword_and_length('8a. precomputation drawback', [r'[a-zA-Z]+'], text,
                                search_string=r'8a\. .+? tabledata (.+) 8b\.', min_length=15, points=1)
    test8b = keyword_and_length('8b. max length and why', [r'[a-zA-Z]+'], text,
                                search_string=r'8b\. .+? tabledata (.+) 9a\.', min_length=10, points=1)
    test9a = keyword_and_length('9a. max length and why', [r'[a-z]+'], text,
                                search_string=r'9a\. .+? tabledata (.+) $', min_length=10, points=1)
    tests.extend([test2a, test6a, test6b, test7a, test8a, test8b, test9a])
    return tests


