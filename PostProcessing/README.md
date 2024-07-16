# Token Categorizer file (token_categorize.py)

- This file provides a Python script to categorize tokens from a given list(tokens we get from the deepseek model) into logical operators, keywords, arithmetic operators, and identifiers. The categorization helps in analyzing and understanding the distribution and usage of different types of tokens in a given text or code snippet, which we are using in postprocessing for generating codes with some logical issue .

## Features

- Categorizes tokens into:
  - Logical Operators
  - Keywords
  - Arithmetic Operators
  - Identifiers
- Supports a predefined list of logical operators, Python keywords, and arithmetic operators.

## Post processing after categorized the tokens (post_procesing.py)
This python script randomly modifies certain operators in a given code snippet. The modification can be useful for creating code with logical issues, testing edge cases, or simply experimenting with different operator mappings.

## Features

- Randomly selects 3 or 10 operators from a predefined list to modify.
- Modifies operators in the provided code snippet based on a predefined mapping.
- Supports various operators including comparison, arithmetic, and logical operators.

