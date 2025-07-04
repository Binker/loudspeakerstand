# Høyttalerstativ-generator for Tandberg TL 5020

Dette prosjektet inneholder Python-kode for å generere en 3D-modell av et høyttalerstativ tilpasset Tandberg TL 5020-høyttalere ved hjelp av FreeCAD.

## Beskrivelse

Skriptet lager et stativ bestående av firkantrør (25x25 mm) med tilpassede mål for bredde, dybde og høyde. Modellen inkluderer ekstra støtterør for økt stabilitet. Koden kan enkelt tilpasses andre mål ved å endre variablene i toppen av skriptet.

## Bruk

1.  Åpne FreeCAD.
2a. Kjør `import FreeCAD as App.py` fra FreeCADs Python-konsoll eller som et makro-script.
2b. Alternativt, copy-paste koden inn i FreeCAD sitt Python-konsoll (View -> Panels -> Python console)
3.  Modellen genereres automatisk og vises i FreeCAD.

## Avhengigheter

- [FreeCAD](https://www.freecad.org/) (med Python-støtte)
- FreeCAD-modulen `Part`

## Tilpasning

Endre følgende variabler i skriptet for å tilpasse stativet:
- `stand_height` – høyde på stativet
- `stand_width` – bredde (ytterkant)
- `stand_depth` – dybde
- `tube_size` – dimensjon på firkantrør

## Lisens

Dette prosjektet er lisensiert under GNU GPL v3. Se [LICENSE](LICENSE) for detaljer.