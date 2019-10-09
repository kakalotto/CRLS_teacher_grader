def docs_feedback_hardware_power(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Power/server?', [r'1a\. .+? tabledata .*? 360 \s* [wW] .*?   1b\.', ], text, points=5)
    test1b = keyword_and_length('1b. Show work for 1a.', [r'[0-9a-zA-Z]+'], text,
                                search_string=r'1b\. .+? tabledata (.+?) 1c\.', min_length=1, points=1)
    test1c = exact_answer('1c. 3A/server, how many?', [r'1c\. .+? tabledata .*? 6 .*? 1d\.'], text, points=5)
    test1d = keyword_and_length('1d. Show work for 1c.', [r'[0-9a-zA-Z]+'], text,
                                search_string=r'1d\. .+? tabledata (.+?) 1e\.', min_length=1, points=1)
    test1e = exact_answer('1e. 3A/server with 30% fluctuations, how many?',
                          [r'1e\. .+? tabledata .*? 5 .*? 1f\.'], text, points=5)
    test1f = keyword_and_length('1f. Show work for 1e.', [r'[0-9a-zA-Z]+'], text,
                                search_string=r'1f\. .+? tabledata (.+?) 1g\.', min_length=1, points=1)
    test1g = exact_answer('1g. 1000 KW power, 3A/server, how many?',
                          [r'1g\. .+? tabledata .*? 2136 .*? 1h\.'], text, points=5)
    test1h = keyword_and_length('1h. Show work for 1g.', [r'[0-9a-zA-Z]+'], text,
                                search_string=r'1h\. .+? tabledata (.+?) ower.', min_length=1, points=1)
    test2a = exact_answer('2a. CPU power?', [r'2a\. .+? tabledata .*? aaa \s inlineobject .*? 2b\.'],text, points=1,)
    test2b = exact_answer('2b. slimsata power?', [r'2b\. .+? tabledata .*? aaa \s inlineobject .*? 2c\.'],
                          text, points=1,)
    test2c = exact_answer('2c. motherboard power?', [r'2c\. .+? tabledata .*? aaa \s inlineobject .*? 2d\.'],
                          text, points=1, )
    test2d = exact_answer('2d. SATA power?', [r'2d\. .+? tabledata .*? aaa \s inlineobject .*? stalling'],
                          text, points=1, )
    test3a = exact_answer('3a. Power supply watts?', [r'3a\. .+? tabledata .*? 235 \s* [wW] .*? 3b\.'],
                          text, points=5, )

    tests.extend(
        [test1a, test1b, test1c, test1d, test1e, test1f, test1g, test1h, test2a, test2b, test2c, test2d, test3a, ])
    return tests