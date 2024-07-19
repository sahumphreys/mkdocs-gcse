---
hide:
  - navigation
  - toc
---

<div class="logo-hero">
    <img src="assets/images/logo2.svg" alt="GCSE CS logo"/>
</div>

{{ get_topics()}}


For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Code Annotations

### Code blocks

Inline `code` can be used

With a title:

```py title="Python code block"
print("Hello, World!")
for i in range(10): # (1)!
    print(i)
```

1. This is some annotation for this line of code

With line numbers, and a title:

```py linenums="1", title="Python code block"
print("Hello, World!")
for i in range(10):
    print(i)
```

With line numbers, a title and highlighting:

```py linenums="1", title="Python code block", hl_lines="2"
print("Hello, World!")
for i in range(10):
    print(i)
```
