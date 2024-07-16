def categorize_tokens(tokens):
    logical_operators = {}
    keywords = {}
    arithmetic_operators = {}
    identifiers = {}

    # Define lists of operators and keywords
    logical_operator_list = ['and', 'or', 'not']
    python_keywords = [
                    'if', 'else', 'elif', 'while', 'for', 'try', 'except', 'finally', 'raise',
                    'return', 'break', 'continue', 'def', 'class', 'lambda', 'nonlocal', 'global',
                    'with', 'as', 'in', 'is', 'assert', 'yield', 'import', 'from', 'async', 'await',
                    'True', 'False', 'None'
                    ]
    arithmetic_operator_list = ['+', '-', '*', '/']

    for token, token_id in tokens:
        if token in logical_operator_list:  
            if token not in logical_operators:
                logical_operators[token] = []
            logical_operators[token].append(token_id)
        elif token in python_keywords:
            if token not in keywords:
                keywords[token] = []
            keywords[token].append(token_id)
        elif token in arithmetic_operator_list:
            if token not in arithmetic_operators:
                arithmetic_operators[token] = []
            arithmetic_operators[token].append(token_id)
        else:
            # Assuming anything else is an identifier
            if token not in identifiers:
                identifiers[token] = []
            identifiers[token].append(token_id)

    return {
        'logical_operators': logical_operators,
        'keywords': keywords,
        'arithmetic_operators': arithmetic_operators,
        'identifiers': identifiers
    }

# Example usage:
if __name__ == "__main__":
    tokens_with_ids = [
    ('for', 327),
    ('clarity', 26954),
    ('.', 13),
    ('\n', 185),
    ('Here', 4888),
    ('is', 317),
    ('a', 245),
    ('solution', 3402),
    ('this', 437),
    ('problem', 2054),
    ('in', 279),
    ('Python', 13003),
    (':', 25),
    ('```', 10252),
    ('python', 11364),
    ('def', 1551),
    ('fib', 12606),
    ('o', 78),
    ('_', 62),
    ('binary', 23432),
    ('(', 7),
    ('n', 77),
    ('):', 1772),
    ('   ', 315),
    ('=', 405),
    ('[', 821),
    ('0', 15),
    (',', 11),
    (' ', 207),
    ('1', 16),
    (']', 60),
    ('binary', 10042),
    ("''", 15355),
    ('    ', 251),
    ('while', 1470),
    ('[-', 13857),
    ('+', 945),
    ('2', 17),
    ('<=', 14443),
    ('n', 291),
    ('       ', 436),
    ('append', 6880),
    ('f', 69),
    ('ib', 551),
    ('])', 5589),
    ('str', 1401),
    ('%', 3018),
    (')', 8),
    ('//', 1069),
    ('        ', 294),
    ('return', 967),
    ('num', 6487),
    ('int', 1097),
    ('input', 3584),
    ("('", 1497),
    ('Enter', 14651),
    ('number', 1594),
    (" '", 651),
    ('))', 1435),
    ('print', 4128),
    ('F', 37),
    ('on', 249),
    ('ac', 305),
    ('ci', 2711),
    ("',", 1183),
    ('You', 2042),
    ('can', 482),
    ('replace', 8394),
    ('`', 2220),
    ('`', 63),
    ('with', 365),
    ('the', 254),
    ('desired', 8764),
    ('to', 276),
    ('be', 330),
    ('decom', 13349),
    ('posed', 2791),
    ('The', 428),
    ('function', 1155),
    ('takes', 4486),
    ('calcul', 3946),
    ('ates', 980),
    ('its', 891),
    ('decomposition', 19413),
    ('and', 285),
    ('turns', 9240),
    ('it', 359),
    ('into', 878),
    ('string', 2649),
    ('Note', 6014),
    ('only', 885),
    ('up', 578),
    ('given', 2017),
    ('If', 1271),
    ('you', 340),
    ('want', 1120),
    ('generate', 8297),
    ('numbers', 5744),
    ('until', 2632),
    ('less', 2236),
    ('than', 849),
    ('input', 2773),
    ('will', 540),
    ('need', 927),
    ('adjust', 7223),
    ('condition', 4089),
    ('of', 280),
    ('loop', 7845),
    ('', 32021)
]


categorized_tokens = categorize_tokens(tokens_with_ids)

# Example of accessing categorized tokens:
print("Logical Operators:", categorized_tokens['logical_operators'])
print("Keywords:", categorized_tokens['keywords'])
print("Arithmetic Operators:", categorized_tokens['arithmetic_operators'])
# print("Identifiers:", categorized_tokens['identifiers'])
