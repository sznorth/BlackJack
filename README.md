# SZBI Blackjack – Turtle alapú Blackjack játék

## Hallgató

Név: Szabó Bence István
Monogram: SZBI
Tantárgy: Szkript nyelvek Python  

------------------------------------------------------------------------------------------------------------------------

## Feladat leírása

A program egy egyszerű **Blackjack kártyajáték**, ahol a **játékos az osztó (DEALER) ellen játszik**.

- A játék egy **52 lapos francia kártyapaklit** használ.
- A lapok értéke:
  - 2–10: a saját értékük
  - J, Q, K: 10 pont
  - A (ász): 1 vagy 11 pont, a Blackjack szabály szerint
- A játékos és az osztó 2-2 lapot kap.
- A játékos dönthet:
  - **Lapot kérek** (Hit)
  - **Megállok** (Stand)
- Az osztó addig húz lapot, amíg el nem éri legalább a 17 pontot.
- A játék eldönti, ki nyert (játékos, osztó, döntetlen), és kiírja az eredményt.

A grafikus megjelenítés kizárólag a **turtle** modulra épül:

- a **DEALER** lapjai felül,
- a **Játékos** lapjai alul jelennek meg,
- középen egy vízszintes elválasztó vonal látszik,
- alul a játékos pontszáma és üzenet, felül az osztó pontszáma.

Irányítás a billentyűzettel:

- `N` – új játék indítása  
- `H` – lapot kérek (Hit)  
- `S` – megállok (Stand)  
- `Esc` – kilépés a játékból  

------------------------------------------------------------------------------------------------------------------------

## Modulok és a modulokban használt függvények

### Beépített / tanult modulok

#### `turtle`
- `turtle.Screen()` – grafikus ablak létrehozása (ez lesz a `root`)
- `turtle.Turtle()` – rajzoló objektum
- `screen.bgcolor(...)` – háttérszín beállítása
- `screen.title(...)` – ablak címe
- `screen.tracer(0, 0)` / `screen.update()` – a rajzolás frissítésének vezérlése
- `screen.onkey(..., ...)` – billentyű-események kezelése
- `screen.listen()` – billentyűk figyelése
- `screen.bye()` – ablak bezárása
- `turtle` objektum metódusai: `penup`, `pendown`, `goto`, `forward`, `left`, `fillcolor`, `begin_fill`, `end_fill`, `clear`, `write`, `hideturtle`, `speed`

#### `random`
- `random.shuffle(lista)` – a pakli megkeverése

#### `time`
- `time.sleep(0.5)` – fél másodperces késleltetés az osztó húzásai között, hogy látványos legyen a játék menete

------------------------------------------------------------------------------------------------------------------------

### Saját modul

#### `szbi_blackjack.py`

Ebben található a játék logikája és a rajzolás nagy része.

##### Saját függvények

- `szbi_create_deck()`
  - Létrehozza az 52 lapos francia kártyapaklit.
  - A lapokat `(rank, suit)` tuple-ként tárolja, pl. `("10", "♥")`.

- `szbi_calculate_hand_value(hand)`
  - Kiszámítja egy kéz (lista lapokkal) Blackjack-pontszámát.
  - Kezeli az ászokat (A) úgy, hogy lehetnek 1 vagy 11 pont értékűek.

##### Egyéb (nem monogramos) függvények / metódusok az osztályon belül

Az alábbiak az `SZBIBlackjackGame` osztály metódusai (példák):

- `bind_keys()` – a billentyűk (N, H, S, Esc) hozzárendelése
- `szbi_new_game()` – új játék indítása (pakli létrehozása, keverése, osztás)
- `player_hit()` – a játékos húz egy lapot
- `player_stand()` – a játékos megáll
- `dealer_play()` – az osztó húz, amíg el nem éri a 17 pontot
- `decide_winner()` – eldönti a játék eredményét
- `exit_game()` – kilép a programból
- `redraw()` – mindent újrarajzol a vásznon
- `draw_layout()` – elválasztó vonal rajzolása
- `draw_hands()` – a játékos és az osztó lapjainak kirajzolása
- `draw_hand(hand, y, label)` – egy kéz (lapok sorban) kirajzolása
- `draw_card(x, y, card)` – egyetlen kártyalap kirajzolása
- `draw_values_and_message()` – pontszámok és üzenet kiírása

------------------------------------------------------------------------------------------------------------------------

## Saját osztály

### `SZBIBlackjackGame`

A program fő osztálya, a nevében szerepel a monogram (SZBI).  
Feladata:

- a játék logikájának kezelése (pakli, osztás, pontszámítás, nyertes meghatározása),
- a játék állapotának tárolása (`deck`, `player_hand`, `dealer_hand`, `message`, `game_over`, `player_stood`),
- a turtle grafikus felület (asztal, kártyák, feliratok) kirajzolása,
- a billentyű-események (N, H, S, Esc) kezelése.

---

## Program felépítése

- **Indítási fájl:** `main.py`
- **Alapablak:** `root`  
  - `root = turtle.Screen()`  
- **Programnév (fő objektum):** `app`  
  - `app = SZBIBlackjackGame(root)`

A `main.py` feladata:

- létrehozza a turtle képernyőt (`root`),
- beállítja az ablak méretét,
- létrehozza a `SZBIBlackjackGame` példányt (`app`),
- meghívja a turtle főciklust (`turtle.mainloop()`), amely futtatja a játékot.

---

## Használat

1. Futtasd a `main.py` fájlt Python értelmezővel.
2. A megnyíló turtle ablakban a következő billentyűk használhatók:
   - `N` – új játék  
   - `H` – lapot kérek  
   - `S` – megállok  
   - `Esc` – kilépés  
3. A tetején a DEALER lapjai és pontszáma látható, alul a Játékos lapjai és pontszáma, lejjebb az aktuális üzenet (nyertél, vesztettél, döntetlen stb.).

------------------------------------------------------------------------------------------------------------------------
