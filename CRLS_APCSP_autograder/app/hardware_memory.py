def docs_feedback_hardware_memory(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test1c = exact_answer('1c. How much memory?', [r'1c\. .+? tabledata \s* (8|16|32) .*? g .+? 1d\.'], text, points=5)
    test1d = exact_answer('1d. ECC?', [r'1d\. .+? tabledata \s* n .+? 1e\.'], text, points=5)
    test1e = exact_answer('1e. Full memory test. How long??', [r'1d\. .+? tabledata .+? [0-9] .+? 1f\.'],
                          text, points=1)
    test1f = exact_answer('1f. Memory speed and type', [r'1f\. .+? tabledata .+? [0-9] .+? 1g\.',
                                                        r'1f\. .+? tabledata .+? ddr .+? 1g\.'],
                          text, required=2, points=1)
    test1g = exact_answer('1g. Full memory test 192G. How long??', [r'1g\. .+? tabledata \s* [0-9] .+? memory'],
                          text, points=1)
    test2b = exact_answer('2b. removed. Teacher marks?', [r'2b\. .+? tabledata .+? [a-z] .+? 2c\.'], text, points=1)
    test2c = exact_answer('2c. replaced. Teacher marks?', [r'2c\. .+? tabledata .+? [a-z] .+? how'], text, points=1)
    test3a = exact_answer('3a. screenshot memory', [r'3a\. .+? tabledata \s aaa \s inlineobject .+? picking'],
                          text, points=1)
    test4a = exact_answer('4a. Memory speed and type', [r'4a\. .+? tabledata .+? [0-9] .+? 4b\.',
                                                        r'4a\. .+? tabledata .+? ddr .+? 4b\.',
                                                        r'4a\. .+? tabledata .+? ecc .+? 4b\.'],
                          text, required=3, points=1)
    test4b = exact_answer('4b. Max memory desktop?', [r'4b\. .+? tabledata \s* [0-9] .*? g .+? pick'], text, points=1)
    test5a = exact_answer('5a. Memory speed and type', [r'5a\. .+? tabledata .+? [0-9] .+? 5b\.',
                                                        r'5a\. .+? tabledata .+? ddr .+? 5b\.',
                                                        r'5a\. .+? tabledata .+? ecc .+? 5b\.'],
                          text, required=3, points=1)
    test5b = exact_answer('5b. Max memory server?', [r'5b\. .+? tabledata \s* [0-9] .*? g .+? comparison'],
                          text, points=1)

    test6a = keyword_and_length('6a. Compare server/desktop memory', [r'[a-zA-Z]+'], text,
                                search_string=r'6a\. .+? tabledata (.+) laptop', min_length=15, points=1)
    test7a = keyword_and_length('7a. sodimm', [r'[a-zA-Z]+'], text,
                                search_string=r'7a\. .+? tabledata (.+) check', min_length=7, points=1)
    tests.extend([test1c, test1d, test1e, test1f, test1g, test2b, test2c, test3a, test4a, test4b, test5a, test5b,
                  test6a, test7a])
    return tests
