import FIlewriter as page

page.start()
page.heading(2,"HTML Forms")

page.Form.label("fname","First Name:")
page.Form.input("text","fname","fname","Jhon")
page.Form.label("lname","Last Name:")
page.Form.input("text","lname","lname","Doe")
page.line_break()
page.Form.input(type="submit",value = "Submit")

page.Form.close()

page.paragraph("""If you click the "Submit" button, 
               the form-data will be sent to a page called "/action_page.php".""")
page.end()