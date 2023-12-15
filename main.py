class TeaMaker:
    def __init__(self):
        self.tea_type = None
        self.sugar_level = None
        self.water_temp = None
        self.water_level = None
        self.state = 'idle'

    def start(self):
        print('Welcome to the Tea Maker!')

    def select_tea(self):
        print('Select your tea type: black, green, or herbal')
        tea_type = input()
        if tea_type in ['black', 'green', 'herbal']:
            self.tea_type = tea_type
            self.state = 'select_sugar_level'
        else:
            print('Invalid tea type. Please select again.')

    def select_sugar_level(self):
        print('Select your sugar level: low, medium, or high')
        sugar_level = input()
        if sugar_level in ['low', 'medium', 'high']:
            self.sugar_level = sugar_level
            self.state = 'heat_water'
        else:
            print('Invalid sugar level. Please select again.')

    def heat_water(self):
        print('Select water temperature: cold, warm, or boiling')
        water_temp = input()
        if water_temp in ['cold', 'warm', 'boiling']:
            self.water_temp = water_temp
            self.state = 'pour_water'
        else:
            print('Invalid water temperature. Please select again.')

    def pour_water(self):
        print('Select water level: low, medium, or high')
        water_level = input()
        if water_level in ['low', 'medium', 'high']:
            self.water_level = water_level
            self.state = 'brew_tea'
        else:
            print('Invalid water level. Please select again.')

    def brew_tea(self):
        print('Brewing tea...')
        print(f'Your {self.tea_type} tea with {self.sugar_level} sugar level is ready!')
        self.tea_type = None
        self.sugar_level = None
        self.water_temp = None
        self.water_level = None
        self.state = 'idle'

    def make_tea(self):
        if self.state == 'idle':
            self.select_tea()
        elif self.state == 'select_sugar_level':
            self.select_sugar_level()
        elif self.state == 'heat_water':
            self.heat_water()
        elif self.state == 'pour_water':
            self.pour_water()
        elif self.state == 'brew_tea':
            self.brew_tea()

# Membuat objek TeaMaker
tea_maker = TeaMaker()

# Memulai mesin
tea_maker.start()

# Memilih jenis teh
tea_maker.make_tea()

# Memilih level gula
tea_maker.make_tea()

# Memanaskan air
tea_maker.make_tea()

# Menuang air
tea_maker.make_tea()

# Menyeduh teh
tea_maker.make_tea()
