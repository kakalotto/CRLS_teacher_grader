def docs_feedback_binary_practice_v4(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test1a = exact_answer('1a. 3', [r'1a\. .*? tabledata .*? 0011 .*? tabledata \s 3 \n '], text, points=2)
    test1b = exact_answer('1b. 4', [r'1b\. .*? tabledata .*? 0100 .*? tabledata \s 4 \n'], text, points=2)
    test1c = exact_answer('1c. 5', [r'1c\. .*? tabledata .*? 0101 .*? tabledata \s 5 \n '], text, points=2)
    test1d = exact_answer('1d. 6', [r'1d\. .*? tabledata .*? 0110 .*? tabledata \s 6 \n'], text, points=2)
    test1e = exact_answer('1e. 7' , [r'1e\. .*? tabledata .*? 0111 .*? tabledata \s 7 \n'], text, points=2)
    test1f = exact_answer('1f. 8', [r'1f\. .*? tabledata .*? 1000 .*? tabledata \s 8 \n'], text, points=2)
    test1g = exact_answer('1g. 9', [r'1g\. .*? tabledata .*? 1001 .*? tabledata \s 9 \n '], text, points=2)
    test1h = exact_answer('1h. 10', [r'1h\. .*? tabledata .*? 1010 .*? tabledata \s 10 \n'], text, points=2)
    test1i = exact_answer('1i. 11', [r'1i\. .*? tabledata .*? 1011 .*? tabledata \s 11 \n'], text, points=2)
    test1j = exact_answer('1j. 12', [r'1j\. .*? tabledata .*? 1100 .*? tabledata \s 12 \n'], text, points=2)
    test1k = exact_answer('1k. 13', [r'1k\. .*? tabledata .*? 1101 .*? tabledata \s 13 \n'], text, points=2)
    test1l = exact_answer('1l. 14', [r'1l\. .*? tabledata .*? 1110 .*? tabledata \s 14 \n'], text, points=2)
    test1m = exact_answer('1m. 15', [r'1m\. .*? tabledata .*? 1111 .*? tabledata \s 15 \n'], text, points=2)
    test2a = exact_answer('2a. 0000 0100 ', [r'2a\. .*? tabledata .*? 4 .*? 2e\.'], text, points=2)
    test2b = exact_answer('2b. 0000 1000 ', [r'2b\. .*? tabledata .*? 8 .*? 2f\.'], text, points=2)
    test2c = exact_answer('2c. 0001 0000', [r'2c\. .*? tabledata  .*? 16 .*? 2'], text, points=2)
    test2d = exact_answer('2d. 0010 0000', [r'2d\. .*? tabledata .*? 32 .*? 2a\.'], text, points=2)
    test2e = exact_answer('2e. 0100 0000', [r'2e\. .*? tabledata .*? 64 .*? 2b\.'], text, points=2)
    test2f = exact_answer('2f. 1000 0000', [r'2f\. .*? tabledata .*? 128 .*? conversion \s practice'], text, points=2)
    test3a = exact_answer('3a. 100', [r'3a\. .*? tabledata .*? 4 .*? 3h\.'], text, points=2)
    test3b = exact_answer('3b. 111', [r'3b\. .*? tabledata .*? 7 .*? 3i\.'], text, points=2)
    test3c = exact_answer('3c. 1101',[r'3c\. .*? tabledata .*? 13 .*? 3j\.'], text, points=2)
    test3d = exact_answer('3d. 0011 1111', [r'3d\. .*? tabledata .*? 63 .*? 3k\.'], text, points=2)
    test3e = exact_answer('3e. 0100 0000', [r'3e\. .*? tabledata .*? 64 .*? 3l\.'],text, points=2)
    test3f = exact_answer('3f. 1010 1010', [r'3f\. .*? tabledata .*? 170 .*? 3m\.'], text, points=2)
    test3g = exact_answer('3g. 1111 1111', [r'3g\. .*? tabledata .*? 255 .*? 3n\.'], text, points=2)
    test3h = exact_answer('3h. 5', [r'3h\. .*? tabledata .*? 101 .*? 3b\.'], text, points=2)
    test3i = exact_answer('3i. 17', [r'3i\. .*? tabledata .*? 1 \s* 0001 .*? 3c\.'], text, points=2)
    test3j = exact_answer('3j. 63', [r'3j\. .*? tabledata .*? 11 \s* 1111 .*? 63'], text, points=2)
    test3k = exact_answer('3k. 128', [r'3k\. .*? tabledata .*? 1000 \s* 0000 .*? 3e\.'], text, points=2)
    test3l = exact_answer('3l. 127', [r'3l\. .*? tabledata .*? 111 \s* 1111 .*? 3f\.'], text, points=2)
    test3m = exact_answer('3m. 256', [r'3m\. .*? tabledata .*? 1 \s* 0000 \s* 0000 .*? 3g\.'], text, points=2)
    test3n = exact_answer('3n. 514', [r'3n\. .*? tabledata .*? 10 \s* 0000 \s* 0010 .*? note: \s a \s short'], text, points=2)
    test4a = keyword_and_length('4a. How to tell if odd?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .*? tabledata (.+?) 5a\.', min_length=10, points=1)
    test5a = exact_answer('5a. How many bits to count to 2000', [r'5a\. .*? tabledata .*? 11 .*? 5b\.'], text, points=1)
    test5b = keyword_and_length('5b. Explain 5a', [r'.+'], text,
                                search_string=r'5b. .*? tabledata (.+?) 6a\. ', min_length=7, points=1)
    test6a = exact_answer('6a. How high can homer count', [r'6a\. .*? tabledata .*? 255 .*? 6b\.'], text, points=1)
    test6b = keyword_and_length('6b. Explain 6a', [r'.+'], text,
                                search_string=r'6b. .*? tabledata (.+?) inline', min_length=7, points=1)
    tests.extend([test1a, test1b, test1c, test1d, test1e, test1f, test1g, test1h, test1i, test1j, test1k, test1l,
                  test1m, test2a, test2b, test2c, test2d, test2e, test2f, test3a, test3b, test3c, test3d, test3e,
                  test3f, test3g, test3h, test3i, test3j, test3k, test3l, test3m, test3n, test4a, test5a, test5b,
                  test6a, test6b])

    return tests
