def docs_feedback_lossless_compression(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1a = exact_answer('1a. song name', [r'\s1a\. .+? tabledata \s [a-zA-Z\.0-9] .+? 2a\.'], text, points=5)
    test2a = keyword_and_length('2a. Copy+paste compressed song', [r'[a-zA-Z]'], text,
                                search_string=r'2a\. .*? tabledata (.+?) 3a\.', min_length=1, points=1)
    test3a = keyword_and_length('3a. Copy+paste dictionary', [r'[a-zA-Z]'], text,
                                search_string=r'3a\. .*? tabledata (.+?) 4a\.', min_length=1, points=1)
    test4a = keyword_and_length('4a. Copy+paste stats', [r'[a-zA-Z]'], text,
                                search_string=r'4a\. .*? tabledata (.+?) 5a\.', min_length=20, points=1)
    test5a = keyword_and_length('5a. What made compression hard', [r'[a-zA-Z]'], text,
                                search_string=r'5a\. .*? tabledata (.+?) 6a\.', min_length=10, points=1)
    test6a = keyword_and_length('6a. Describe thinking process', [r'[a-zA-Z]'], text,
                                search_string=r'6a\. .*? tabledata (.+?) 7a\.', min_length=10, points=1)
    test7a = keyword_and_length('7a. Possible to write instructions always better than heuristic?', [r'[a-zA-Z]'], text,
                                search_string=r'7a\. .*? tabledata (.+?) 8a\.', min_length=10, points=1)
    test8a = keyword_and_length('8a. Possible to know most compressed?', [r'[a-zA-Z]'], text,
                                search_string=r'8a\. .*? tabledata (.+?) 9a\.', min_length=8, points=1)
    test9a = keyword_and_length('9a. Can your friend read compressed? Dictionary?', [r'[a-zA-Z]'], text,
                                search_string=r'9a\. .*? tabledata (.+?) check \s your \s work', min_length=10, points=1)

    tests.extend([test1a, test2a, test3a, test4a, test5a, test6a, test7a, test8a, test9a])
    return tests
