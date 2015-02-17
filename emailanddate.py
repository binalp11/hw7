from bs4 import BeautifulSoup



# these lines were used to generate paths all of the html files
filepath = open('filepath.txt', 'a')


for xx in range(1, 813):
    xyz =str("/home/vagrant/hw7htmlfiles/seminars/" + str(xx) + ".html")
    filepath.write(xyz + '\n')
filepath.close()

pathfile = open('filepath.txt')

allpath = pathfile.read()
lines = allpath.splitlines()


#code for parsing the soup for each path
for line in lines:
    #opens the soup for the html code
    soup = BeautifulSoup(open(line))

    #finds the section the information we want is stored
    section = soup.find("div", class_="section")
    #since  we only want the names and dates of EcoEvoPub speakers this tests
    #to see if there is a flag for EcoEvoPub speakers, if there is it will print the information
    word = section.p.next.next
    eco = u'EcoEvoPub Series \n'
    if word == eco:
        date = section.h4.contents
        print date



# however the code above does not work, although it does work if i only test it without the loop (single page at a time)
#i still cannot figure out how to extract the speakers names as they are listed in one paragraph 
#with line breaks

    soup = BeautifulSoup(open("/home/vagrant/hw7htmlfiles/seminars/797.html"))
    section = soup.find("div", class_="section")
    word = section.p.next.next.next.get_text()
    eco = u'EcoEvoPub Series \n'
        if word == eco:
            date = section.h4.contents
            print date

#output> [u'February 26 2015 ']


          