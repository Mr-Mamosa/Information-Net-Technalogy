def rail_fence_cipher(plain_text, num_rails):
    # Initialize the rails as a list of empty strings
    rails = ['' for _ in range(num_rails)]
    direction = 1
    rail_index = 0

    for char in plain_text:
        rails[rail_index] += char
        rail_index += direction

        # Change direction when reaching the top or bottom rail
        if rail_index == 0 or rail_index == num_rails - 1:
            direction *= -1

    # Join the rails to form the cipher text
    cipher_text = ''.join(rails)
    return cipher_text

def main():
    print("******************RAILFENCE CIPHER******************")
    plain_text = input('Enter the Plain Text: ')
    num_rails = int(input("Enter the number of rails: "))

    cipher_text = rail_fence_cipher(plain_text, num_rails)

    print("The Cipher text is: ", cipher_text)

if __name__ == "__main__":
    main()
