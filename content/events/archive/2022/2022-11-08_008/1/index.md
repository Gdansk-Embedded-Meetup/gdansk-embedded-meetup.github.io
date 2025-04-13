---
template: presentation.html
title: Poznaj epoll
youtube_url: https://www.youtube.com/watch?v=0kG2G-7Jg4g
tags:
    - linux
attachments:
    - Poznaj epoll.pptx
---

## Opis
Pisząc aplikację na wbudowanego Linuksa warto rozważyć architekturę sterowaną zdarzeniami (ang. event-driven architecture). W architekturze sterowanej zdarzeniami potrzebny jest mechanizm wyzwalający właściwą procedurę, gdy wystąpi odpowiednie dla niej zdarzenie. Jądro Linuksa udostępnia nam w tym celu m.in. epoll. Jest to narzędzie pozwalające zasubskrybować się na zdarzenia występujące na różnych deskryptorach pliku (urządzenia, sockety, timery, sygnały i inne). Poznajmy epoll w praktyce!

## O sobie
Mateusz Przybyła (lat 36), studiował Automatykę i Robotykę na Politechnice Poznańskiej, gdzie pracował także przy projektach naukowych dotyczących algorytmów sterowania, detekcji i omijania przeszkód przez roboty mobilne (https://github.com/tysik/obstacle_detector); zawodowo zajmujący się szeroko pojętymi systemami wbudowanymi - od bare-metal, po uszyte na miarę Linuksy dla potrzeb robotyki, automatyki budynkowej, automotive itp.
