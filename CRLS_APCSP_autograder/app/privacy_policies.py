def docs_feedback_privacy_policies(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    # print(text)
    test_website = keyword_and_length('Website?', [r'.+'], text,
                                      search_string=r'our\swebsite\: .+? tabledata (.+?) hat', min_length=1, points=1)
    test1a = keyword_and_length('question 1a', [r'[a-zA-Z]+'], text,
                                search_string=r'1a. .+? tabledata (.+) 1b', min_length=4, points=1)
    test1b = keyword_and_length('question 1b', [r'[a-zA-Z]+'], text,
                                search_string=r'1b. .+? tabledata (.+) 2a', min_length=4, points=1)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 2b', min_length=4, points=1)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b. .+? tabledata (.+) 3a', min_length=4, points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 3b', min_length=4, points=1)
    test3b = keyword_and_length('question 3b', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .+? tabledata (.+) 4a', min_length=4, points=1)
    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]+'], text,
                                search_string=r'4a. .+? tabledata (.+) 4b', min_length=4, points=1)
    test4b = keyword_and_length('question 4b', [r'[a-zA-Z]+'], text,
                                search_string=r'4b. .+? tabledata (.+) 5a', min_length=4, points=1)
    test5a = keyword_and_length('question 5a', [r'[0-4]+'], text,
                                search_string=r'5a. .+? tabledata  (.+?) tabledata ', min_length=1, points=1)
    test5b = keyword_and_length('question 5b', [r'[a-zA-Z]+'], text,
                                search_string=r'5b. .+? tabledata (.+?) erify', min_length=10, points=1)
    tests.extend([test_website, test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b, test5a, test5b])

    return tests