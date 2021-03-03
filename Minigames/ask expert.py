from tkinter import Tk, simpledialog, messagebox

print('Ask the Expert - Dunyoning poytaxt shaharlari')
root = Tk()
root.withdraw()
the_world = {}

def read_from_file():
    with open('Poytaxtlar.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city

def write_to_file(country_name, city_name):
    with open('Poytaxtlar.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)

read_from_file()

while True:
    query_country = simpledialog.askstring('Davlat', 'Davlat nomini kiriting:')

    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer',  query_country + 'ning poytaxti bu ' + result +'!')
    else:
        new_city = simpledialog.askstring('ILtimos! Men bilmayman! Menga o`rgating. ',  query_country + 'ning poytaxti qayer?' )
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)

root.mainloop()        
