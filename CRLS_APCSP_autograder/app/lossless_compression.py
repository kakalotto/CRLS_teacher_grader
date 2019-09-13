def docs_feedback_lossless_compression(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test1a = exact_answer('question 1a song name', [r'\s1a\. .+? tabledata \s [a-zA-Z\.0-9] .+? 2a\.'], text, points=5)
    test2a = exact_answer('question 2a screenshot compressed txt',
                          [r'\s2a\. .+? tabledata \s aaa \s inlineobject .+? 3a\.'], text, points=1)
    test3a = exact_answer('question 3a screenshot dictionary',
                          [r'\s3a\. .+? tabledata \s aaa \s inlineobject .+? 4a\.'], text, points=1)
    test4a = exact_answer('question 4a  stats',
                          [r'\s4a\. .+? tabledata \s aaa \s inlineobject .+? 5a\.'], text, points=1)
    test5a = keyword_and_length('question 5a', [r'[a-zA-Z]'], text,
                                search_string=r'\s5a\. .+? tabledata (.+) 6a\.', min_length=10, points=1)
    test6a = keyword_and_length('question 6a', [r'[a-zA-Z]'], text,
                                search_string=r'\s6a\. .+? tabledata (.+) 7a\.', min_length=15, points=1)
    test7a = keyword_and_length('question 7a', [r'[a-zA-Z]'], text,
                                search_string=r'\s7a\. .+? tabledata (.+) 8a\.', min_length=10, points=1)
    test8a = keyword_and_length('question 8a', [r'[a-zA-Z]'], text,
                                search_string=r'\s8a\. .+? tabledata (.+) 9a\.', min_length=8, points=1)
    test9a = keyword_and_length('question 9a', [r'[a-zA-Z]'], text,
                                search_string=r'\s9a\. .+? tabledata (.+) check', min_length=10, points=1)
    tests.extend([test1a, test2a, test3a, test4a, test5a, test6a, test7a, test8a, test9a])
    return tests