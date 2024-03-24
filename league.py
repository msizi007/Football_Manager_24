from tabulate import tabulate
class League:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams
        self.avg_rating = self.calc_avarage_rating()

        # set every club's league to this league
        for team in self.teams:
            team.league = self

    def calc_avarage_rating(self):
        total = 0
        for team in self.teams:
            total += team.avg
        self.avg_rating = total / len(self.teams)

    def order_table(self):
        self.teams.sort(key=lambda x: x.avg, reverse=True)
        for pos, team in enumerate(self.teams, start=1):
            team.league_pos = pos
    def display_table(self):
        self.order_table()
        headers = ['Name', 'P', 'W', 'D', 'L', 'GA', 'GF', 'GD', 'PTS']
        data = []
        for team in self.teams:
            data.append([team.name, team.P, team.W, 
                team.D, team.L, team.GA, team.GF, 
                team.GD, team.PTS])
        print(tabulate(data, headers=headers, tablefmt="grid"))


PREMIER_LEAGUE_CLUB_NAMES = [
    'Manchester City', 'Liverpool', 'Manchester United', 
    'Tottenham Hotspur', 'Chelsea', 'Arsenal', 'Leicester City', 
    'West Ham United', 'Everton', 'Newcastle United', 'Aston Villa', 
    'Southampton', 'Crystal Palace', 'Wolverhampton Wanderers', 
    'Leeds United', 'Brighton & Hove Albion', 'Burnley', 'Norwich City', 
    'Watford', 'Brentford']
LA_LIGA = [
    'Real Madrid CF', 'FC Barcelona', 'Atlético de Madrid', 
    'Real Betis Balompié', 'RC Celta de Vigo', 'Sevilla FC', 
    'Valencia CF', 'Real Sociedad', 'Athletic Club de Bilbao', 
    'Villarreal CF', 'RCD Espanyol de Barcelona', 'Cádiz CF', 
    'Real Valladolid CF', 'Elche CF', 'RCD Mallorca', 'Granada CF', 
    'Getafe CF', 'Rayo Vallecano', 'CA Osasuna', 'Alavés']
SERIE_A = [
    'AC Milan', 'Lazio', 'Inter', 'Roma', 'Juventus', 'Napoli',
    'U.S. Sassuolo Calcio', 'Atalanta', 'Fiorentina', 'Bologna', 
    'Sampdoria', 'Empoli', 'Torino F.C.', 'Genoa', 'Venezia FC', 
    'Spezia', 'Salernitana']
BUNDESLIGA = [
    'FC Bayern München', 'Eintracht Frankfurt', 'Borussia Dortmund',
    'Bayer 04 Leverkusen', 'Borussia Mönchengladbach', 'RB Leipzig',
    'VfL Wolfsburg', 'SC Freiburg', 'TSG Hoffenheim', '1. FC Köln',
    'VfB Stuttgart', 'FC Augsburg', 'Hertha BSC', 'Arminia Bielefeld',
    'SpVgg Greuther Fürth', 'Bochum', 'Mainz 05', 'Fürth', 
    'Fortuna Düsseldorf', 'Hamburg']
LEAGUE_1 = [
    'Paris Saint-Germain', 'AS Monaco', 'Olympique de Marseille', 
    'Lyon', 'Nice', 'Lille', 'Rennes', 'Strasbourg', 'Bordeaux', 
    'Montpellier', 'Lens', 'Nantes', 'Reims', 'Troyes', 'Metz', 'Angers', 
    'Lorient', 'Clermont', 'Brest', 'Toulouse']
EREDIVISIE = [
    'Ajax', 'PSV', 'Feyenoord', 'Vitesse', 'AZ Alkmaar', 'FC Utrecht', 
    'Heerenveen', 'Sparta Rotterdam', 'FC Groningen', 'Willem II', 
    'Heracles Almelo', 'Fortuna Sittard', 'NEC', 'Cambuur', 'RKC Waalwijk', 
    'Go Ahead Eagles', 'VVV-Venlo', 'ADO Den Haag', 'PEC Zwolle', 'Emmen']
PRIMEIRA_LIGA = [
    'FC Porto', 'SL Benfica', 'Sporting CP', 'SC Braga', 
    'Vitória Guimarães', 'Belenenses SAD', 'Famalicão', 'Boavista FC', 
    'Portimonense', 'Santa Clara', 'P. Ferreira', 'Gil Vicente', 'Arouca', 
    'Marítimo', 'Tondela', 'Estoril Praia', 'Moreirense', 'Vizela', 
    'Braga B', 'Farense']
MAJOR_LEAGUE_SOCCER = [
    'Toronto FC', 'Los Angeles FC', 'AFC Richmond', 'Minnesota United FC', 
    'New England Revolution', 'New York City FC', 'Philadelphia Union', 
    'Orlando City Soccer Club', 'Seattle Sounders FC', 'Atlanta United', 
    'Columbus Crew', 'Real Salt Lake', 'Colorado Rapids', 'Inter Miami CF', 
    'FC Cincinnati', 'Chicago Fire Football Club', 'Austin FC', 
    'Portland Timbers', 'Sporting Kansas City', 'New York Red Bulls']
BRASILEIRAO= [
    'Palmeiras', 'Flamengo', 'Atlético Mineiro', 'Fluminense', 'Santos',
    'Corinthians', 'Athletico Paranaense', 'Cruzeiro', 'Grêmio', 
    'São Paulo', 'Internacional', 'Vasco da Gama', 'Botafogo', 'Bahia', 
    'Sport Recife', 'Ceará', 'Fortaleza', 'Chapecoense', 'Goiás', 'Juventude']
ARGENTINE_PRIMERA_DIVISION= [
    'Boca Juniors', 'River Plate', 'Racing Club', 'Independiente', 
    'San Lorenzo', 'Vélez Sarsfield', 'Estudiantes (LP)', "Newell's Old Boys",
      'Rosario Central', 'Huracán', 'Argentinos Juniors', 'Banfield', 
      'Lanús', 'Talleres (C)', 'Unión (SF)', 'Colón', 'Gimnasia (LP)', 
      'Central Córdoba (SdE)', 'Patronato', 'Aldosivi']
OTHER_EUROPEAN_LEAGUES = [
    'Shakhtar Donetsk', 'Zenit St. Petersburg', 'Olympiacos', 
    'Galatasaray SK', 'Fenerbahçe', 'Beşiktaş', 'FC Basel', 
    'FC København', 'Rosenborg', 'Dynamo Kyiv', 'Ferencváros',
    'Red Star Belgrade', 'PAOK', 'AEK Athens', 'CSKA Moscow',
    'Spartak Moscow', 'Ludogorets Razgrad', 'Maccabi Tel Aviv', 
    'F91 Dudelange', 'Dinamo Zagreb']
OTHER_AMERICAN_LEAGUES = [
    'Club América', 'Club de Foot Montréal', 'Club Tijuana', 'CF Pachuca', 
    'Cruz Azul', 'Monterrey', 'Club Necaxa', 'Club León', 'Club Atlas',
    'Club Universidad Nacional', 'Club Santos Laguna', 'Tigres UANL', 
    'Querétaro FC', 'Club Atlético Mineiro', 'Palmeiras', 'Internacional',
    'São Paulo', 'Flamengo']


leagues = [
    PREMIER_LEAGUE_CLUB_NAMES, LA_LIGA, SERIE_A, BUNDESLIGA, LEAGUE_1,
    EREDIVISIE, PRIMEIRA_LIGA, MAJOR_LEAGUE_SOCCER, BRASILEIRAO,
    ARGENTINE_PRIMERA_DIVISION, OTHER_EUROPEAN_LEAGUES, OTHER_AMERICAN_LEAGUES
]


ALL_CLUB_NAMES = [
    'Paris Saint-Germain', 'Real Madrid CF', 'FC Barcelona',
    'Manchester City', 'Liverpool', 'FC Bayern München',
    'Manchester United', 'Tottenham Hotspur', 'Atlético de Madrid',
    'Chelsea', 'AC Milan', 'Lazio', 'Inter', 'Roma', 'Juventus',
    'Eintracht Frankfurt', 'Villarreal CF', 'RB Leipzig',
    'Borussia Dortmund', 'Real Betis Balompié', 'RC Celta de Vigo',
    'Sevilla FC', 'Leicester City', 'Bayer 04 Leverkusen',
    'Borussia Mönchengladbach', 'Galatasaray SK',
    'Club Nacional de Football', 'Ajax', 'U.S. Sassuolo Calcio',
    'Arsenal', 'Aston Villa', 'AS Monaco', 'Toronto FC',
    'VfL Wolfsburg', 'Athletic Club de Bilbao',
    'Newcastle United', 'Los Angeles FC', 'AFC Richmond',
    'West Ham United', 'Real Sociedad', 'TSG Hoffenheim',
    'Wolverhampton Wanderers', 'Palmeiras', 'Napoli',
    'PSV', 'Atalanta', 'OGC Nice', 'SL Benfica', 'Getafe CF',
    'Al Nassr', 'Valencia CF', 'FC Porto', 'Sport-Club Freiburg',
    'Club Athletico Paranaense', 'Everton', 'RCD Espanyol de Barcelona',
    'Olympique de Marseille', 'Royal Antwerp FC', 'Bologna', 'Sporting CP',
    'Olympique Lyonnais', 'Crystal Palace', 'Fiorentina', 'Stade Rennais FC',
    'AFC Bournemouth', 'Trabzonspor', 'Clube Atlético Mineiro', 'Flamengo',
    'RB Bragantino', 'Sport Club Corinthians Paulista', 'Fulham', 
    'Al Shabab', 'RSC Anderlecht', 'Shanghai Port FC', 'Southampton',
    'Montpellier Hérault SC', 'SC Braga', 'Racing Club de Lens', 
    'Leeds United', 'FC Nantes', 'Internacional', 'Fluminense', 
    'Dynamo Kyiv', 'Nottingham Forest', 'Dinamo Zagreb', 
    'Unión Deportiva Las Palmas', 'N.E.C. Nijmegen', 'Club Brugge KV', 
    'Udinese Calcio', 'Free agent', 'Elche CF', 'Houston Dynamo', 
    'LOSC Lille', 'US Salernitana 1919', 'AC Monza', 'Cádiz CF', 
    'New England Revolution', 'Feyenoord', 'Al Fayha', 
    'Brighton & Hove Albion', 'Rayo Vallecano', 'Santos', 'CA Osasuna', 
    'Boca Juniors', '1. FC Köln', 'Beşiktaş JK', 'Brøndby IF', 'LA Galaxy', 
    'Real Valladolid CF', 'Parma', 'Minnesota United FC', 'Fenerbahçe SK', 
    'RC Strasbourg Alsace', 'VfL Bochum 1848', 'Seattle Sounders FC', 
    'Adana Demirspor', 'Columbus Crew', 'River Plate', 'KRC Genk', 
    'Wuhan Three Towns', 'Lecce', 'SK Slavia Praha', 'VfB Stuttgart', 
    'SV Werder Bremen', 'Granada CF', 'Empoli', 'Torino F.C.', 
    'RCD Mallorca', 'Shakhtar Donetsk', 'Watford', 'FC Basel 1893', 
    'Brentford', 'U.C. Sampdoria', 'Al Hilal', 'İstanbul Başakşehir FK', 
    'Austin FC', 'Atlanta United', 'Unión Deportiva Almería', 'Al Ittihad', 
    'Rangers FC', 'Hellas Verona', 'Racing Club', 'F.C. København', 
    'Inter Miami CF', 'FC Twente', 'Levante Unión Deportiva', 'Girona FC', 
    'AZ Alkmaar', 'Stade de Reims', 'São Paulo', 'Gil Vicente FC', 
    'Real Sporting de Gijón', 'FC Augsburg', 'Wuhan FC', 'Middlesbrough', 
    'Celtic', 'Angers SCO', 'Fortuna Sittard', '1. FSV Mainz 05', 
    'Al Wehda', 'Philadelphia Union', 'PAOK', 'Stade Brestois 29', 
    'Melbourne Victory', '1. FC Union Berlin', 'Club Atlético Colón', 
    'Real Oviedo', 'FC Sion', 'Vélez Sarsfield', 'Hertha BSC', 
    'AC Sparta Praha', 'Hajduk Split', 'AEK Athens', 'Nashville SC', 
    'FC Midtjylland', 'KAA Gent', 'Antalyaspor', 'Universidad Católica', 
    'Club Olimpia', 'Panathinaikos FC', 'Shenzhen FC', 
    'Club Atlético Independiente', 'BSC Young Boys', 'Racing Santander', 
    'Fatih Karagümrük S.K.', 'Ettifaq FC', 'Chicago Fire Football Club', 
    'Clermont Foot 63', 'Ferencvárosi TC', 'FC Cincinnati', 
    'FC Viktoria Plzeň', 'Portland Timbers', 'Burnley', 'FC Utrecht', 
    'US Cremonese', 'Godoy Cruz', 'Ceará Sporting Club', 'Rio Ave FC', 
    'Servette FC', 'América Futebol Clube', 'Deportivo Alavés', 
    'Estudiantes de La Plata', 'Al Ain FC', 'FC Schalke 04', 'FC Lugano', 
    'New York City FC', 'Demir Grup Sivasspor', 'Norwich City', 
    'Adelaide United', 'América de Cali', 'Spezia', 'MKE Ankaragücü', 
    'Cuiabá', 'ESTAC Troyes', 'New York Red Bulls', 
    'FC Girondins de Bordeaux', 'FC Red Bull Salzburg', 'FC Lorient', 
    'FC Dallas', 'Royale Union Saint-Gilloise', 'Al Taawoun', 'Pisa', 
    'FBC Melgar', 'Club Atlético Talleres', 'Hull City', 
    'Club de Foot Montréal', "Newell's Old Boys", 'Al Fateh', 
    'Vitesse', 'AJ Auxerre', 'Atlético Clube Goianiense', 
    'Club Cerro Porteño', 'DSC Arminia Bielefeld', 'Daegu FC', 
    'Blackburn Rovers', 'FC Metz', 'Club Libertad', 'Orlando Pirates', 
    'Sheffield United', '1. FC Kaiserslautern', 'Abha Club', 
    'Clube Sport Marítimo', 'West Bromwich Albion', 'Venezia FC', 
    'Stade Malherbe Caen', 'D.C. United', 'Club Atlético Huracán', 
    'Malmö FF', 'Gazişehir Gaziantep F.K.', 'Atakaş Hatayspor', 
    'Sporting Kansas City', 'Cagliari', 'Gimnasia y Esgrima La Plata', 
    'Guangzhou City', 'Club Atlético Lanús', 'Genoa', 'SD Eibar', 
    'Coventry City', 'KV Mechelen', 'Argentinos Juniors', 
    'San Jose Earthquakes', 'Royal Charleroi S.C.', 'Aytemiz Alanyaspor', 
    'Santa Clara', 'Orlando City Soccer Club', 'CD Leganés', 'Al Adalah', 
    'KV Oostende', 'Standard de Liège', 'Shanghai Shenhua FC', 
    'Henan Songshan Longmen FC', 'Deportivo Ñublense', 'Boavista FC', 
    'KVC Westerlo', 'Vitória de Guimarães', 'Club Atlético Aldosivi', 
    'Queens Park Rangers', 'Club Atlético Peñarol', 'Shandong Taishan', 
    'Fortaleza', 'Club Atlético Tigre', 'Mamelodi Sundowns FC', 'Colo-Colo', 
    'Kasimpaşa SK', 'Independiente del Valle', 'Valenciennes FC', 
    'Jeonbuk Hyundai Motors', 'Deportivo Cali', 'UD Ibiza', 'Junior FC', 
    'Suwon Samsung Bluewings', 'CD Mirandés', 'SD Huesca', 
    'Heart of Midlothian', 'İttifak Holding Konyaspor', 'FK Bodø/Glimt', 
    'Hamburger SV', 'Charlotte FC', 'Club Deportes Tolima', 
    'Kaizer Chiefs', 'Toulouse Football Club', 'Damac FC', 'Casa Pia', 
    'Preston North End', 'FC Seoul', 'KV Kortrijk', 'Frosinone', 
    'Bristol City', 'Rosario Central', 'Real Salt Lake', 'Swansea City', 
    'AC Ajaccio', '1. FC Magdeburg', 'Oud-Heverlee Leuven', 'CD Tenerife', 
    'Reading', 'Málaga CF', 'Jeju United FC', 'Urbs Reggina 1914', 
    'FC Zürich', 'Cosenza', 'Atlético Tucumán', 'FC St. Gallen 1879', 
    'Hannover 96', 'APOEL Nicosia FC', 'Al Raed', 'Ulsan Hyundai FC', 
    'Club Atlético Banfield', 'LDU Quito', 'CD Everton de Viña del Mar', 
    'Shijiazhuang Ever Bright F.C.', 'Changchun Yatai FC', 
    'Yukatel Kayserispor', 'En Avant de Guingamp', 'Atlético Nacional', 
    'Chengdu Rongcheng F.C.', 'SV Darmstadt 98', 'FC Luzern', 
    'FC Paços de Ferreira', 'Unión de Santa Fe', 'Platense', 
    'GZT Giresunspor', 'Como', 'Futebol Clube de Famalicão', 
    'Western United FC', 'SK Sturm Graz', 'KAS Eupen', 
    'Defensa y Justicia', 'Nîmes Olympique', 'Paris FC', 
    'AS Saint-Étienne', 'Independiente Medellín', 'Real Zaragoza', 
    'Macarthur FC', '1. FC Nürnberg', 'Pogoń Szczecin', 'Ascoli', 
    'Portimonense SC', 'KSV Cercle Brugge', 'Unión Española', 
    'Al Khaleej', 'Legia Warszawa', 'Al Batin', 'Millwall', 'Hammarby IF', 
    'Benevento', 'Vancouver Whitecaps FC', 'Djurgårdens IF', 
    'Chamois Niortais Football Club', 'Fortuna Düsseldorf', 
    'SD Ponferradina', 'Club Alianza Lima', 'Bari', 'CFR Cluj', 
    'SV Sandhausen', 'Piast Gliwice', 'CS Emelec', 'Sint-Truidense VV', 
    'SC Heerenveen', 'FCSB (Steaua)', 'Unión La Calera', 'Colorado Rapids', 
    'FC Cartagena', 'Club Atlético Sarmiento', 'Hibernian', 'Estoril Praia', 
    'LASK Linz', 'Stoke City', 'C.D. Universidad Católica del Ecuador', 
    'Lech Poznań', 'Club Sol de América', 'San Lorenzo de Almagro', 'AIK', 
    'Club Nacional', 'Aalborg BK', 'SpVgg Greuther Fürth', 'SK Rapid Wien', 
    'Go Ahead Eagles', 'Burgos CF', 'Beijing Guoan FC', 'Derby County', 
    'FC Sochaux-Montbéliard', 'SPAL', 'CD Lugo', 'FC Vizela', 'Luton Town', 
    'Club Sporting Cristal', 'Rosenborg BK', 'Karlsruher SC', 'Palermo', 
    'Al Tai', 'Brescia', 'Cienciano', 'Molde FK', '1. FC Heidenheim 1846', 
    'Liverpool Fútbol Club', 'Huddersfield Town', 'FC St. Pauli', 
    'Aarhus GF', 'Pohang Steelers', 'Sparta Rotterdam', 'F.C. Hansa Rostock', 
    'Zhejiang Professional FC', 'Dijon FCO', 'Sheffield Wednesday', 
    'Górnik Zabrze', 'Western Sydney Wanderers', 'Club Atlético River Plate', 
    'Raków Częstochowa', 'Ternana', 'Cardiff City', 'Modena', 'FC Arouca', 
    'Rotherham United', 'Vålerenga Fotball', 'IFK Norrköping', 
    'FC Ingolstadt 04', 'Patronato', 'Melbourne City FC', 
    'Villarreal Club de Fútbol B', 'Birmingham City', 'SV Zulte Waregem', 
    'Guangzhou FC', 'FC Groningen', 'Blackpool', 'Holstein Kiel', 'SV Ried', 
    'Silkeborg IF', 'Peterborough United', 'FC Farul Constanța', 
    'Wigan Athletic', 'Suwon FC', 'Randers FC', 'SC Paderborn 07', 
    'IF Elfsborg', 'BK Häcken', 'Lyngby BK', 'Grasshopper Club Zürich', 
    'Le Havre AC', 'SSV Jahn Regensburg', 'Lillestrøm SK', 
    'Universitatea Craiova', 'Viking FK', 'Club The Strongest', 
    'Incheon United FC', 'Perth Glory', 'Eintracht Braunschweig', 
    'Perugia', 'FC Andorra', 'ATK Mohun Bagan FC', 'Ümraniyespor', 
    'Guaireña FC', 'Club Atlético Central Córdoba', 'Amiens SC', 
    'Hyderabad FC', 'Petrolul Ploiești', 'Club Always Ready', 
    'Portsmouth', 'GD Chaves', 'Sydney FC', 'Aberdeen', 'Lechia Gdańsk', 
    'Albacete BP', 'Bengaluru FC', 'Sunderland', 'FC Emmen', 'Gangwon FC', 
    'La Equidad', 'Tianjin Jinmen Tiger FC', 'Arsenal de Sarandí', 
    'Oxford United', 'Barracas Central', 'FK Austria Wien', 
    'Rapid București', 'Brisbane Roar', 'AFC UTA Arad', 'Newcastle Jets', 
    'FC Erzgebirge Aue', 'FC Volendam', 'CD Antofagasta', 'Barnsley', 
    'Kalmar FF', 'Central Coast Mariners', 'Mumbai City FC', 'Mushuc Runa', 
    'Jagiellonia Białystok', 'Meizhou Hakka', 'FC U Craiova 1948', 
    'RZ Pellets Wolfsberger AC', 'Cracovia', 'FC Annecy', 'Dundee United', 
    'Seraing', 'SC Cambuur', 'Südtirol', 'Wisła Płock', 
    'Club Deportivo Oriente Petrolero', 'Sangju Sangmu FC', 'Grenoble Foot 38', 'FC Nordsjælland', 'Strømsgodset IF', 'FC Goa', 'Radomiak Radom', 'Wycombe Wanderers', 'TSV 1860 München', 'Excelsior', 'Barcelona Sporting Club', 'Seongnam FC', 'Independiente Petrolero', 'İstanbulspor', 'Ipswich Town', 'SV Waldhof Mannheim 07', 'HJK Helsinki', 'Wellington Phoenix', 'Estudiantes de Mérida', 'St. Johnstone FC', 'Widzew Łódź', 'Caracas Fútbol Club', 'Rodez Aveyron Football', 'Royal Pari', 'IFK Göteborg', 'SG Dynamo Dresden', 'Ayacucho', 'FC Botoşani', 'Śląsk Wrocław', 'VfL Osnabrück', 'Odense Boldklub', 'Sepsi OSK Sf. Gheorghe', 'Chennaiyin FC', 'Delfín Sporting Club', 'Deportivo La Guaira FC', 'Kerala Blasters FC', 'Sarpsborg 08 FF', 'Stade Lavallois Mayenne FC',
    'TSV Egger Glas Hartberg', 'FSV Zwickau', 'Plymouth Argyle', 
    'Rot-Weiß Essen', 'Cittadella', 'Bolton Wanderers',
    'Miedź Legnica', 'Deportivo Táchira FC', 'Viborg FF', 
    'Club Deportivo Jorge Wilstermann', 'Hallescher FC', 
    'Metropolitanos de Caracas FC', 'Montevideo Wanderers', 
    'AC Horsens', 'Cheltenham Town', '1. FC Saarbrücken', 'Pau FC', 
    '9 de Octubre', 'Fleetwood Town', 'Odisha FC', 'Jamshedpur FC', 
    'Cerro Largo Fútbol Club', 'RKC Waalwijk', 'Exeter City', 
    'Dalian Professional Football Club', 'St. Mirren', 'Aalesunds FK', 
    'WSG Tirol', 'Zagłębie Lubin', 'Morecambe', 'Odds BK', 
    'Hermanos Colmenarez', 'Charlton Athletic', 'Shamrock Rovers', 
    'Club Deportivo Guabirá', 'FC Voluntari', 'AFC Chindia Târgoviște', 
    'Motherwell', 'Viktoria Köln', 'Milton Keynes Dons', 'Wrexham AFC', 
    'SC Bastia', 'Universitatea Cluj', 'Sport Boys', 'Shrewsbury Town', 
    'US Quevilly Rouen Métropole', 'Austria Lustenau', 'MSV Duisburg', 
    'Colchester United', 'Accrington Stanley', 'Campionii FC Arges', 
    'Ross County FC', 'Kilmarnock', 'GIF Sundsvall', 'SV Elversberg', 
    'Hebei FC', 'Sandefjord Fotball', 'Bradford City', 'Bohemian FC', 
    'Warta Poznań', 'Kristiansund BK', 'SV Meppen', 'SC Rheindorf Altach', 
    'VfB Oldenburg', 'PGE FKS Stal Mielec', 'Salford City',
    'Helsingborgs IF', 'Tromsø IL', 'SK Austria Klagenfurt', 
    'SC East Bengal FC', 'Forest Green Rovers', 'IK Sirius', 
    'FK Haugesund', 'Cambridge United', 'AFC Hermannstadt', 
    'Port Vale', 'General Caballero (JLM)', 'IFK Värnamo', 
    'FC Winterthur', 'SC Freiburg II', 'Livingston FC', 'Lincoln City', 
    'Mjällby AIF', 'Tranmere Rovers', 'Burton Albion', 
    'SV Wehen Wiesbaden', 'Borussia Dortmund II', 'Derry City', 
    'Leyton Orient', 'AFC Wimbledon', 'Degerfors IF', 'Northampton Town', 
    'Korona Kielce', "St. Patrick's Athletic", 'Mansfield Town', 
    'Swindon Town', 'Dundalk FC', 'Hamarkameratene', 'Harrogate Town', 
    'Doncaster Rovers', 'Hartlepool United', 'Crawley Town', 
    'Bristol Rovers', 'Sligo Rovers', 'Sportclub Verl', 'Stockport County', 
    'Varbergs BoIS FC', 'NorthEast United FC', 'Gillingham', 'CS Mioveni', 
    'Stevenage', 'Crewe Alexandra', 'Newport County', 'Carlisle United',
    'SpVgg Bayreuth', 'FK Jerv', 'Walsall', 'Rochdale', 'Grimsby Town', 
    'Sutton United', 'Barrow', 'Finn Harps', 'Drogheda United', 
    'Shelbourne FC', 'UCD AFC']

clubs_in_leagues = set(club for league in leagues for club in league)

other_clubs = []
for club in ALL_CLUB_NAMES:
    if club not in clubs_in_leagues:
        other_clubs.append(club)
        

        