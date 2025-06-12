CODE_REVIEW_PROMPT = """
Please review the following {language} code from file {file_path}:

```{language}
{code}
```

Analyze the code for:
1. Code quality and best practices
2. Potential bugs or issues
3. Performance optimizations
4. Code style and formatting
5. Maintainability improvements

Provide specific suggestions with line numbers where applicable.
Format your response as structured feedback.
"""

SECURITY_ANALYSIS_PROMPT = """
Analyze the following {language} code from file {file_path} for security vulnerabilities:

```{language}
{code}
```

Look for:
1. Input validation issues
2. SQL injection vulnerabilities
3. XSS vulnerabilities
4. Authentication/authorization flaws
5. Sensitive data exposure
6. Insecure dependencies
7. OWASP Top 10 vulnerabilities

Provide detailed explanations and remediation suggestions.
"""

PERFORMANCE_ANALYSIS_PROMPT = """
Analyze the following {language} code from file {file_path} for performance issues:

```{language}
{code}
```

Identify:
1. Inefficient algorithms or data structures
2. Memory leaks or excessive memory usage
3. Database query optimization opportunities
4. Caching opportunities
5. Async/await optimization
6. Resource cleanup issues

Suggest specific improvements with examples.
"""