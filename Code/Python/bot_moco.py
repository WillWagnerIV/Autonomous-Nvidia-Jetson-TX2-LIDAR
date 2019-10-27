# Motion Control Features
# Will Wagner



class Motor:
    def __init__ (self, mot_type = "pwm", pin_out = 0, mo_speed = 0, mo_direction = "forward"):
        print("Initializing a Motor")
        self.motor_type = mot_type
        self.mspeed = mo_speed
        self.m_dir = mo_direction
        self.pin_out = 1

    def pulse_out(self, which_pin, pulse_amt):
        print ('Should be pulsing out: {}'.format(pulse_amt)) 

    def spin_motor( self, speed = 0, ramp = .5):
        print ('... Spinning a Motor!')
        mspd = speed
        mramp = ramp
        pout_v = .01
        ramp_val = 0

        while ramp_val < mramp:
            print("Ramping up!  Ramp: {}".format(ramp_val))
            self.pulse_out(self.pin_out, pout_v)
            pout_v += .05
            ramp_val += .01
            mspd += 1

    


# test_motor = Motor(mo_speed=225)
# # test_motor.mspeed = 10
# print (test_motor.mspeed)
# print (test_motor.m_dir)
# test_motor.spin_motor(225,.5)
# print (test_motor.mspeed)

