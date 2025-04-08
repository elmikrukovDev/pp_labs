def decrypt(encrypted_message):
    stack = []
    i = 0

    while i < len(encrypted_message):
        if encrypted_message[i] == '.':
            if i + 1 < len(encrypted_message) and encrypted_message[i + 1] == '.':
                if stack:
                    stack.pop()
                i += 2
            else:
                i += 1
        else:
            stack.append(encrypted_message[i])
            i += 1
    
    return ''.join(stack)

if __name__ == '__main__':
    import sys

    input_data = sys.stdin.read().strip()

    print(decrypt(input_data))