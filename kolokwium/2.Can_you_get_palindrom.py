def is_palindrome_possible(s):
    s = s.lower()
    s_reversed = s[::-1]

    if s == s_reversed:
        return "YES"

    for i in range(len(s)):
        new_s = s[:i] + s[i + 1:]
        new_s_reversed = new_s[::-1]

        if new_s == new_s_reversed:
            return "YES"

        for j in range(i + 1, len(s)):
            new_s_2 = s[:i] + s[i + 1:j] + s[j + 1:]
            new_s_2_reversed = new_s_2[::-1]

            if new_s_2 == new_s_2_reversed:
                return "YES"

    return "NO"


# Example usage:
s = input()
print(is_palindrome_possible(s))
