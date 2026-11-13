# Reflection

The provided handout asks for four reflection answers but does not include the wording of those questions. These responses address the reflection topics described in the handout.

1. Static analysis examines source without running it. It quickly found security risks and maintainability issues, while dynamic tests are still needed to confirm actual behavior.
2. Bandit identified the highest-risk patterns: evaluating user input and constructing SQL with string interpolation. Replacing these patterns removed code execution and injection risks.
3. Pylint and Flake8 helped make the program easier to read and maintain through consistent naming, documentation, and formatting. Tool findings need review because not every warning represents a user-visible bug.
4. Static analysis is most useful as an early, repeatable review step. It cannot prove correctness or catch every runtime problem, so it should be paired with tests and careful review.
