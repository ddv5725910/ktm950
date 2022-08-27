input.onPinReleased(TouchPin.P0, function () {
    P0_Pressed = false
    if (P0P1_Pressed) {
        if (!(P1_Pressed)) {
            P0P1_Pressed = false
        }
    } else {
        if (!(TurnCancelTouched)) {
            if (TurnSignal_R) {
                TurnSignal_R = false
                TurnSignal_L = false
            } else {
                TurnSignal_R = true
                TurnSignal_L = false
                Initial_Turn()
            }
        }
    }
})
function CancelTurn () {
    if (input.pinIsPressed(TouchPin.P0) && !(input.pinIsPressed(TouchPin.P1))) {
        TurnCancelTimer += 0.05
        if (TurnCancelTimer >= 3) {
            TurnCancelTouched = true
            TurnSignal_R = false
            TurnSignal_L = false
        }
    } else {
        TurnCancelTouched = false
        TurnCancelTimer = 0
    }
}
function LowBeam () {
    if (input.pinIsPressed(TouchPin.P1) && !(input.pinIsPressed(TouchPin.P0))) {
        LowBeamTimer += 0.05
        if (LowBeamTimer >= 3) {
            if (LowBeamSwitch) {
                LowBeamOn = true
                LowBeamTouched = true
            } else {
                LowBeamOn = false
                LowBeamTouched = true
            }
        }
    } else {
        if (LowBeamTimer >= 3) {
            if (LowBeamSwitch) {
                LowBeamSwitch = false
                LowBeamTouched = true
            } else {
                LowBeamSwitch = true
                LowBeamTouched = true
            }
        }
        LowBeamTouched = false
        LowBeamTimer = 0
    }
    if (LowBeamOn) {
        led.plot(2, 1)
        pins.digitalWritePin(DigitalPin.P14, 1)
    } else {
        led.unplot(2, 1)
        pins.digitalWritePin(DigitalPin.P14, 0)
    }
}
datalogger.onLogFull(function () {
    logging = false
})
function LogTester () {
    logging = LowBeamOn
}
input.onButtonPressed(Button.AB, function () {
    CleanLog()
})
function Initial_Turn () {
    Ready_To_Turn = true
    Turn_Angle = input.compassHeading()
    Initial_Angle = Turn_Angle
}
function HighBeam () {
    if (input.pinIsPressed(TouchPin.P0) && input.pinIsPressed(TouchPin.P1)) {
        HighBeamTimer += 0.05
        if (HighBeamTimer >= 3) {
            HighBeamOn = true
            if (!(HighBeamBlink)) {
                HighBeamBlink = true
                pins.digitalWritePin(DigitalPin.P15, 0)
                led.unplot(2, 0)
                basic.pause(100)
            }
        } else {
            HighBeamOn = false
        }
        led.plot(2, 0)
        pins.digitalWritePin(DigitalPin.P15, 1)
    } else {
        if (!(HighBeamOn)) {
            pins.digitalWritePin(DigitalPin.P15, 0)
            led.unplot(2, 0)
        }
        HighBeamBlink = false
        HighBeamTimer = 0
    }
    if (HighBeamOn) {
        led.plot(2, 0)
        pins.digitalWritePin(DigitalPin.P15, 1)
    }
}
input.onPinReleased(TouchPin.P1, function () {
    P1_Pressed = false
    if (P0P1_Pressed) {
        if (!(P0_Pressed)) {
            P0P1_Pressed = false
        }
    } else {
        if (!(LowBeamTouched)) {
            if (TurnSignal_L) {
                TurnSignal_R = false
                TurnSignal_L = false
            } else {
                TurnSignal_L = true
                TurnSignal_R = false
                Initial_Turn()
            }
        }
    }
})
function BrakeLight () {
    if (input.acceleration(Dimension.Y) > 300) {
        BrakeEngineShake = true
        BrakeTimer = 0
    }
    if (input.acceleration(Dimension.Y) < -500) {
        BrakeTimer += 0.025
        if (BrakeTimer >= 0.25) {
            led.plot(2, 2)
            pins.digitalWritePin(DigitalPin.P13, 1)
            basic.pause(1000)
        }
    } else {
        led.unplot(2, 2)
        BrakeTimer = 0
        pins.digitalWritePin(DigitalPin.P13, 0)
    }
}
function CleanLog () {
    music.playTone(880, music.beat(BeatFraction.Eighth))
    basic.showIcon(IconNames.Skull)
    basic.pause(100)
    basic.clearScreen()
    logging = false
    datalogger.deleteLog(datalogger.DeleteType.Full)
}
let HighBeamTimer = 0
let Initial_Angle = 0
let Turn_Angle = 0
let TurnCancelTimer = 0
let TurnCancelTouched = false
let P1_Pressed = false
let P0_Pressed = false
let HighBeamBlink = false
let Ready_To_Turn = false
let TurnSignal_L = false
let TurnSignal_R = false
let BrakeEngineShake = false
let LowBeamSwitch = false
let HighBeamOn = false
let LowBeamTouched = false
let LowBeamOn = false
let BrakeTimer = 0
let LowBeamTimer = 0
let P0P1_Pressed = false
let logging = false
logging = false
datalogger.includeTimestamp(FlashLogTimeStampFormat.Seconds)
datalogger.setColumnTitles("y")
music.setVolume(255)
music.playTone(880, music.beat(BeatFraction.Eighth))
P0P1_Pressed = false
pins.digitalWritePin(DigitalPin.P0, 0)
pins.digitalWritePin(DigitalPin.P1, 0)
LowBeamTimer = 0
BrakeTimer = 0
LowBeamOn = false
LowBeamTouched = false
HighBeamOn = false
LowBeamSwitch = true
BrakeEngineShake = false
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
TurnSignal_R = false
TurnSignal_L = false
Ready_To_Turn = false
HighBeamBlink = false
basic.forever(function () {
    LogTester()
    if (input.pinIsPressed(TouchPin.P0)) {
        P0_Pressed = true
        if (P1_Pressed) {
            P0P1_Pressed = true
        }
    }
    if (input.pinIsPressed(TouchPin.P1)) {
        P1_Pressed = true
        if (P0_Pressed) {
            P0P1_Pressed = true
        }
    }
    CancelTurn()
    LowBeam()
    HighBeam()
    BrakeLight()
})
loops.everyInterval(250, function () {
    if (logging) {
        datalogger.log(datalogger.createCV("y", input.acceleration(Dimension.X)))
    }
})
loops.everyInterval(100, function () {
    if (TurnSignal_R) {
        led.plot(0, 2)
        pins.digitalWritePin(DigitalPin.P12, 0)
        pins.digitalWritePin(DigitalPin.P8, 1)
        music.playTone(880, music.beat(BeatFraction.Eighth))
        basic.pause(300)
        led.unplot(0, 2)
        pins.digitalWritePin(DigitalPin.P8, 0)
        basic.pause(300)
    }
    if (TurnSignal_L) {
        led.plot(4, 2)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P12, 1)
        music.playTone(880, music.beat(BeatFraction.Eighth))
        basic.pause(300)
        led.unplot(4, 2)
        pins.digitalWritePin(DigitalPin.P12, 0)
        basic.pause(300)
    }
})
