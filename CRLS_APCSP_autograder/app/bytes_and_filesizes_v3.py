def docs_feedback_bytes_and_file_sizes_v3(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1a = exact_answer('question 1a KB', [r'1a\. .+? tabledata \s* 1 [\s,]* 000 [^0] '
                                             r'[Bb]* y* t* e* s* \s*tabledata \s 2a\.'],
                          text, points=2)
    test2a = exact_answer('question 2a MB', [r'2a\. .+? tabledata \s* 1 [\s,]* 000 [\s,]* 000 [^0] '
                                             r'[Bb]* y* t* e* s* \s* tabledata \s 3a\.'],
                          text, points=2)
    test3a = exact_answer('question 3a GB', [r'3a\. .+? tabledata \s* 1 [\s,]* 000 [\s,]*'
                                             r' 000[\s,]* 000 [^0] '
                                             r'[Bb]* y* t* e* s* \s* tabledata \s 4a\.'],
                          text, points=2)
    test4a = exact_answer('question 4a TB',
                          [r'4a\. .+? tabledata \s* 1 [\s,]* [\s,]* 000[\s,]* 000[\s,]* '
                           r'000 [\s,]* 000[^0] [Bb]* y* t* e* s* \s* tabledata \s 5a\.'],
                          text, points=2)
    test5a = exact_answer('question 5a PB',
                          [r'5a\. .+? tabledata \s* 1 [\s,]* 000 [\s,]* 000[\s,]* 000[\s,]* '
                           r'000[\s,]* 000 [^0] [Bb]* y* t* e* s* \s* tabledata \s 6a\.'],
                          text, points=2)
    test6a = exact_answer('question 6a EB',
                          [r'6a\. .+? tabledata \s* 1 [\s,]* 000 [\s,]* 000[\s,]* 000[\s,]* '
                           r'000[\s,]* 000[\s,]* 000 [^0] [Bb]* y* t* e* s* \s* \s* in \s the'],
                          text, points=2)
    test8a = exact_answer('question 8a jpg size', [r'8a\. .+? tabledata \s*  [\sa-zA-Z0-9]+ \n tabledata \s 8b\. '],
                          text, points=0.5)
    test8b = exact_answer('question 8b jpg filesize',
                          [r'8b\. .+? tabledata \s  [a-zA-Z0-9]+ .+? tabledata .+? tabledata \s 9a\. '],
                          text, points=0.5)
    test9a = exact_answer('question 9a gif size', [r'9a\. .+? tabledata \s*  [\sa-zA-Z0-9]+ \n tabledata \s 9b\. '],
                          text, points=0.5)
    test9b = exact_answer('question 9b gif filesize',
                          [r'9b\. .+? tabledata \s  [a-zA-Z0-9]+ .+? tabledata .+? tabledata \s 10a\.'],
                          text, points=0.5)
    test10a = exact_answer('question 10a pdf size', [r'10a\. .+? tabledata \s*  [\sa-zA-Z0-9]+ \n tabledata \s 10b\. '],
                           text, points=0.5)
    test10b = exact_answer('question 9b pdf filesize',
                           [r'10b\. .+? tabledata \s  [a-zA-Z0-9]+ .+? tabledata .+? tabledata \s 11a\.'],
                           text, points=0.5)
    test11a = exact_answer('question 11a audio size',
                           [r'11a\. .+? tabledata \s*  [\s,:\.a-zA-Z0-9]+ \n tabledata \s 11b\. '],
                           text, points=0.5)
    test11b = exact_answer('question 11b audio filesize',
                           [r'11b\. .+? tabledata \s  [a-zA-Z0-9]+ .+? tabledata .+? tabledata \s 12a\. '],
                           text, points=0.5)
    test12a = exact_answer('question 12a video size',
                           [r'12a\. .+? tabledata \s*  [\s,:\.a-zA-Z0-9]+ \n tabledata \s 12b\. '],
                           text, points=0.5)
    test12b = exact_answer('question 12b video filesize',
                           [r'12b\. .+? tabledata \s  [a-zA-Z0-9]+ .+?test'],
                           text, points=0.5)
    test13a = exact_answer('13a. Fits on drive?', [r'13a\. .+? tabledata \s  no .+? 13b\. '],
                           text, points=1)
    test13b = exact_answer('13b. Checkoff', [r'13b\. .+? tabledata \s* [\*=a-zA-Z0-9]+ .+? 14a\.'],
                           text, points=1)
    test14a = exact_answer('14a. Fits on drive?', [r'14a\. .+? tabledata \s  52\.5 .+? 14b\. '],
                           text, points=1)
    #    test14b = exact_answer('14b. Checkoff', [r'14b\. .+? tabledata \s*  [\*=a-zA-Z0-9]+ .+? 15a\.'],
    #                           text, points=1)
    test15a = exact_answer('15a. Enough or not?', [r'15a\. .+? tabledata \s  not .+? 15b\. '],
                           text, points=1)
    #    test15b = exact_answer('15b. Checkoff', [r'15b\. .+? tabledata \s*  [\*=a-zA-Z0-9]+ .+? 16a\.'],
    #                           text, points=1)
    test16a = exact_answer('16a. shakespeare or video??', [r'16a\. .+? tabledata \s  video .+? 16b\. '],
                           text, points=1)
    #    test16b = exact_answer('16b. Checkoff', [r'16b\. .+? tabledata \s*  [\*=a-zA-Z0-9]+ .+? 17a\.'],
    #                           text, points=1)
    test17a = exact_answer('17a. Ohio facetube??', [r'17a\. .+? tabledata \s  324 .+? 17b\. '],
                           text, points=1)
    test17b = exact_answer('17b. Checkoff', [r'17b\. .+? tabledata \s*  [\*=a-zA-Z0-9]+ .+? Question'],
                           text, points=1)
    tests.extend([test1a, test2a, test3a, test4a, test5a, test6a, test8a, test8b, test9a, test9b, test10a, test10b,
                  test11a, test11b, test12a, test12b, test13a, test13b, test14a, test15a, test16a,
                  test17a, ])
    return tests
