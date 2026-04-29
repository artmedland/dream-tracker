# Pylint report

Pylint prints out the following report:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:125:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:170:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:183:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:193:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:244:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:254:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:306:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:324:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:341:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:367:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:423:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:442:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:446:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:475:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:498:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:505:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module db
db.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:12:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:19:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:29:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:53:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module posts
posts.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module seed
seed.py:45:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:63:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:77:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:88:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:99:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:123:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:140:11: W0718: Catching too general exception Exception (broad-exception-caught)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0411: standard import "datetime.datetime" should be placed before third party imports "werkzeug.security.generate_password_hash", "werkzeug.security.check_password_hash" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 9.06/10 (previous run: 9.06/10, +0.00)
```

## Justifications

### Docstrings

On several occasions, Pylint warns that module, function and method docstrings are missing. In general, during the development of the program, the use of docstrings has been liberal, particularly in place of traditional commentation. A few notable exceptions:

- Functions preceded by a decorator, such as `@app.route`, contain no function docstrings. The developer sees the purpose of these functions as self-evident.
- Only helper modules have been given module-level docstrings. The primary module, as well as any refactored secondary modules (such as `users.py`), have intentionally been left free of docstrings.
- Module docstrings have intentionally been omitted from the module `db.py`, as this module closely resembles the implementation found in the course material.
- The helper function `logged_in()` is considered self-explanatory.

### External libraries

Occasionally, Pylint claims, for instance, that `standard import "datetime.datetime" should be placed before third-party imports "werkzeug..."`.
The developer considers that a flawed or non-standard ordering or grouping is preferable to a lack of ordering or grouping, and that the style used in the program is logical and aesthetically pleasing.

Note that `import` statements can be grouped and joined by commas as follows:

```
*** users.py
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from werkzeug.security import generate_password_hash, check_password_hash
```

The developer considers the benefit from this technique to be marginal compared to the downsides of writing needlessly lengthy lines. Imports have been split as such to avoid line lengths exceeding 72 characters, including tabs and spaces.

Finally, Pylint warns that some external modules could not be imported - `unable to import 'flask'`. This is presumably a side effect of `venv` virtual environments, but has no effect on the functionality of the program.

### Error handling

Pylint claims that the program is `catching too general exception Exception`. This refers to a preference toward catching more specific derived error classes with the `except` block, as opposed to the base class `Exception`. Generally, it is ill-advised to catch a general error – as it provides little information about the *cause of said error* – especially if the program fails to handle the exceptions for a good reason, or in a meaningful way.

However, the developer considers the module containing these errors, `seed.py`, to be utilized primarily for testing purposes. The flaws in this module do not reflect any flaws in the program, and the errors that are handled are collected solely for the debugging convenience of the programmer.

### Dangerous default values

Pylint warns that the standard argument values in some method invocations may cause unpredictable behavior:

`dangerous default value [] as argument`

This refers to a strange Pythonic quirk: an empty list is initialized as a reference to an object instance, which is shared across invocations. Providing `[]` as a default value for a function parameter may introduce issues if a method modifies the contents of the list. However, as no method does so, this issue has no effect on the functionality of the program.

### Constant naming conventions

In `seed.py`, Pylint warns that the `constant name "errs" doesn't conform to UPPER_CASE naming style`. Said CAPITAL_SNAKE_CASE naming convention has been utilized elsewhere in the application, primarily in the `seed` and `config` modules. 

Notably, `seed:~errs` *is not a constant, but a variable* – the value of this field is retrieved and updated throughout the program.

> If it looks like a variable, acts like a variable and quacks like a variable -- it's probably a variable!