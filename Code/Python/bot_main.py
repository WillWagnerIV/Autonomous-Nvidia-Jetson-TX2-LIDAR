# GIS Lab Autonomous Bot
# Graeme and Will



import bot_moco as moco
import bot_conv as bcon 
import bot_io as bio



# Main Bot Class
class Bot:
    def __init__(self ):
        print("Initializing a Bot")
    
    name = None
    gpu_type = "tx2"
    bot_type = "ground"  # ground, flying
    mode = "indoor" # indoor, outdoor
    ip_addr = "192.168.1.150"
    right_motor_1 = moco.Motor()
    right_motor_2 = None
    left_motor_1 = moco.Motor()
    left_motor_2 = None
    steering_servo_1 = None
    steering_servo_2 = None
    battery_type = None
    battery_charge = 0
    lat = 0
    long = 0
    x_loc = 0
    y_loc = 0
    camera = None
    lidar = None


def get_start():
    print ()
    menuchoice = int(input('1 - Starting Location in Lat/Long \n' +
                        '2 - Starting Location in X , Y \n' + 
                        'Please choose 1 or 2: ')) 
    if menuchoice == 1:
        print()
        lat = float(input("Enter starting Latitude: "))
        lon = float(input("Enter starting Longitude: "))
        x_loc, y_loc, z_loc, timestamp = bcon.latlong_to_cart(lat,lon)

    elif menuchoice == 2:
        x_loc = float(input("Enter starting X: "))
        y_loc = float(input("Enter starting Y: "))
        z_loc = float(input("Enter starting Z: "))
        lat, lon, timestamp = bcon.cart_to_latlong(x_loc, y_loc, z_loc)

    starting_point = bcon.Point(x_loc,y_loc,z_loc,lat,lon)
    print(starting_point)

    return starting_point


def get_destination():
    print ()
    menuchoice = int(input( '1 - End Location in Lat/Long \n' +
                            '2 - End Location in X , Y \n' + 
                            '3 - End Location by Cartesian Direction \n' +
                            '4 - End Location by Radial Direction \n' +
                            'Please choose: ')) 
    if menuchoice == 1:
        lat = float(input("Enter Final Latitude: "))
        lon = float(input("Enter Final Longitude: "))
        x_loc, y_loc, z_loc, timestamp = bcon.latlong_to_cart(lat,lon)

    elif menuchoice == 2:
        x_loc = float(input("Enter Final X: "))
        y_loc = float(input("Enter Final Y: "))
        z_loc = float(input("Enter Final Z: "))
        lat, lon, timestamp = bcon.cart_to_latlong(x_loc, y_loc, z_loc)

    elif menuchoice == 3:
        x_dist = float(input('Enter X distance: '))
        y_dist = float(input('Enter Y distance: '))
        z_dist = float(input('Enter Z distance: '))

        # ADDITIONAL CODE TO ADD VECTORS/MATRICES

    elif menuchoice == 4:
        bearing = float(input('Enter Bearing from Front of Bot: '))
        destance = float(input('Enter Distance: '))

        # ADDITIONAL CODE TO ADD VECTORS/MATRICES

    end_point = bcon.Point(x_loc,y_loc,z_loc,lat,lon)
    print(end_point)

    return end_point



# Main Loop
if __name__ == "__main__":

    # TX2 Software Test Bot Params
    stb_tx2 = Bot
    print (stb_tx2.lat)
    stb_tx2.name = "stb_test_tx2"


    # Nano Software Params
    # software_test_bot_nano = Bot

    gbot = stb_tx2
    print(gbot.name)

    # Main Menu
    main_menuing = True
    while main_menuing == True:
        print("\n\n")
        print ("     ===  MAIN MENU  ===  ")
        print ("1 -- Calibrate Local Start")
        print ("2 -- Enter Starting Location")
        print ("3 -- Enter Destination")
        print ("4 -- Start")
        print ("5 -- Retrieve")
        print ("6 -- Add Waypoint(s)")
        print ("7 -- Save Mission")
        print ("8 -- Load Mission")
        print ()    
        print ("0 -- Quit")
        print()

    # try:
        menu_choice = int (input ("Please select: "))

        if menu_choice == 1:
            calibrate_local()

        elif menu_choice == 2:
            get_start()

        elif menu_choice == 3:
            get_destination()

        elif menu_choice == 4:
            perform_mission ()

        elif menu_choice == 5:
            complete_mission ()
            

        elif menu_choice == 0: break

        else:
            print ("\n\n\n")
            print("Please choose a selection from the menu.")

    # except:
        # print ("\n\n\n")
        # print("Please choose a selection from the menu.")

    print ("\n\n\n")


