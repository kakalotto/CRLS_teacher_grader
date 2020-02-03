def docs_feedback_bytes_and_file_sizes_v3(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1a = exact_answer('1a. KB', [r'1a\. .*? tabledata .*? 1 [\s,]* 000  .*?  1b\. ',
                                     r'1a\. .*? tabledata .*? 1e3  .*?  1b\. ',],text, points=2)
    test1b = exact_answer('1b. MB', [r'1b\. .*? tabledata .*? 1 [\s,]* 000 [\s,]* 000  .*?  1c\. ',
                                     r'1b\. .*? tabledata .*? 1e6  .*?  1c\. ',],text, points=2)
    test1c = exact_answer('1c. GB', [r'1c\. .*? tabledata .*? 1 [\s,]* 000 [\s,]* 000 [\s,]* 000 .*?  1d\. ',
                                     r'1c\. .*? tabledata .*? 1e9  .*?  1d\. ',],text, points=2)
    test1d = exact_answer('1d. TB', [r'1d\. .*? tabledata .*? 1 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000 .*?  1e\. ',
                                     r'1d\. .*? tabledata .*? 1e12  .*?  1e\. ',],text, points=2)
    test1e = exact_answer('1e. PB', [r'1e\. .*? tabledata .*? 1 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000 .*?  1f\. ',
                                     r'1e\. .*? tabledata .*? 1e15  .*?  1f\. ',],text, points=2)
    test1f = exact_answer('1f. EB', [r'1f\. .*? tabledata .*? 1 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000.*?  in \s the \s real ',
                                     r'1f\. .*? tabledata .*? 1e18  .*?  in \s the \s real ',],text, points=2)
    test2a = keyword_and_length('2a. jpg size dimensions', [r'[0-9]'], text, search_string=r'2a\. .*? tabledata (.+?) 2b\.', min_length=1, points=0.5)
    test2c = keyword_and_length('2c. animated gif size dimensions', [r'[0-9]'], text, search_string=r'2c\. .*? tabledata (.+?) 2d\.',
                                min_length=1, points=0.5)
    test2e = keyword_and_length('2e. PDF size #', [r'[0-9]'], text,
                                search_string=r'2e\. .*? tabledata (.+?) 2f\.', min_length=1, points=0.5)
    test2g = keyword_and_length('2g. audio size #', [r'[0-9]'], text,
                                search_string=r'2g\. .*? tabledata (.+?) 2h\.', min_length=1, points=0.5)
    test2i = keyword_and_length('2i. video size #', [r'[0-9]'], text,
                            search_string=r'2i\. .*? tabledata (.+?) 2j\.', min_length=1, points=0.5)
    test2b = keyword_and_length('2b. jpg size (requires units)', [r'[0-9] .*? B'], text,
                                search_string=r'2b\. .*? tabledata (.+?) 2c\.', min_length=1, points=0.5)
    test2d = keyword_and_length('2d. animated gif file size (requires units)', [r'[0-9] .*? B'], text,
                                search_string=r'2d\. .*? tabledata (.+?) 2e\.', min_length=1, points=0.5)
    test2f = keyword_and_length('2f. PDF file size (requires units)', [r'[0-9] .*? B'], text,
                                search_string=r'2f\. .*? tabledata (.+?) 2g\.', min_length=1, points=0.5)
    test2h = keyword_and_length('2h. audio file size (requires units)', [r'[0-9] .*? B'], text,
                                search_string=r'2h\. .*? tabledata (.+?) 2i\.', min_length=1, points=0.5)
    test2j = keyword_and_length('2j. video file size (requires units)', [r'[0-9] .*? B'], text,
                                search_string=r'2j\. .*? tabledata (.+?) test \s your \s', min_length=1, points=0.5)
    test3a = exact_answer('3a. Fits on drive?', [r'3a\. .+? tabledata .*? yes .*? 3b\.'], text, points=1)
    test3b = keyword_and_length('3b. Show work for 3a', [r'[0-9]'], text,
                                search_string=r'3b\. .*? tabledata (.+?) 4a\.', min_length=1, points=1)
    test4a = exact_answer('4a. How much space?', [r'4a\. .*? tabledata .*?  52\.5 .+? 4b\. '],
                           text, points=1)
    test4b = keyword_and_length('4b. Show work for 4a', [r'[0-9]'], text,
                                search_string=r'4b\. .*? tabledata (.+?) 5a\.', min_length=1, points=1)
    test5a = exact_answer('5a. Enough?', [r'5a\. .*? tabledata .*?  not .+? 5b\. '],
                          text, points=1)
    test5b = keyword_and_length('5b. Show work for 5a', [r'[0-9]'], text,
                                search_string=r'5b\. .*? tabledata (.+?) 6a\.', min_length=1, points=1)
    test6a = exact_answer('6a. shakespeare or video??', [r'6a\. .*? tabledata .*?  video .*? 6b\. '],
                           text, points=1)
    test6b = keyword_and_length('6b. Show work for 6a', [r'[0-9]'], text,
                                search_string=r'6b\. .*? tabledata (.+?) 7a\.', min_length=1, points=1)
    test7a = exact_answer('7a. Ohio facetube??', [r'7a\. .*? tabledata .*? 324 .*? 7b\. '],
                           text, points=1)
    test7b = keyword_and_length('7b. Show work for 7a', [r'[0-9]'], text,
                                search_string=r'7b\. .*? tabledata (.+?) question \s ', min_length=1, points=1)

    tests.extend([test1a, test1b, test1c, test1d, test1e, test1f, test2a, test2b, test2c, test2d, test2e, test2f,
                  test2g, test2h, test2i, test2j, test3a, test3b, test4a, test4b, test5a, test5b, test6a, test6b,
                  test7a, test7b])

    return tests
