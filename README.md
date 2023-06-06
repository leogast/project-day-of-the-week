# Day of the Week
Final Project - Introduction to Computer & Systems Sciences (Python)

Räkna ut veckodagen
Instruktioner
Uppgiften ska lösas individuellt.
Resultatet ska vara ett Python-program. Programmets källkod ska lämnas in i VPL- inlämningslådan i iLearn2 (se kursanvisningar för datum för inlämning).
Högst uppe i källkodsfilen ska en kommentar med inlämnarens namn och personnummer stå.
I samband med inlämning ska programmet testas (evalueras) i VPL (Virtual Programming Lab). Om programmet inte passerar alla tester så innehåller det fel och måste rättas och testas i VPL igen. Det finns en kort video-snutt i iLearn2 som beskriver detta förfarande.
Obs! att VPL-testning innebär att programmets input och output kontrolleras maskinellt. Detta innebär att utskrifter från programmet måste följa nedanstående instruktioner exakt!
Dialogen ska alltså vara på engelska, man får inte förkorta dialogen (man får t.ex. inte göra om ”It is” till ”It’s”), man får inte ersätta ”to” i felmeddelandena med ”-”, etc.
Uppgiften
Uppgiften går ut på att skriva ett program som läser in ett datum på formen år, månad och dag (tre heltal) och skriver ut vilken veckodag det är.
Veckodagsberäkningen SKA göras med en formel som kallas Zellers kongruens, se nedan. Programdialogen ska se ut så här (användarens inmatning i svart text):
Year: 2018 Month: 8 Day: 21
It is a Tuesday
Användarens inmatning ska kontrolleras och varje fråga ska upprepas tills användaren har besvarat den korrekt. Programdialogen skulle alltså kunna se ut så här:
Year: 1066
Out of allowed range 1583 to 9999 Year: 20178
Out of allowed range 1583 to 9999 Year: 2018
Month: 15
Out of allowed range 1 to 12 Month: 9
Day: 0
Out of allowed range 1 to 30
Day: 31
Out of allowed range 1 to 30
Day: 13
It is a Thursday
Följande ska kontrolleras:
 att årtalet är i intervallet 1583 – 9999
 att månaden är i intervallet 1-12
 att dagnummer inom månaden stämmer överens med månadsnumret, dvs att om månaden är 1, 3, 5,
7, 8, 10 eller 12 så är dagnummer i intervallet 1-31, om månaden är 4, 6, 9, eller 11 så är dagnummer i intervallet 1-30 och om månaden är 2 så är dagnummer i intervallet 1-28 eller 1-29 beroende på om det är skottår eller ej.
Det är skottår om årtalet är jämnt delbart med 400, eller om det är jämnt delbart med 4 men inte jämnt delbart med 100.
Zellers kongruensformel
Zellers kongruens (se https://en.wikipedia.org/wiki/Zeller%27s_congruence) är en formel för att räkna ut veckodagen. Den börjar gälla år 1583, året efter det att många länder övergick till den Gregorianska kalendern.
Den börjar med att man kodar om månaden så att januari resp. februari betraktas som månaderna 13 resp. 14 föregående år:
  if month == 1 or month == 2:
       month += 12
year -= 1
Sedan kan man räkna ut veckodagen ur formeln:
  weekday = ( day + 13*(month+1)//5 + year + year//4
             - year//100 + year//400 ) % 7
där veckodagen är kodad som 0 = lördag, 1 = söndag, 2 = måndag, ..., 6 = fredag.
