def write_file(file_name, file_content):

    with open(f"{file_name}.txt", mode='w', encoding= 'utf-8') as f:
      f.write("This is a test content.")
    
    with open(f"{file_content}.txt", mode='w', encoding= 'utf-8') as f2:
      f2.write("SmokingMirror")

    

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode='a', encoding= 'utf-8') as f3:
      f3.write(append_content)
    
    
    

def read_file(file_name):
    with open(f"{file_name}.txt", mode='r', encoding= 'utf-8') as f4:
      return f4.read()
