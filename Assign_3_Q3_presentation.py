#importing business code as B
import Assign_3_Q3_business as B


def main():
    '''
    :return: nothing
    uses the functions from business code in a while loop and asks for user input as for what to do
    '''
    print("Task List\n")
    B.menu()
    go = "y"
    while go == "y":
        user_choice = B.choice()
        if user_choice == "view":
            B.view_pending()
        elif user_choice == "history":
            B.view_history()
        elif user_choice == "add":
            B.add_task()
        elif user_choice == "complete":
            B.complete_task()
        elif user_choice == "delete":
            B.delete_task() 
        elif user_choice == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Try again.\n")
            B.menu()


if __name__ == "__main__":
    main()
