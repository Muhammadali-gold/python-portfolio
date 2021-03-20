import json

data=json.load(open('data.json'))

def main():
    word=input("Please, input search word=").lower()
    if word in data:
        print(data[word])
    else:
        print("Sorry information not found")
if __name__ == '__main__':
    main()
