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
        cas_mereni = Math.round((konecny_cas - pocatecni_cas)/1000)
        stav_mereni = False
input.on_logo_event(TouchButtonEvent.RELEASED, ukonceni_mereni)

def test():
    print(cas_mereni)
input.on_button_pressed(Button.A, test)