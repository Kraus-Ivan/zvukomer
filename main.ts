// ULOZENI NAHODNEHO CASU TONU
let delka_tonu = 0
input.onButtonPressed(Button.B, function btnB() {
    
    delka_tonu = randint(1000, 10000)
    music.playTone(262, delka_tonu)
    console.log(delka_tonu)
})
// OPAKOVANE PREHRATI ULOZENEHO TONU
input.onButtonPressed(Button.A, function btnA() {
    
    if (delka_tonu > 0) {
        music.playTone(262, delka_tonu)
    }
    
})
// MERENI CASU UZIVATELE
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
        cas_mereni = konecny_cas - pocatecni_cas
        stav_mereni = false
    }
    
    console.log(cas_mereni)
    vyhodnoceni()
})
// VYHODNOCENI
// POKUD cas_mereni JE VETSI JAK delka_tonu, ZOBRAZI SE ">" (ODCHYLKA 0,5 SEKUNDY)
function vyhodnoceni() {
    
    if (cas_mereni <= delka_tonu + 500) {
        led.plotBarGraph(cas_mereni, delka_tonu)
        if (led.point(0, 0)) {
            soundExpression.happy.play()
        }
        
    } else {
        basic.showLeds(`
        . # . . .
        . . # . .
        . . . # .
        . . # . .
        . # . . .
        `)
        soundExpression.sad.play()
    }
    
}

