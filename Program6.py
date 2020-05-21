#***************************************************************
#
#  Developer:         Renee White
#
#  Program #:         Program 6
#
#  File Name:         Program6.py
#
#  Description:       This is a program that calculates the occupancy rate for a hotel
#
#***************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():
    
    developerInfo()
    
    print('Welcome to your hotel management system.')
    print('')
    floors = int(input('How many floors does your hotel have?: '))
    print('')
    TotalRooms = 0
    TotalOcc = 0
    for floor in range(floors):
        print('Floor number', floor + 1)
        print('-----------------')
        NumRooms = int(input('How many rooms are on this floor?: '))
        TotalRooms = TotalRooms + NumRooms
        occ = int(input('How many rooms are occupied on this floor?: '))
        print('')
        print('')
        TotalOcc = TotalOcc + occ
        NotOcc = TotalRooms - TotalOcc
        Percentage = TotalOcc / TotalRooms

            

    print('')
    print('')
    print('Your hotel has a total of', TotalRooms, 'rooms')
    print('Your hotel has a total of', TotalOcc, 'occupied rooms')
    print('Your hotel has a total of', NotOcc, 'unoccupied rooms available')
    print('Your hotel has a total occupancy percentage of', format(Percentage, '.0%'))
    
            
    
        
            
             
        

    
    # End of the main function 
    
#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     Renee White')
    print('Program:  Six')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1
