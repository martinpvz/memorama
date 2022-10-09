#!/usr/bin/env python3

# HTML is following
print('Content-Type: text/html')

# Leave a blank line
print('')


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memorama</title>
    <link rel="stylesheet" href="./style.css">
</head>
<body>
    <div class="header">
        <img src="./img/casino.png" alt="Casino">
    </div>
    <div class="main">
        <div class="tablero">
            <div class="carta" id="carta1">
                <img src="./img/back.png" alt="carta" class="back" id="back1" onclick="voltearCarta(this)">
                <img src="./img/alonso.png" class="front">
            </div>
            <div class="carta" id="carta2">
                <img src="./img/back.png" alt="carta" class="back" onclick="voltearCarta(this)">
                <img src="./img/bottas.png" class="front">
            </div>
            <div class="carta" id="carta3">
                <img src="./img/back.png" alt="carta" class="back" onclick="voltearCarta(this)">
                <img src="./img/checo.png" class="front">
            </div>
            <div class="carta" id="carta4">
                <img src="./img/back.png" alt="carta" class="back" onclick="voltearCarta(this)">
                <img src="./img/gasly.png" alt="" class="front">
            </div>
            <div class="carta" id="carta5">
                <img src="./img/back.png" alt="carta" class="back" onclick="voltearCarta(this)">
                <img src="./img/hamilton.png" alt="" class="front">
            </div>
            <div class="carta" id="carta6">
                <img src="./img/back.png" alt="carta" class="back" onclick="voltearCarta(this)">
                <img src="./img/checo.png" alt="" class="front">
            </div>
            <div class="carta" id="carta7">
                <img src="./img/back.png" alt="carta" class="back" onclick="voltearCarta(this)">
                <img src="./img/gasly.png" alt="" class="front">
            </div>
            <div class="carta" id="carta8">
                <img src="./img/back.png" alt="carta" class="back" onclick="voltearCarta(this)">
                <img src="./img/bottas.png" alt="" class="front">
            </div>
            <div class="carta" id="carta9">
                <img src="./img/back.png" alt="carta" class="back" onclick="voltearCarta(this)">
                <img src="./img/alonso.png" alt="" class="front">
            </div>
            <div class="carta" id="carta10">
                <img src="./img/back.png" alt="carta" class="back" onclick="voltearCarta(this)">
                <img src="./img/hamilton.png" alt="" class="front">
            </div>
        </div>
    </div>
    <script src="./main.js"></script>
</body>
</html>
""")