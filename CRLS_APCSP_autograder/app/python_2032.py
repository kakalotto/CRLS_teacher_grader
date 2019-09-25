def docs_feedback_python_2032(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)

    test1a = exact_answer('1a ', [r'1a\. .+? tabledata \s* (true|false) .+? 1b\.'], text, points=0.5)
    test1b = exact_answer('1b ', [r'1b\. .+? tabledata \s* true \s* tabledata .+? 2a\.'], text, points=0.5)
    test2a = exact_answer('2a ', [r'2a\. .+? tabledata \s* (true|false) .+? 2b\.'], text, points=0.5)
    test2b = exact_answer('1b ', [r'2b\. .+? tabledata \s* false \s* tabledata .+? 3a\.'], text, points=0.5)
    test3a = exact_answer('3a ', [r'3a\. .+? tabledata \s* (true|false) .+? 3b\.'], text, points=0.5)
    test3b = exact_answer('3b ', [r'3b\. .+? tabledata \s* true \s* tabledata .+? 4a\.'], text, points=0.5)
    test4a = exact_answer('4a ', [r'4a\. .+? tabledata \s* (true|false) .+? 4b\.'], text, points=0.5)
    test4b = exact_answer('4b ', [r'4b\. .+? tabledata \s* false \s* .+? check'], text, points=0.5)
    test5a = exact_answer('5a ', [r'5a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test6a = exact_answer('6a ', [r'6a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test7a = exact_answer('7a ', [r'7a\. .+? tabledata \s* true \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test8a = exact_answer('8a ', [r'8a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test9a = exact_answer('9a ', [r'9a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test10a = exact_answer('10a ', [r'10a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test11a = exact_answer('11a ', [r'11a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test12a = exact_answer('12a ', [r'12a\. .+? tabledata \s* false \s* .+?  program'], text, points=0.5)
    test13a = exact_answer('13a ', [r'13a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 13b\.'], text, points=0.1)
    test14a = exact_answer('14a ', [r'14a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 14b\.'], text, points=0.1)
    test15a = exact_answer('15a ', [r'15a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 15b\.'], text, points=0.1)
    test16a = exact_answer('16a ', [r'16a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 16b\.'], text, points=0.1)
    test17a = exact_answer('17a ', [r'17a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 17b\.'], text, points=0.1)
    test18a = exact_answer('18a ', [r'18a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 18b\.'], text, points=0.1)
    test19a = exact_answer('19a ', [r'19a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 19b\.'], text, points=0.1)
    test20a = exact_answer('20a ', [r'20a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 20b\.'], text, points=0.1)
    test13b = exact_answer('13b ', [r'13b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 13c\.'], text, points=0.1)
    test14b = exact_answer('14b ', [r'14b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 14c\.'], text, points=0.1)
    test15b = exact_answer('15b ', [r'15b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 15c\.'], text, points=0.1)
    test16b = exact_answer('16b ', [r'16b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 16c\.'], text, points=0.1)
    test17b = exact_answer('17b ', [r'17b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 17c\.'], text, points=0.1)
    test18b = exact_answer('18b ', [r'18b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 18c\.'], text, points=0.1)
    test19b = exact_answer('19b ', [r'19b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 19c\.'], text, points=0.1)
    test20b = exact_answer('20b ', [r'20b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 20c\.'], text, points=0.1)
    test13c = exact_answer('13c ', [r'13c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 14a\.'], text, points=0.3)
    test14c = exact_answer('14c ', [r'14c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 15a\.'], text, points=0.3)
    test15c = exact_answer('15c ', [r'15c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 16a\.'], text,
                           points=0.3)
    test16c = exact_answer('16c ', [r'16c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 17a\.'], text,
                           points=0.3)
    test17c = exact_answer('17c ', [r'17c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 18a\.'], text,
                           points=0.3)
    test18c = exact_answer('18c ', [r'18c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 19a\.'], text,
                           points=0.3)
    test19c = exact_answer('19c ', [r'19c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 20a\.'], text,
                           points=0.3)
    test20c = exact_answer('20c ', [r'20c\. .+? tabledata \s* (true|false) \s* .+? $'], text,
                           points=0.3)

    tests.extend([test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b, test5a, test6a, test7a, test8a,
                  test9a, test10a, test11a, test12a, test13a, test13b, test13c, test14a, test14b, test14c, test15a,
                  test15b, test15c, test16a, test16b, test16c, test17a, test17b, test17c, test18a, test18b, test18c,
                  test19a, test19b, test19c, test20a, test20b,test20c])
    return tests

