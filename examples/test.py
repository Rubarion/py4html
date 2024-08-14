import py4html as page

page.start()
page.heading(1,"sreehari")
page.heading(2,"is a legend")
page.heading(3,"he will change the world")
page.heading(4, "sreehari is great")
page.heading(5, 'sreehari is the best')
page.heading(6,"Nothing is impossible for sreehari")
page.paragraph("""I think sreehari is the greatest engineer of all time.
there is nothing that he cannot acheive""")
page.heading(1,"He is a very emotional Person")
page.Form.label("fname","First name:")
page.Form.input("text","fname","fname","John")
page.Form.label("lname","Last name:")
page.Form.input("text","lname","lanme","Doe")
page.Form.input(type="submit",value="Submit")
page.Form.close()
page.paragraph("""If you click the "Submit" button, the form-data will be sent to a page 
               called "/action_page.php".""")
page.end()