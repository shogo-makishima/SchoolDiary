from Scripts.Main.Settings import Settings


def GenerateButtonStyleSheet(name: str = "Back", fontSize: int = 15, fontFamily: str = "Trench"):
    return f"""
            #{name} {{
                font-size: {fontSize}pt;
                font-family: {fontFamily};
                
                background-color: rgb(25, 25, 25);

                border: 4px outset black;
                border-radius: 10 10 10 10;
                border-color: rgb(240, 240, 240);
                
                color: rgb(240, 240, 240);
            }}
            #{name}::hover {{
                background-color: rgb(20, 20, 20);
                border-color: rgb(200, 200, 200);
                color: rgb(200, 200, 200);
            }}
            #{name}:pressed {{
                background-color: rgb(15, 15, 15);
                border-color: rgb(160, 160, 160);
                color: rgb(160, 160, 160);
            }}
            
    """


def GenerateDropDownStyleSheet(name: str = "Back", fontSize: int = 15, fontFamily: str = "Trench"):
    return f"""
        #{name} {{
            font-size: {fontSize}pt;
            font-family: {fontFamily};
                
            background-color: rgb(25, 25, 25);

            border: 4px outset black;
            border-radius: 10 10 10 10;
            border-color: rgb(240, 240, 240);
                
            color: rgb(240, 240, 240);
        }}

        QComboBox QAbstractItemView {{
            color: rgb(240, 240, 240);

            border: 1px outset black;
            border-radius: 5 5 5 5;
            border-color: rgb(240, 240, 240);
        }}
    """


def GenerateDiaryDayStyleSheet(name: str = "Back", fontSize: int = 15, fontFamily: str = "Trench"):
    return f"""
            #{name} {{
                font-size: {fontSize}pt;
                font-family: {fontFamily};

                background-color: rgb(25, 25, 25);

                border: 4px outset black;
                border-radius: 10 10 10 10;
                border-color: rgb(240, 240, 240);

                color: rgb(240, 240, 240);
            }}
    """


def GenerateLabelStyleSheet(name: str = "Back", fontSize: int = 15, fontFamily: str = "Trench"):
    return f"""
            #{name} {{
                font-size: {fontSize}pt;
                font-family: {fontFamily};
                background-color: rgb(25, 25, 25);
                color: rgb(240, 240, 240);
            }}
    """
