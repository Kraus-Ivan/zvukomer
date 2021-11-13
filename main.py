#ULOZENI NAHODNEHO CASU TONU
delka_tonu = 0
def btnB():
    global delka_tonu
    delka_tonu = randint(1000, 10000)
    music.play_tone(frequency = 262, ms = delka_tonu)
    print(delka_tonu)
input.on_button_pressed(Button.B, btnB)

#OPAKOVANE PREHRATI ULOZENEHO TONU
def btnA():
    global delka_tonu
    if delka_tonu > 0:
        music.play_tone(frequency = 262, ms = delka_tonu)
input.on_button_pressed(Button.A, btnA)

#MERENI CASU UZIVATELE
stav_mereni = False
pocatecni_cas = 0
cas_mereni = 0

def spusteni_mereni():
    global pocatecni_cas, stav_mereni
    stav_mereni = True
    pocatecni_cas = control.millis()
input.on_logo_event(TouchButtonEvent.TOUCHED, spusteni_mereni)

def ukonceni_mereni():
    global pocatecni_cas, stav_mereni, cas_mereni
    konecny_cas = control.millis()
    if stav_mereni == True:
        cas_mereni = (konecny_cas - pocatecni_cas)
        stav_mereni = False
    print(cas_mereni)
    vyhodnoceni()
input.on_logo_event(TouchButtonEvent.RELEASED, ukonceni_mereni)

#VYHODNOCENI
#POKUD cas_mereni JE VETSI JAK delka_tonu, ZOBRAZI SE ">" (ODCHYLKA 0,5 SEKUNDY)
def vyhodnoceni():
    global cas_mereni, delka_tonu
    if cas_mereni <= (delka_tonu + 500):
        led.plot_bar_graph(cas_mereni, delka_tonu)
        if led.point(0, 0):
            soundExpression.happy.play()
    else:
        basic.show_leds("""
        . # . . .
        . . # . .
        . . . # .
        . . # . .
        . # . . .
        """)
        soundExpression.sad.play()

