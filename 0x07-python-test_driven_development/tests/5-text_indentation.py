The ``5-text_indentation`` module
======================

Using ``text_indentation``
-------------------

This is an test text file. These are the possible test cases:

    ##### Importing the function from the module #####
    >>> text_indentation = __import__('5-text_indentation').text_indentation

    ##### Check that the file is executable #####
    >>> import os
    >>> os.access("5-text_indentation.py", os.X_OK)
    True

    ##### Check for the documentation of the module #####
    >>> len(__import__("5-text_indentation").__doc__) > 1
    True

    ##### Check for the documentation of the function #####
    >>> len(__import__("5-text_indentation").text_indentation.__doc__) > 1
    True

    ##### Check for pep8 style #####
    >>> os.popen("pep8 5-text_indentation.py").read()
    ''

    ##### Check for a newline at the end of the file #####
    >>> os.popen("cat -e 5-text_indentation.py | tail -1").read()[-1]
    '\n'

    ##### Check for the file has a shebang #####
    >>> os.popen("cat 5-text_indentation.py | head -1").read()
    '#!/usr/bin/python3\n'

    ##### Check that the README file exists #####
    >>> cwd = os.getcwd()
    >>> check_readme = cwd + '/README.md'
    >>> os.path.exists(check_readme)
    True

    ##### Check when a large text is passed #####
    >>> text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres""")
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <BLANKLINE>
    Quonam modo?
    <BLANKLINE>
    Utrum igitur tibi litteram videor an totas paginas commovere?
    <BLANKLINE>
    Non autem hoc:
    <BLANKLINE>
    igitur ne illud quidem.
    <BLANKLINE>
    Fortasse id optimum, sed ubi illud:
    <BLANKLINE>
    Plus semper voluptatis?
    <BLANKLINE>
    Teneo, inquit, finem illi videri nihil dolere.
    <BLANKLINE>
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.
    <BLANKLINE>
    Si id dicis, vicimus.
    <BLANKLINE>
    Inde sermone vario sex illa a Dipylo stadia confecimus.
    <BLANKLINE>
    Sin aliud quid voles, postea.
    <BLANKLINE>
    Quae animi affectio suum cuique tribuens atque hanc, quam dico.
    <BLANKLINE>
    Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres

    ##### Check when a integer data type is passed #####
    >>> text_indentation(20)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string
