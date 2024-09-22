# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input("input number of contacts to upload: "))
i = 0
p_book = {}

while i < n:
    name, phone_number = input("input the number of contacts that you set in the prior input. format 'name' 'phone_number': ").split()
    p_book[name] = phone_number
    i = i + 1

while True:
    query = input("Query as much contacts as you need: ")
    if query == "": 
        break
    elif query in p_book and query != None:
        print(f"{query}={p_book[query]}")
    elif query not in p_book:
        print("Not Found")

