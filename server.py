from random import random
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def guess_number():
    return('<h1 style="text-align: center;color:Blue" >Guess a number between 1 to 9</h1>'
           '<div style="text-align: center">'
           '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXRpMnBjZzlndW11YWhyMXg3ZW8xNnh4bHd0MDl'
           'jbWV5cmNvamJnYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l378khQxt68syiWJy/giphy.gif" width = "900">'
           '</div>')

random_number = random.randint(1, 9)
print(random_number)

@app.route("/<int:number>")
def found_less(number):
    if random_number > number:
        return('<h1 style="text-align:center;color:Red":> You guessed lower increase the number</h1>'
               '<div style="text-align:center">'
               '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmtpM3ZwdWU0MGV4eGlkNn'
               'RnZGFqaTcycWJveG56OTkwOWM5a2RxciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/w4zX4PfkQmZ4x'
               'eG7ny/giphy.gif"width = "900">'
               '</div>')

    if random_number < number:
        return('<h1 style="text-align:center;color:Blue":> You guessed more decrease the number</h1>'
               '<div style="text-align:center">'
               '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd20ybDliN24weHIzZzluYmN6ZWx5YmozbjZxZ3'
               'g1Z3Qzc2l0ZmZtZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZtiJXC39OIdN389opP/giphy.gif"width = "900">'
               '</div>')


    if random_number == number:
        return('<h1 style="text-align:center;color:Green":> You Win 🎉🎉🎉 </h1>'
               '<div style="text-align:center">'
               '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjFxbXg3Z2kwMW9nZmVoOWNsd2RiNmw'
               'wbW00aHdlZDZkaWtnZmV3MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IS6CvSgqzzv4T1LMDj/giphy.gif"width = "900">'
               '</div>')










if __name__ == "__main__":
    app.run(debug=True)