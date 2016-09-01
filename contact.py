#Class contact list

class Contact(object):
    def __init__(self,fn,ln, mobile, work, email, twitter):
        self.fn = fn
        self.ln = ln
        self.mobile = mobile
        self.work = work
        self.email= email
        self.twitter= twitter       
    def send_txt(self, message):
        print "To: %s - %s" %(self.mobile, message)


contact_donna = Contact("Donna", "S", "646.801.5228", "818.977.7079", "d@work.com", "dontwitter")
contact_michelle = Contact("michelle", "monica", "650-353-0425","", "michellemmonica@gmail.com","")

contact_donna.send_txt("Wee!")
print Contact
# (contact_donna, "Wee it's Wednesday!")

# def main():



# if __name__ == '__main__':
#     main()