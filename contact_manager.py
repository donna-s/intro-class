from contact import Contact

contact_michelle = Contact("michelle", "monica", "650-353-0425","", "michellemmonica@gmail.com","")
contact_donna = Contact("Donna", "S", 6468015228, 8189777079, "d@work.com", "dontwitter")

contact_list = []
# contact_list.append(contact_donna)

# for info in contact_list:
#     print info.fn


# def show_current_contacts():
#     contact_list = []
#     global contact_list
#     for info in contact_list:
#         print info.fn

# print show_current_contacts
    # with open ("contact.py") as my_file:
        # return contact.fn

def add_new_contact():
    friend = []
    first_name = raw_input("Please provide the Contact's First Name")
    friend.append(first_name)
    friend.append(first_name)
    last_name = raw_input("Please provide the Contact's Last Name")
    friend.append(last_name)
    cell=raw_input("Please provide the Contact's Mobile")
    friend.append(cell)
    work = raw_input("Please provide the Contact's Work")
    friend.append(work)
    email= raw_input("Please provide the Contact's Email")
    friend.append(email)
    twit= raw_input("Please provide the Contact's twitter")
    friend.append(twit)
    return Contact(friend)

print add_new_contact()
print contact_list.fn    
# # def edit_contact():

# # def delete_contact():

# def menu():
#     selection = raw_input("Please choose one of the following: 1- Show current Contacts 2- Add new Contact 3- Edit Contact 4- Delete Contact")
#     print selection
#     if selection == "1":
#         show_current_contacts
#     elif selection == "2":
#         add_new_contact()
#     elif selection == "3":
#         edit_contact
#     elif selection == "4":
#         delete_contact
#     else:
#         print "That's not a choice"
#         exit()

# def main():

#     selection = raw_input("Please choose one of the following: 1- Show current Contacts 2- Add new Contact 3- Edit Contact 4- Delete Contact")
#     print selection

#     print show_current_contacts

# if __name__ == '__main__':
#         main()