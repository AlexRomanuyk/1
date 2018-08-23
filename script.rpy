
define h = Character("Слуга")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    # These display lines of dialogue.

    h 'Доброго ранку мій лорд,Вам лист від Короля!'
    'Лорд' 'Що вже сталось?'
    h 'Король сьогодні зранку наказав передати всім лордам королівства, 
       що від сьогодні починається полювання на Легендарного дракона, який живе в замку "Бовард"'
    menu: 
        "Взяти лист":
            'Лорд' 'Давай сюди того листа'
        "Проігнорувати лист":
            'Лорд' 'Мені це не цікаво, нехай інші з цим розбираються'
        
        
        
    # This ends the game.

    return
