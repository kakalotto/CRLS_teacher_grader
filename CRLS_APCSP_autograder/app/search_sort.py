def docs_feedback_search_sort(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)


    test1a = keyword_and_length('1a. Good algorithm?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+) 2a\.', min_length=10, points=1)
    test2a = keyword_and_length('2a. Efficiency of merge vs. bubble, small sets??', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+) 2b\.', min_length=7, points=1)
    test2b = keyword_and_length('2b. Efficiency of merge vs. bubble, large sets??', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+) 3a\.', min_length=7, points=1)
    test3a = exact_answer('3a. binary always faster?',
                          [r'3a\. .+? tabledata \s* no \s*  3b\.'], text, points=1)
    test3b = keyword_and_length('3b. Explain 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+) 3c\.', min_length=7, points=1)
    test3c = exact_answer('3c. Before binary search must?',
                          [r'3c\. .+? tabledata .+? sort .+?  3d\.'], text, points=3)
    test3d = exact_answer('3d. Must sort for linear search?',
                          [r'3a\. .+? tabledata \s* no \s*  3b\.'], text, points=3)
    test4a = keyword_and_length('4a. Put numbers on it', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+) 5a\.', min_length=12, points=1)
    test5a = keyword_and_length('5a. Why sort?', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+) 6a\.', min_length=10, points=1)
    test6a = keyword_and_length('6a. Example of time want to sort?', [r'[a-zA-Z]+'], text,
                                search_string=r'6a\. .+? tabledata (.+) 7a\.', min_length=10, points=1)
    test7a = exact_answer('7a. n^2 reasonable?',
                          [r'7a\. .+? tabledata .+? yes .+?  7b\.'], text, points=5)
    test7b = exact_answer('7b. n! reasonable?',
                          [r'7b\. .+? tabledata .+? no .+?  in \s the \s real'], text, points=5)

    tests.extend([test1a, test2a, test2b, test3a, test3b, test3c, test3d, test4a, test5a, test6a, test7a,
                  test7b])

    return tests

