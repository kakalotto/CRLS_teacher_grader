def docs_feedback_internet_2_v2(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. packets guaranteed?', [r'1a\. .+? tabledata \s* no \s*  1b\.'], text, points=5)
    test1b = exact_answer('1b. protocol name?', [r'1b\. .+? tabledata \s* tcp \s*  1c\.'], text, points=5)
    test1c = keyword_and_length('1c. explain', [r'[a-zA-Z]+'], text,
                                search_string=r'1c\. .+? tabledata (.+) scalin', min_length=10, points=1)
    test2a = keyword_and_length('2a. DNS again', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+) 2b\.', min_length=7, points=1)
    test2b = keyword_and_length('2b. IP again', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+) 2c\.', min_length=7, points=1)
    test2c = keyword_and_length('2c. Hierarchy in DNS/IP and scaling', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+) 2d\.', min_length=10, points=1)
    test2d = keyword_and_length('2d. Fault-tolerant routing and scaling', [r'[a-zA-Z]+'], text,
                                search_string=r'2d\. .+? tabledata (.+) 2e\.', min_length=10, points=1)
    test2e = keyword_and_length('2e. Protocols and scaling', [r'[a-zA-Z]+'], text,
                                search_string=r'2e\. .+? tabledata (.+) 2f\.', min_length=10, points=1)
    test2f = keyword_and_length('2f. Protocols and scaling', [r'[a-zA-Z]+'], text,
                                search_string=r'2f\. .+? tabledata (.+?) latency', min_length=7, points=1)
    test3a = keyword_and_length('3a. Bandwidth vs. Latency', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) internet', min_length=10, points=1)
    test4a = keyword_and_length('4a. Cookie', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+)  4b\.', min_length=10, points=1)
    test4b = keyword_and_length('4b. Cookie good?', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+)  4c\.', min_length=10, points=1)
    test4c = keyword_and_length('4c. Cookie good?', [r'[a-zA-Z]+'], text,
                                search_string=r'4c\. .+? tabledata (.+?)  internet', min_length=10, points=1)
    test5a = keyword_and_length('5a. What going on?', [r'[a-zA-Z]+'], text,
                               search_string=r'5a\. .+? tabledata (.+)  5b\.', min_length=10, points=1)
    test5b = exact_answer('5b. Min number?', [r'5b\. .+? tabledata \s* 2 \s*  5c\.'], text, points=5)
    test5c = exact_answer('5b. Max number??', [r'5c\. .+? tabledata \s* 8 \s*  .+? $'], text, points=5)
    tests.extend([test1a, test1b, test1c, test2a, test2b, test2c, test2d, test2e, test2f, test3a, test4a, test4b,
                  test4c, test5a, test5b, test5c, ])
    return tests

