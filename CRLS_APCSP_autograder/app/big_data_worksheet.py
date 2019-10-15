def docs_feedback_big_data_worksheet(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)
    test1a = exact_answer('1a. 5 years?', [r'1a .+? tabledata \s* 5\.7 .+? 1b\.'], text, points=5)
    test1b = exact_answer('1b. 15 years?', [r'1b .+? tabledata \s* 190 .+? 1c\.'], text, points=1)
    test1c = keyword_and_length('1c. Show work', [r'[a-zA-Z]+'], text,
                                search_string=r'1c\. .+? tabledata (.+?) 1d\.', min_length=7, points=1)
    test1d = keyword_and_length('1d. Moores law', [r'[a-zA-Z]+'], text,
                                search_string=r'1d\. .+? tabledata (.+?) code', min_length=10, points=1)
    test2a = keyword_and_length('2a. 3 sources of data', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+?) 3a\.', min_length=7, points=1)
    test3a = keyword_and_length('3a. 3Vs', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 4a\.', min_length=10, points=1)
    test4a = keyword_and_length('4a. Big data good?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) 4b\.', min_length=10, points=1)
    test4b = keyword_and_length('4b. Big data bad', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) heck', min_length=10, points=1)
    tests.extend([test1a, test1b, test1c, test1d, test2a, test3a, test4a, test4b,])
    return tests
