---
template: presentation.html
title: "ESP32-C3 jako ultra-tani host eMMC"
# slides: TBD.pdf
youtube_url: https://www.youtube.com/watch?v=ZZTNMVtjmVM
tags:
    - builds
    - hardware design
# website: https://github.com/TBD/tbd
# attachments:
#     - folder/
#     - materials.zip
---

## Opis
Opracowanie i implementacja sterownika eMMC dla ESP32-C3, umożliwiającego odczyt i zapis pamięci eMMC przy minimalnym budżecie — około 6 zł. Sterownik może być wykorzystany jako podstawa ekstremalnie taniego czytnika/programatora eMMC, przydatnego m.in. przy odzyskiwaniu danych z uszkodzonych telefonów lub flashowaniu firmware'u płyt głównych urządzeń takich jak telewizory.

W projekcie wykorzystuję niestandardowe podejście polegające na użyciu kontrolera SPI jako programowalnej warstwy transportowej dla komunikacji eMMC w trybie 1-bit. Zamiast korzystać z natywnego kontrolera eMMC, którego ESP32-C3 nie posiada, dynamicznie przełączam funkcje oraz kierunek linii MISO/MOSI, mapując je w odpowiednich fazach komunikacji na linie CMD i DAT0 pamięci eMMC. Dzięki temu możliwe jest wysyłanie komend, odbieranie odpowiedzi oraz przesyłanie danych z użyciem SPI, GDMA i własnej implementacji protokołu eMMC.

To podejście ma charakter eksperymentalny i hackerski w najlepszym znaczeniu tego słowa: polega na kreatywnym wykorzystaniu dostępnych peryferiów ESP32-C3 poza ich typowym przeznaczeniem, aby obejść ograniczenia sprzętowe i stworzyć działające rozwiązanie przy minimalnym koszcie.

## O sobie
Piotr Siedlecki - Lubię wykorzystywać swoje umiejętności programistyczne do eksperymentowania z rozwiązaniami, w których hardware styka się z software'em. Embedded zajmuję się hobbystycznie, a najciekawsze są dla mnie projekty wymagające kreatywności, reverse engineeringu oraz używania sprzętu w sposób, do którego niekoniecznie został pierwotnie zaprojektowany.
