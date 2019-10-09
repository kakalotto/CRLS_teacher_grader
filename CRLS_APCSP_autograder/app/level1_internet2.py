def docs_feedback_level1_internet_2(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    print(text)
    test1a = keyword_and_length('1a. What is an IP address', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 1b\.', min_length=5, points=1)
    test1b = exact_answer('1b. IP address of your machine?', [r'1b\. .+? tabledata .+? 172\.25\.233  .+? 1c\.'], text, points=5)
    test1c = exact_answer('1c. DNS servers of your machine?', [r'1c\. .+? tabledata .+? 172\.25\.234\.7 .+?  1d\.',
                                                               r'1c\. .+? tabledata .+? 172\.25\.234\.8 .+? 1d\.'],
                          text, points=5)
    test1d = exact_answer('1d. Router (gateway) of your machine?',
                          [r'1d\. .+? tabledata .+? 172\.25\.233\.1  .+? 1e\.'],
                          text, points=5)
    test1e = exact_answer('1e. DHCP server of your machine?', [r'1e\. .+? tabledata .+? 172\.25\.234\.7  .+? etwork'],
                          text, points=5)
    test2a = exact_answer('2a. Ping a partner.', [r'2a\. .+? tabledata .+? 172\.25\.233 .+? 2b\.',
                                                  r'2a\. .+? tabledata .+? [pP]inging .+? 2b\.',
                                                  r'2a\. .+? tabledata .+? [rR]eply .+? 2b\.'],
                          text, points=5, required=3)
    test2b = exact_answer('2b. Ping Amazon Japan.', [r'2b\. .+? tabledata .+? amazon\.co\.jp .+? 2c\.',
                                                     r'2b\. .+? tabledata .+? [pP]inging .+? 2c\.',
                                                     r'2b\. .+? tabledata .+? [rR]eply .+? 2c\.'],
                          text, points=5, required=2)
    test2c = exact_answer('2c. Ping nonexistent or down machine.',
                          [r'2c\. .+? tabledata .+? [pP]inging .+? nslookup',
                           r'2c\. .+? tabledata .+? timed \s out .+? nslookup',],
                          text, points=5, required=2)
    test3a = exact_answer('3a. nslookup.',
                          [r'3a\. .+? tabledata .+? [sS]erver .+? 3b\.',
                           r'3a\. .+? tabledata .+? [nN]ame .+? 3b\.', ],
                          text, points=5, required=2)
    test3b = keyword_and_length('3b. What does nslookup mean', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) tracert', min_length=5, points=1)
    test4a = exact_answer('4a. tracert',
                          [r'4a\. .+? tabledata .+? [hH]ops .+? 4b\.',
                           r'4a\. .+? tabledata .+? ms .+? 4b\.',
                           r'4a\. .+? tabledata .+? [tT]racing .+? 4b\.',
                           ],
                          text, points=5, required=3)

    test4b = keyword_and_length('4b. Explain tracert ', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) work', min_length=10, points=1)

    tests.extend([test1a, test1b, test1c, test1d, test1e, test2a, test2b, test2c, test3a, test3b, test4a, test4b,])
    return tests
