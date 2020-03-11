# SPOPisOP
De Structured programming opdracht van op is op voordeel shop
2. Document Store naar Relationele Database Documentatie
Namen:
Thijme de Bruijn
Charlie Choffat
Iwan van der Kolk
Bart de Vries
Klas: V1B

We moesten de database zo ontwerpen dat we makkelijk de data kunnen gebruiken voor het bepalen van de recommendations, en laten we hier zien welke data we willen gebruiken voor de recommendations.
  
Eerst begonnen we met de drie al bestaande tabelen Profiles, Sessions en products. Voor profile hebben we gekozen om alleen de “_ID”(Profiles_id) en “buids”(buids) op te slaan in de database zodat we met Buids de link tussen sessions en profiles konden leggen, en ID zodat een gebruiker met een bekende ID herkent kan worden en de data van die persoon zijn vorige sessies gebruikt kan worden voor de recommendations.  
In sessions staan “Buids”(buidsbuids) om de link naar Profiles te leggen en “ _id”(Session_id) in sessions omdat we niet zeker wisten of “buids” altijd een unieke waarde is bij sessions en, dus “_id” als primaire sleutel nemen.
 

Om de link te leggen tussen de profile en de sessies hebben de een extra tabel gemaakt genaamd buids. Dit is omdat een profile meerdere buids heeft en kan je dus niet een profile aan meerdere sessies linken en hebben we het dus via buids met elkaar gelinkt. Profiles en buids zijn gelinkt door “_id”(ProfilesProfiles_id) en Buids en sessions met “buids”.
Tussen Sessions en Products hebben we ook nog een tabel toegevoegd genaamd Order omdat we anders een veel op veel relatie hadden tussen sessions en products. Op deze manier kunnen we ook goed bepalen welke producten in een sessie voorkwamen en dus recommendations geven op basis van welke producten een profile eerder heeft bekeken en gekochte producten.
Voor de data van producten hebben we gekozen voor “_id”(Product_id) als primaire sleutel, “name” , “gender”(Gender) als een bezoeker veel naar vrouwen producten kijkt weet je dat de bezoeker waarschijnlijk meer vrouwelijke producten wil en is het dus relevant om te weten of een product voor mannen of vrouwen is en kan je gespecialiseerde recommendations geven. “selling_price” (prijs) als een bezoeker naar goedkopen producten kijkt kan je producten aanraden in dezelfde prijsklasse.
We hebben ook nog de twee tabellen Brands en Categorie dit is om producten in groepen te verdelen waardoor je makkelijk recommendations kan geven op basis van wat vergelijkbare producten zijn. en als een bezoeker veel producten van een bepaalt merk bekijkt soortgelijke producten van dat merk aanraden, of producten aanraden die goed samen gaan van verschillende categorieën.
Brands bevat alleen “Brand” als primaire sleutel dit maakt het ook makkelijk als een bedrijf zijn naam verandert kan je gelijk voor alle producten de naam veranderen.  Categorie bevat als primaire sleutel “categorie”(category) en “subcategorie” (subcategorie) en “subsubcategorie”             (subsubcategorie) dit met drie soorten categorieën kan je beter specificeren welke producten het meest op elkaar lijken.  

*Afbeeldingen zijn verdwenen toen we het naar git verplaatsen

*Hierna volgt de code voor in MySQL de correcte tables te maken, kies enkel nog wel in welke database je dit wilt hebben.

CREATE TABLE Besteld (SessionsSession_id char(255) NOT NULL, ProductsProduct_id int(255) NOT NULL);
CREATE TABLE Brands (Brand_name char(255) NOT NULL, PRIMARY KEY (Brand_name));
CREATE TABLE Buids (Buids char(255) NOT NULL, ProfilesProfiles_id char(255) NOT NULL, PRIMARY KEY (Buids));
CREATE TABLE Categorie (Categorie char(255) NOT NULL, Subcategorie char(255), Subsubcategorie char(255), PRIMARY KEY (Categorie));
CREATE TABLE Products (Product_id int(255) NOT NULL AUTO_INCREMENT, Product_name char(255) NOT NULL, Gender char(255), Prijs int(11) NOT NULL, BrandsBrands char(255) NOT NULL, CategorieCategorie char(255) NOT NULL, PRIMARY KEY (Product_id));
CREATE TABLE Profiles (Profiles_id char(255) NOT NULL, PRIMARY KEY (Profiles_id));
CREATE TABLE Sessions (Session_id char(255) NOT NULL, BuidsBuids char(255) NOT NULL, PRIMARY KEY (Session_id));
ALTER TABLE Sessions ADD CONSTRAINT FKSessions485302 FOREIGN KEY (BuidsBuids) REFERENCES Buids (Buids);
ALTER TABLE Products ADD CONSTRAINT FKProducts329484 FOREIGN KEY (BrandsBrands) REFERENCES Brands (Brand_name);
ALTER TABLE Products ADD CONSTRAINT FKProducts830464 FOREIGN KEY (CategorieCategorie) REFERENCES Categorie (Categorie);
ALTER TABLE Buids ADD CONSTRAINT FKBuids241977 FOREIGN KEY (ProfilesProfiles_id) REFERENCES Profiles (Profiles_id);
ALTER TABLE Besteld ADD CONSTRAINT FKBesteld780638 FOREIGN KEY (SessionsSession_id) REFERENCES Sessions (Session_id);
ALTER TABLE Besteld ADD CONSTRAINT FKBesteld612044 FOREIGN KEY (ProductsProduct_id) REFERENCES Products (Product_id);
