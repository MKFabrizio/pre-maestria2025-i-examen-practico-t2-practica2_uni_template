

def main():
    S       = input()
    def es_palindrome(palabra:str):
        if len(palabra)%2==1:
            medio = int(np.floor((len(palabra))/2))
            parte_1 = palabra[:medio]
            parte_2 = palabra[medio+1:][::-1]
            if parte_1==parte_2:
                print('Es palindrome')
            else:
                print('No es palindrome')
        else:
            medio_1 = int(np.floor((len(palabra))/2)) - 1
            medio_2 = int(np.floor((len(palabra))/2))
    
            if palabra[medio_1]==palabra[medio_2]:
                parte_1 = palabra[:medio_1]
                parte_2 = palabra[medio_2+1:][::-1]
                if parte_1==parte_2:
                    print('Es palindrome')
                else:
                    print('No es palindrome')
            else:
                print('No es palindrome')
    es_palindrome(S)

if __name__ == '__main__':
    main()


