import json

def main(args=[]):
    while True:
        try:
            f = open("contato.txt", encoding="utf8")

            JsonObjs = json.load(f)
            print(JsonObjs)

            break

        except FileNotFoundError:
            print ("Arquivo nao encontrado.")

if __name__== '__main__':
    main()
