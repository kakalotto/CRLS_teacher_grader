def docs_feedback_hardware_displays(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Resolution of monitors?', [r'1a\. .+? tabledata .*? 1920 \s* x \s* 1080 .*?  1b\.',
                                                          r'1a\. .+? tabledata .*? 1440 \s* x \s* 900 .*?  1b\.',],
                          text, points=5)
    test1b = exact_answer('1b. Type of video card?',
                          [r'1b\. .+? tabledata .*? AMD \s Radeon .*? Graphics  .*?  1c\.',
                           r'1b\. .+? tabledata .*? 1200 \s* x \s* 1020 .*?  1c\.', ],
                          text, points=5)
    test1c = exact_answer('1c. Monitor type?', [r'1c\. .+? tabledata .*? [gG]eneric .*?  ideo.',],
                          text, points=5)
    test2a = exact_answer('2a. Driver name, provider, version?',
                          [r'2a\. .+? tabledata .*? AMD \s Radeon \s HD  \s 8570 \s Graphics  .*?  2b\.',
                           r'2a\. .+? tabledata .*? Advanced \s Micro \s Devices .*?  2b\.',
                           r'2a\. .+? tabledata .*? [0-9][0-9]\.[0-9][0-9][0-9] .*?  2b\.',
                           r'2a\. .+? tabledata .*? ATI \s Technologies \s  .*?  2b\.',
                           r'2a\. .+? tabledata .*? ATI \s Radeon \s HD   .*?  2b\.'
                           ],
                          text, points=5, required=3)
    test2b = exact_answer('2b. Driver date version?',
                          [r'2b\. .+? tabledata .*? [0-9][0-9]\.[0-9][0-9][0-9] .*? isplay',
                           r'2b\. .+? tabledata .*? 20[0-9][0-9] .*? isplay'],
                          text, points=5)
    test3a = exact_answer('3a. VGA pic?', [r'3a\. .+? tabledata .*? aaa \s inlineobject .*? 3b\.'],
                          text, points=1, )
    test3b = exact_answer('3b. DVI pic?', [r'3b\. .+? tabledata .*? aaa \s inlineobject .*? 3c\.'],
                          text, points=1, )
    test3c = exact_answer('3c. Displayport pic?', [r'3c\. .+? tabledata .*? aaa \s inlineobject .*? 3d\.'],
                          text, points=1, )
    test3d = keyword_and_length('3d. Why DVI/Display over VGA?', [r'[a-zA-Z]+'], text,
                                search_string=r'3d. .+? tabledata (.+?) rouble', min_length=7, points=1)

    tests.extend(
        [test1a, test1b, test1c, test2a, test2b, test3a, test3b, test3c, test3d, ])

    return tests
