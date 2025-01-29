def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':  # Uppercase letters
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':  # Lowercase letters
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

# Example usage
message = "Hello, World"
shift = 3

encrypted = caesar_cipher(message, shift)
decrypted = caesar_cipher(encrypted, -shift)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)