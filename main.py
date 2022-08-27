def on_pin_released_p0():
    global P0_Pressed, P0P1_Pressed, TurnSignal_R, TurnSignal_L
    P0_Pressed = False
    if P0P1_Pressed:
        if not (P1_Pressed):
            P0P1_Pressed = False
    else:
        if not (TurnCancelTouched):
            if TurnSignal_R:
                TurnSignal_R = False
                TurnSignal_L = False
            else:
                TurnSignal_R = True
                TurnSignal_L = False
                Initial_Turn()
input.on_pin_released(TouchPin.P0, on_pin_released_p0)

def CancelTurn():
    global TurnCancelTimer, TurnCancelTouched, TurnSignal_R, TurnSignal_L
    if input.pin_is_pressed(TouchPin.P0) and not (input.pin_is_pressed(TouchPin.P1)):
        TurnCancelTimer += 0.05
        if TurnCancelTimer >= 3:
            TurnCancelTouched = True
            TurnSignal_R = False
            TurnSignal_L = False
    else:
        TurnCancelTouched = False
        TurnCancelTimer = 0
def LowBeam():
    global LowBeamTimer, LowBeamOn, LowBeamTouched, LowBeamSwitch
    if input.pin_is_pressed(TouchPin.P1) and not (input.pin_is_pressed(TouchPin.P0)):
        LowBeamTimer += 0.05
        if LowBeamTimer >= 3:
            if LowBeamSwitch:
                LowBeamOn = True
                LowBeamTouched = True
            else:
                LowBeamOn = False
                LowBeamTouched = True
    else:
        if LowBeamTimer >= 3:
            if LowBeamSwitch:
                LowBeamSwitch = False
                LowBeamTouched = True
            else:
                LowBeamSwitch = True
                LowBeamTouched = True
        LowBeamTouched = False
        LowBeamTimer = 0
    if LowBeamOn:
        led.plot(2, 1)
        pins.digital_write_pin(DigitalPin.P14, 1)
    else:
        led.unplot(2, 1)
        pins.digital_write_pin(DigitalPin.P14, 0)

def on_log_full():
    global logging
    logging = False
datalogger.on_log_full(on_log_full)

def LogTester():
    global logging
    if LowBeamOn:
        logging = True
    else:
        logging = False
    if HighBeamOn:
        datalogger.delete_log(datalogger.DeleteType.FULL)

def on_button_pressed_ab():
    if logging:
        CleanLog()
    else:
        StartLog()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def Initial_Turn():
    global Ready_To_Turn, Turn_Angle, Initial_Angle
    Ready_To_Turn = True
    Turn_Angle = input.compass_heading()
    Initial_Angle = Turn_Angle
def HighBeam():
    global HighBeamTimer, HighBeamOn, HighBeamBlink
    if input.pin_is_pressed(TouchPin.P0) and input.pin_is_pressed(TouchPin.P1):
        HighBeamTimer += 0.05
        if HighBeamTimer >= 3:
            HighBeamOn = True
            if not (HighBeamBlink):
                HighBeamBlink = True
                pins.digital_write_pin(DigitalPin.P15, 0)
                led.unplot(2, 0)
                basic.pause(100)
        else:
            HighBeamOn = False
        led.plot(2, 0)
        pins.digital_write_pin(DigitalPin.P15, 1)
    else:
        if not (HighBeamOn):
            pins.digital_write_pin(DigitalPin.P15, 0)
            led.unplot(2, 0)
        HighBeamBlink = False
        HighBeamTimer = 0
    if HighBeamOn:
        led.plot(2, 0)
        pins.digital_write_pin(DigitalPin.P15, 1)

def on_pin_released_p1():
    global P1_Pressed, P0P1_Pressed, TurnSignal_R, TurnSignal_L
    P1_Pressed = False
    if P0P1_Pressed:
        if not (P0_Pressed):
            P0P1_Pressed = False
    else:
        if not (LowBeamTouched):
            if TurnSignal_L:
                TurnSignal_R = False
                TurnSignal_L = False
            else:
                TurnSignal_L = True
                TurnSignal_R = False
                Initial_Turn()
input.on_pin_released(TouchPin.P1, on_pin_released_p1)

def BrakeLight():
    global BrakeEngineShake, BrakeTimer
    if input.acceleration(Dimension.Y) > 300:
        BrakeEngineShake = True
        BrakeTimer = 0
    if input.acceleration(Dimension.Y) < -500:
        BrakeTimer += 0.025
        if BrakeTimer >= 0.25:
            led.plot(2, 2)
            pins.digital_write_pin(DigitalPin.P13, 1)
            basic.pause(1000)
    else:
        led.unplot(2, 2)
        BrakeTimer = 0
        pins.digital_write_pin(DigitalPin.P13, 0)
def CleanLog():
    global logging
    music.play_tone(880, music.beat(BeatFraction.EIGHTH))
    basic.show_icon(IconNames.NO)
    basic.pause(100)
    basic.clear_screen()
    logging = False
    datalogger.delete_log(datalogger.DeleteType.FULL)
def StartLog():
    global logging
    music.play_tone(147, music.beat(BeatFraction.EIGHTH))
    basic.show_icon(IconNames.YES)
    basic.pause(100)
    basic.clear_screen()
    logging = True
HighBeamTimer = 0
Initial_Angle = 0
Turn_Angle = 0
TurnCancelTimer = 0
TurnCancelTouched = False
P1_Pressed = False
P0_Pressed = False
HighBeamBlink = False
Ready_To_Turn = False
TurnSignal_L = False
TurnSignal_R = False
BrakeEngineShake = False
LowBeamSwitch = False
HighBeamOn = False
LowBeamTouched = False
LowBeamOn = False
BrakeTimer = 0
LowBeamTimer = 0
P0P1_Pressed = False
logging = False
logging = False
datalogger.include_timestamp(FlashLogTimeStampFormat.SECONDS)
datalogger.set_column_titles("y")
music.set_volume(255)
music.play_tone(880, music.beat(BeatFraction.EIGHTH))
P0P1_Pressed = False
pins.digital_write_pin(DigitalPin.P0, 0)
pins.digital_write_pin(DigitalPin.P1, 0)
LowBeamTimer = 0
BrakeTimer = 0
LowBeamOn = False
LowBeamTouched = False
HighBeamOn = False
LowBeamSwitch = True
BrakeEngineShake = False
led.plot(0, 0)
basic.pause(100)
led.unplot(0, 0)
led.plot(4, 0)
basic.pause(100)
led.unplot(4, 0)
led.plot(4, 4)
basic.pause(100)
led.unplot(4, 4)
led.plot(0, 4)
basic.pause(100)
led.unplot(0, 4)
TurnSignal_R = False
TurnSignal_L = False
Ready_To_Turn = False
HighBeamBlink = False

def on_forever():
    global P0_Pressed, P0P1_Pressed, P1_Pressed
    if input.pin_is_pressed(TouchPin.P0):
        P0_Pressed = True
        if P1_Pressed:
            P0P1_Pressed = True
    if input.pin_is_pressed(TouchPin.P1):
        P1_Pressed = True
        if P0_Pressed:
            P0P1_Pressed = True
    CancelTurn()
    LowBeam()
    HighBeam()
    BrakeLight()
basic.forever(on_forever)

def on_every_interval():
    if logging:
        datalogger.log(datalogger.create_cv("y", input.acceleration(Dimension.X)))
loops.every_interval(250, on_every_interval)

def on_every_interval2():
    if TurnSignal_R:
        led.plot(0, 2)
        pins.digital_write_pin(DigitalPin.P12, 0)
        pins.digital_write_pin(DigitalPin.P8, 1)
        music.play_tone(880, music.beat(BeatFraction.EIGHTH))
        basic.pause(300)
        led.unplot(0, 2)
        pins.digital_write_pin(DigitalPin.P8, 0)
        basic.pause(300)
    if TurnSignal_L:
        led.plot(4, 2)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P12, 1)
        music.play_tone(880, music.beat(BeatFraction.EIGHTH))
        basic.pause(300)
        led.unplot(4, 2)
        pins.digital_write_pin(DigitalPin.P12, 0)
        basic.pause(300)
loops.every_interval(100, on_every_interval2)
