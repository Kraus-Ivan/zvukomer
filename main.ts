let stav_mereni = false
let pocatecni_cas = 0
let cas_mereni = 0
input.onLogoEvent(TouchButtonEvent.Touched, function spusteni_mereni() {
    
    stav_mereni = true
    pocatecni_cas = control.millis()
})
input.onLogoEvent(TouchButtonEvent.Released, function ukonceni_mereni() {
    
    let konecny_cas = control.millis()
    if (stav_mereni == true) {
        cas_mereni = Math.round((konecny_cas - pocatecni_cas) / 1000)
        stav_mereni = false
    }
    
})
input.onButtonPressed(Button.A, function test() {
    console.log(cas_mereni)
})
