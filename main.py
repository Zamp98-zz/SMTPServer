import user
import input_output

def main():
    r = input_output.loadUsers("users.txt")
    for i in r:
        i.print()
main()
