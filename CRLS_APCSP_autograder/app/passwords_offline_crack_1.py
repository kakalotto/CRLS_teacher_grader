def docs_feedback_passwords_offline_crack_1(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)

    print(text)

    test1a = exact_answer('1a. Screenshot of accounts',
                          [r'1a\. .+? tabledata \s* aaa \s* inlineobject .+?  2a\.'], text, points=1)
    test2a = exact_answer('2a. Copy+paste hash file dump', [r'2a\. .+? tabledata .*?  NO \s PASSWORD .*? 2b\.',
                                                            r'2a\. .+? tabledata .*? ADMINISTRATOR .*? 2b\.',
                                                            r'2a\. .+? tabledata .*? 500 .*? 2b\.',
                                                            r'2a\. .+? tabledata .*? :.+?:.+?:.+?:.+?:.+?: .*? 2b\.', ]
                          , text, points=10, required=4)
    test2b = exact_answer('2b. Dump hash file as non-admin?', [r'2b\. .+? tabledata .+? (no|No|NO) .+? 2c\.'],
                          text, points=5)
    test2c = keyword_and_length('2c. Why?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) 3a\.', min_length=7, points=1)
    test3a = exact_answer('3a. Copy+paste word list file?', [r'3a\. .+? tabledata .+? q \n w \n e \n r \n t \n y \n'
                                                             r'u \n i \n o \n p .+? 4a\.'],
                          text, points=20)
    test4a = exact_answer('4a. Copy+paste crack password',
                          [r'4a\. .+? tabledata .*? Loaded \s [0-9]+ \s password \s hashes .*? 5a\.',
                           r'4a\. .+? tabledata .*? Proceeding \s with \s wordlist .*? 5a\.',
                           r'4a\. .+? tabledata .*? Proceeding \s with \s incremental.*? 5a\.',
                           r'4a\. .+? tabledata .*? [a-zA-Z]+ \s* \(.+?\)  .*? 5a\.', ]
                          , text, points=35, required=2)
    test5a = keyword_and_length('5a.How long does this take??', [r'[0-9a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) 5b\.', min_length=4, points=1)
    test5b = keyword_and_length('5b. Explain offline vs. online?', [r'[a-zA-Z]+'], text,
                                search_string=r'5b\. .+? tabledata (.+?) gnore.', min_length=10, points=1)
    tests.extend(
        [test1a, test2a, test2b, test2c, test3a, test4a, test5a, test5b,])
    return tests
