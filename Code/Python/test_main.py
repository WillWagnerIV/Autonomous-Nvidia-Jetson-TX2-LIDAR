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
    proc_type = "tx2"
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
        print ("     ===  MAIN MENU  ===  ")
        print ("1 -- Spin Motor")
        print ("2 -- Get Data from Sensor")
        print ("3 -- Get Data from AI")
        print ("4 -- Export Data to File")
        print ("5 -- Stream data")
        print ("6 -- Convert LAT/LONG <> X,Y")
        print ("7 -- Convert Radial <> X,Y")
        print ()    
        print ("0 -- Quit")
        print()

    # try:
        menu_choice = int (input ("Please select: "))

        if menu_choice == 1:
            motor = int (input ("Which Motor (1,2,3,4): "))
            speed = int (input ("Enter the speed: "))
            ramp = float (input ("Enter the ramp speed: "))
            print("Spinning Motor...")
            print (gbot.left_motor_1)
            gbot.left_motor_1.spin_motor()  
        elif menu_choice == 2:
            pass

        elif menu_choice == 3:
            pass

        elif menu_choice == 6:
            lat = float (input ("Enter Lat in decimal degrees: "))
            lon = float (input ("Enter Lon in decimal degrees: "))
            x,y,z,timestamp = bcon.latlong_to_cart(lat,lon)
            print("x: {}, y: {}, z: {}, timestamp: {}".format(x,y,z,timestamp))

        elif menu_choice == 0: break

        else:
            print ("\n\n\n")
            print("Please choose a selection from the menu.")

    # except:
        # print ("\n\n\n")
        # print("Please choose a selection from the menu.")

    print ("\n\n\n")


