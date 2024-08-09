f=open("index.html",'w')
start_string = """<!DOCTYPE html>
<html>
<body>
"""
end_string = """</body>
</html>
"""  
def start():
    f.write(start_string)

def heading(num,text):
    f.write(f"<h{num}>{text}</h{num}>\n")

def paragraph(text):
    f.write(f"<p>{text}</p>\n")

def line_break():
    
    f.write("<br>")
    

    
class Form():
    def __init__(self):
        f.write("<form action="">\n")
    def label(id,text):
        f.write(f"<label for=\"{id}\">{text}</label><br>\n")


    def input(type="",id="",name="",value=""):
        if type=="text":
            f.write(f"<input type=\"text\" id=\"{id}\" name=\"{name}\" value=\"{value}\"><br>\n")
        if type=="submit":
            f.write(f"<input type=\"submit\" value=\"{value}\">")
    def close():
        f.write("</form>\n")        
    
    
def end():
    f.write(end_string)
    f.close()