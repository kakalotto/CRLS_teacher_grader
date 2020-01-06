def docs_feedback_two_factor_authentication(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Two factor good?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+) 2a\.', min_length=10, points=1)
    test2a = keyword_and_length('2a. Two factor bad?', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+) 3\.', min_length=10, points=1)
    test3a = exact_answer('3a. Screenshot of two-factor',
                          [r'3a\. .+? tabledata \s* aaa \s* inlineobject \s*  3b\.'], text, points=1)
    test3b = keyword_and_length('3b. Authentications more secure than before??', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) 3c\.', min_length=10, points=1)
    test3c = keyword_and_length('3c. Authentications when you lose phone?', [r'[a-zA-Z]+'], text,
                                search_string=r'3c\. .+? tabledata (.+?) 3d\.', min_length=10, points=1)
    test3d = keyword_and_length('3c. What happens when cancel two-factor??', [r'[a-zA-Z]+'], text,
                                search_string=r'3d\. .+? tabledata (.+?) 4a\.', min_length=10, points=1)
    test4a = keyword_and_length('4a. Celeb hack, what you think??', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) check', min_length=10, points=1)

    tests.extend([test1a, test2a, test3a, test3b, test3c, test3d, test4a, ])
    return tests

