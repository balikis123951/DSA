def balanced_brackets(text):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in text:


        if char in '([{':
            stack.append(char)


        elif char in ')]}':

            if not stack:
                return False

            if stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


print(balanced_brackets("(hello)"))


print(balanced_brackets("{[()]}"))


print(balanced_brackets("([)]"))


print(balanced_brackets("((hello)"))


print(balanced_brackets("()[]{}"))


print(balanced_brackets("hello"))


print(balanced_brackets(")("))


