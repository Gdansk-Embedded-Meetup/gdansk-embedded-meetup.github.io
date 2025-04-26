<style>
    
.sponsor img {
    display: block;
    position: relative;
    margin: auto;
}

.sponsor {
    background: white;
    width: 100%;
    aspect-ratio: 1;
    padding: 1rem;
    border-radius: 1rem;
    display: grid;
    justify-content: center;
    align-items: center;
}

#partners {
    grid-template-columns: 1fr; /* Mobile-first: 1 column by default */
}


@media screen and (min-width: 40em) {
  #partners {
    grid-template-columns: repeat(3, 1fr); /* 3 columns on larger screens */
  }
}

#sponsors {
    grid-template-columns: 1fr; /* Mobile-first: 1 column by default */
}

@media screen and (min-width: 40em) {
  #sponsors {
    grid-template-columns: repeat(2, 1fr); /* 2 columns on other screens */
  }
}

</style>

<!--
Order:
- Current long term sponsors (Ambient)
- Past sponsors sorted by number of events
-->
<div class="grid" id="sponsors" markdown>
[![ambient](static/ambient.webp)](https://ambientsystem.eu/pl/ "Ambient System")
{ .sponsor }

[![solwit](static/solwit.webp)](https://solwit.com/ "Solwit")
{ .sponsor }

[![sii](static/sii.webp)](https://sii.pl/ "Sii")
{ .sponsor }

[![apator](static/apator.webp)](https://www.facebook.com/apatortelemetria/ "Apator Telemetria")
{ .sponsor }

[![ucgosu](static/ucgosu.webp)](https://www.ucgosu.pl/ "ucgosu.pl")
{ .sponsor }

[![3mdeb](static/3mdeb.webp)](https://3mdeb.com/pl/ "3mdeb")
{ .sponsor }

[![amazon](static/amazon.webp)](https://www.linkedin.com/company/amazon-development-center/ "Amazon")
{ .sponsor }

[![goodbyte](static/goodbyte.webp)](https://www.goodbyte.pl/ "GoodByte")
{ .sponsor }

[![etteplan](static/etteplan.webp)](https://www.etteplan.com/pl "Etteplan")
{ .sponsor }

[![ismacontrolli](static/ismacontrolli.webp)](https://www.ismacontrolli.com/en/ "iSMA Controlli")
{ .sponsor }

[![kplabs](static/kplabs.webp)](https://kplabs.space/ "KP Labs")
{ .sponsor }

[![msalamon](static/msalamon.webp)](https://sklep.msalamon.pl/ "msalamon.pl")
{ .sponsor }

[![nordea](static/nordea.webp)](https://nordea.pl/ "Nordea")
{ .sponsor }

[![syderal](static/syderal.webp)](https://www.syderal.pl/ "Syderal Polska")
{ .sponsor }

[![unisystem](static/unisystem.webp)](https://unisystem.pl/ "Unisystem")
{ .sponsor }

</div>
## Partnerzy organizacyjni
<div class="grid" id="partners" markdown>
[![ucgosu](static/ucgosu.webp)](https://www.ucgosu.pl/ "ucgosu.pl")
{ .sponsor }

[![msalamon](static/msalamon.webp)](https://sklep.msalamon.pl/ "msalamon.pl")
{ .sponsor }

[![codeme](static/codeme.webp)](https://codeme.pl/ "Fundacja CODE:ME")
{ .sponsor }

[![hackerspace](static/hackerspace.webp)](https://hs3.pl// "Hackerspace Trójmiasto")
{ .sponsor }

[![st](static/st.webp)](https://www.st.com/content/st_com/en.html "ST Microelectronics")
{ .sponsor }

[![jetbrains](static/jetbrains.webp)](https://www.jetbrains.com/ "JetBrains")
{ .sponsor }

</div>
